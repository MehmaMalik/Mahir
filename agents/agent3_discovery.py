import json
import os
import math
from datetime import datetime

# Path to providers.json
PROVIDERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'providers.json')

# City/area keyword mapping — maps query keywords to canonical city names
CITY_KEYWORDS = {
    "karachi": "karachi",
    "dha": "karachi",
    "clifton": "karachi",
    "gulshan": "karachi",
    "gulshan-e-iqbal": "karachi",
    "nazimabad": "karachi",
    "north nazimabad": "karachi",
    "korangi": "karachi",
    "malir": "karachi",
    "landhi": "karachi",
    "islamabad": "islamabad",
    "rawalpindi": "rawalpindi",
    "g-13": "islamabad",
    "g-11": "islamabad",
    "g-10": "islamabad",
    "g-9": "islamabad",
    "f-7": "islamabad",
    "f-8": "islamabad",
    "f-10": "islamabad",
    "i-8": "islamabad",
    "i-10": "islamabad",
    "i-14": "islamabad",
    "e-7": "islamabad",
    "blue area": "islamabad",
    "bahria town": "rawalpindi",
    "saddar": "rawalpindi",
    "lahore": "lahore",
    "dha lahore": "lahore",
    "gulberg": "lahore",
    "johar town": "lahore",
    "model town": "lahore",
    "faisalabad": "faisalabad",
    "sialkot": "sialkot",
    "multan": "multan",
    "peshawar": "peshawar",
}

def detect_city_from_query(location_str):
    """Extract canonical city name from a location string."""
    location_lower = location_str.lower().strip()
    for keyword, city in CITY_KEYWORDS.items():
        if keyword in location_lower:
            return city
    # If no match, return the raw string normalised (fallback)
    return location_lower

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometres
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def discover_providers(service_type, complexity, cust_lat, cust_lng, customer_city=None):
    print("\n=== AGENT 3: PROVIDER DISCOVERY ===")

    # Detect city from lat/lng fallback if not provided
    if customer_city:
        customer_city_canonical = detect_city_from_query(customer_city)
    else:
        customer_city_canonical = None

    print(f"City filter: {customer_city_canonical or 'none (no filter)'}")

    try:
        with open(PROVIDERS_FILE, 'r') as f:
            providers = json.load(f)
    except Exception as e:
        print(f"Error loading providers: {e}")
        return []

    # Filter rules based on complexity
    allowed_skills = []
    if complexity == "Basic":
        allowed_skills = ["Rookie", "Verified Ustad", "Master Ustad"]
    elif complexity == "Intermediate":
        allowed_skills = ["Verified Ustad", "Master Ustad"]
    elif complexity == "Complex":
        allowed_skills = ["Master Ustad"]
    else:
        allowed_skills = ["Master Ustad"]  # safest fallback

    today = datetime.now()
    matched_providers = []

    for p in providers:
        # 1. Match service type
        if p.get("service_type") != service_type:
            continue

        # 2. City matching — ONLY show providers from same city as customer
        if customer_city_canonical:
            provider_city = detect_city_from_query(p.get("city", p.get("area", "")))
            if provider_city != customer_city_canonical:
                continue

        # 3. Match PKM verified
        if not p.get("pkm_verified"):
            continue

        # 4. Expiry date check
        expiry_str = p.get("pkm_expiry")
        if not expiry_str or expiry_str == "null":
            continue

        try:
            expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
            if expiry_date < today:
                continue
        except ValueError:
            continue

        # 5. Complexity & Skill Level check
        if p.get("skill_level") not in allowed_skills:
            continue

        # 6. Calculate distance
        dist = haversine_distance(cust_lat, cust_lng, p.get("location_lat"), p.get("location_lng"))

        p_copy = p.copy()
        p_copy["distance_km"] = round(dist, 2)
        matched_providers.append(p_copy)

    # Sort by distance
    matched_providers.sort(key=lambda x: x["distance_km"])
    top_5 = matched_providers[:5]

    for idx, provider in enumerate(top_5, 1):
        print(f"{idx}. {provider['name']} ({provider['skill_level']}) - {provider['distance_km']} km away in {provider.get('area', 'Unknown')}")

    if not top_5:
        print(f"No providers found for city: {customer_city_canonical}")

    return top_5

if __name__ == "__main__":
    # Dummy test: Islamabad (G-13)
    discover_providers("plumber", "Basic", 33.6420, 72.9815, customer_city="G-13")
