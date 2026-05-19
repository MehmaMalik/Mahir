import os
import sys
import json

BASE_FEES = {
    "plumber": 1000,
    "electrician": 1200,
    "ac technician": 1500,
    "painter": 2000,
    "carpenter": 1800
}

def calculate_pricing(service_type, distance_km, complexity, is_same_day, is_returning_customer):
    print("\n=== AGENT 6: PRICING ENGINE ===")
    
    # 1. Base Fee
    base_fee = BASE_FEES.get(service_type.lower(), 1000)
    
    # 2. Distance Cost
    distance_cost = round(distance_km * 30, 2)
    
    # 3. Complexity Premium
    premium_rate = 0.0
    if complexity == "Intermediate":
        premium_rate = 0.25
    elif complexity == "Complex":
        premium_rate = 0.60
        
    complexity_premium = round(base_fee * premium_rate, 2)
    
    # 4. Urgency Fee
    urgency_fee = 200 if is_same_day else 0
    
    # Subtotal
    subtotal = base_fee + distance_cost + complexity_premium + urgency_fee
    
    # 5. Loyalty Discount
    loyalty_discount = round(subtotal * 0.05, 2) if is_returning_customer else 0
    
    # Final Total
    total = subtotal - loyalty_discount
    
    print("--- ITEMIZED BILL ---")
    print(f"Base Fee ({service_type}): Rs. {base_fee}")
    print(f"Distance Cost ({distance_km} km @ Rs.30/km): Rs. {distance_cost}")
    print(f"Complexity Premium ({complexity}): Rs. {complexity_premium}")
    print(f"Urgency Fee (Same Day): Rs. {urgency_fee}")
    print(f"Subtotal: Rs. {subtotal}")
    if is_returning_customer:
        print(f"Loyalty Discount (5%): -Rs. {loyalty_discount}")
    print(f"FINAL TOTAL: Rs. {total}")
    print("---------------------")
    
    # Budget Alternative Recommendation (Heuristics)
    if is_same_day:
        budget_alt = "Save Rs. 200 by choosing standard booking (tomorrow) instead of same-day service."
    elif complexity in ["Intermediate", "Complex"]:
        budget_alt = f"Opt for a 'Basic' complexity service package instead of {complexity} to save up to 60% of complexity premiums."
    else:
        budget_alt = "Apply a promo code or book during off-peak morning slots to get a 10% booking discount."
        
    print(f"\nBudget Alternative Option:\n{budget_alt}")
        
    return {
        "base_fee": base_fee,
        "distance_cost": distance_cost,
        "complexity_premium": complexity_premium,
        "urgency_fee": urgency_fee,
        "subtotal": subtotal,
        "loyalty_discount": loyalty_discount,
        "total": total,
        "budget_alt": budget_alt
    }

if __name__ == "__main__":
    calculate_pricing("plumber", distance_km=5.2, complexity="Intermediate", is_same_day=True, is_returning_customer=True)
