import os
import sys
import json
import uuid
from datetime import datetime

BOOKINGS_FILE = os.path.join(os.path.dirname(__file__), '..', 'bookings.json')

def create_booking(provider_name, provider_phone, service_type, customer_area, scheduled_date, scheduled_time, total_cost):
    print("\n=== AGENT 7: BOOKING & DISPATCH ===")
    
    # 1. Generate Urdu Voice Message (Keyword/Heuristic generation)
    urdu_message = f"Aap ke liye ek naya {service_type} ka kaam hai {customer_area} mein, {scheduled_date} ko {scheduled_time} bajay. Aap ki earnings Rs {total_cost} hongi. Qabool karne ke liye 1 dabayein."
        
    # 2. Simulate Twilio Voice Call
    print(f"\nCALLING {provider_name} at {provider_phone} — AI speaking in Urdu:")
    print(f"[{urdu_message}]")
    print("\n... Worker pressed 1 to accept ...")
    
    # 3. Create Booking Record
    booking_id = f"BKG-{uuid.uuid4().hex[:8].upper()}"
    
    booking_record = {
        "booking_id": booking_id,
        "provider_name": provider_name,
        "provider_phone": provider_phone,
        "service_type": service_type,
        "customer_area": customer_area,
        "scheduled_date": scheduled_date,
        "scheduled_time": scheduled_time,
        "total_cost": total_cost,
        "status": "confirmed",
        "created_at": datetime.now().isoformat()
    }
    
    bookings = []
    if os.path.exists(BOOKINGS_FILE):
        try:
            with open(BOOKINGS_FILE, 'r') as f:
                bookings = json.load(f)
        except:
            bookings = []
            
    bookings.append(booking_record)
    
    with open(BOOKINGS_FILE, 'w') as f:
        json.dump(bookings, f, indent=4)
        
    print(f"\nSUCCESS: Booking {booking_id} created and saved in bookings.json with status 'confirmed'.")

if __name__ == "__main__":
    create_booking("Ahmed Khan", "+92-300-1234567", "plumber", "DHA Karachi", "2026-05-20", "10:00", 1250)
