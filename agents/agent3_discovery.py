import json
import os
import math
from datetime import datetime

# Path to providers.json
PROVIDERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'providers.json')

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def discover_providers(service_type, complexity, cust_lat, cust_lng):
    print("\n=== AGENT 3: PROVIDER DISCOVERY ===")
    
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
        allowed_skills = ["Master Ustad"] # fallback to safest if unknown

    today = datetime.now()
    matched_providers = []
    
    for p in providers:
        # 1. Match service type
        if p.get("service_type") != service_type:
            continue
            
        # 2. Match PKM verified
        if not p.get("pkm_verified"):
            continue
            
        # 3. Expiry date check
        expiry_str = p.get("pkm_expiry")
        if not expiry_str or expiry_str == "null":
            continue
            
        try:
            expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
            if expiry_date < today:
                continue
        except ValueError:
            continue # Invalid date format
            
        # 4. Complexity & Skill Level check
        if p.get("skill_level") not in allowed_skills:
            continue
            
        # 5. Calculate distance
        dist = haversine_distance(cust_lat, cust_lng, p.get("location_lat"), p.get("location_lng"))
        
        # Add distance to provider object for sorting
        p_copy = p.copy()
        p_copy["distance_km"] = round(dist, 2)
        matched_providers.append(p_copy)
        
    # Sort by distance
    matched_providers.sort(key=lambda x: x["distance_km"])
    top_5 = matched_providers[:5]
    
    for idx, provider in enumerate(top_5, 1):
        print(f"{idx}. {provider['name']} ({provider['skill_level']}) - {provider['distance_km']} km away in {provider['area']}")
        
    return top_5

if __name__ == "__main__":
    # Dummy test data (DHA Karachi coords roughly)
    discover_providers("plumber", "Basic", 24.8000, 67.0400)
