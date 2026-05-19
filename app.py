from flask import Flask, render_template, request
import sys
import os
import json
import uuid
from datetime import datetime

app = Flask(__name__, template_folder='.', static_folder='static')

try:
    from main import run_pipeline
except Exception as e:
    print(f"WARNING: Could not import run_pipeline: {e}")
    def run_pipeline(query):
        return {"error": "Pipeline unavailable: backend agents failed to load."}

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/onboarding-1')
def onboarding_1():
    return render_template('onboarding-1.html')

@app.route('/onboarding-2')
def onboarding_2():
    return render_template('onboarding-2.html')

@app.route('/onboarding-3')
def onboarding_3():
    return render_template('onboarding-3.html')

@app.route('/role-selection')
def role_selection():
    return render_template('role-selection.html')

@app.route('/provider-registration', methods=['GET'])
def provider_registration():
    return render_template('provider-registration.html')

@app.route('/provider-skill-test', methods=['POST'])
def provider_skill_test():
    name = request.form.get('name', '')
    service_type = request.form.get('service_type', 'plumber')
    city = request.form.get('city', '')
    return render_template('provider-skill-test.html', name=name, service_type=service_type, city=city)

@app.route('/provider-profile', methods=['POST'])
def provider_profile_view():
    name = request.form.get('name', '')
    service_type = request.form.get('service_type', 'plumber')
    city = request.form.get('city', '')
    score = int(request.form.get('score', '2'))
    # Assign skill badge based on score
    if score >= 3:
        badge = 'Master Ustad'
        badge_color = '#1a7f4b'
    elif score == 2:
        badge = 'Verified Ustad'
        badge_color = '#1960a3'
    else:
        badge = 'Rookie'
        badge_color = '#854600'
    return render_template('provider-profile.html', name=name, service_type=service_type,
                           city=city, badge=badge, badge_color=badge_color)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bookings')
def bookings():
    bookings_list = []
    if os.path.exists('bookings.json'):
        try:
            with open('bookings.json', 'r', encoding='utf-8') as f:
                bookings_list = json.load(f)
        except Exception:
            bookings_list = []
    return render_template('bookings.html', bookings=bookings_list)

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/confirm-booking-page', methods=['POST'])
def confirm_booking_page():
    return render_template('confirm-booking.html',
        worker_name=request.form.get('worker_name'),
        skill_level=request.form.get('skill_level', 'Master Ustad'),
        service_type=request.form.get('service_type'),
        total_cost=request.form.get('total_cost'),
        date=request.form.get('date'),
        time=request.form.get('time'),
        location=request.form.get('location'),
        base_fee=request.form.get('base_fee', '0'),
        distance_cost=request.form.get('distance_cost', '0'),
        complexity_premium=request.form.get('complexity_premium', '0'),
        urgency_fee=request.form.get('urgency_fee', '0'),
        subtotal=request.form.get('subtotal', '0'),
        loyalty_discount=request.form.get('loyalty_discount', '0'),
        budget_alt=request.form.get('budget_alt', 'No alternative available.')
    )

@app.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    worker_name = request.form.get('worker_name')
    service_type = request.form.get('service_type')
    location = request.form.get('location')
    date = request.form.get('date')
    time = request.form.get('time')
    total_cost = request.form.get('total_cost')
    safe_mode = request.form.get('safe_mode', 'off')
    guardian_phone = request.form.get('guardian_phone', '')
    
    # Generate 3-character uppercase suffix for booking ID
    suffix = uuid.uuid4().hex[:3].upper()
    booking_id = f"MHR-2024-{suffix}"
    
    # Simulate Guardian Notification
    if safe_mode == 'on' and guardian_phone:
        print(f"\n--------------------------------------------------")
        print(f"GUARDIAN NOTIFIED: Sending WhatsApp to {guardian_phone}: Worker {worker_name} arriving tomorrow at {time}. CNIC verified.")
        print(f"--------------------------------------------------\n")
        
    new_booking = {
        "booking_id": booking_id,
        "provider_name": worker_name,
        "provider_phone": "+92-300-1111111",
        "service_type": service_type,
        "customer_area": location,
        "scheduled_date": date,
        "scheduled_time": time,
        "total_cost": float(total_cost) if total_cost else 0.0,
        "safe_mode": safe_mode,
        "guardian_phone": guardian_phone,
        "status": "confirmed",
        "created_at": datetime.now().isoformat()
    }
    
    bookings_list = []
    if os.path.exists('bookings.json'):
        try:
            with open('bookings.json', 'r', encoding='utf-8') as f:
                bookings_list = json.load(f)
        except Exception:
            bookings_list = []
            
    bookings_list.append(new_booking)
    
    with open('bookings.json', 'w', encoding='utf-8') as f:
        json.dump(bookings_list, f, indent=4)
        
    return render_template('booking-confirmed.html',
        booking_id=booking_id,
        worker_name=worker_name,
        date=date,
        time=time,
        price=total_cost,
        service_type=service_type,
        location=location
    )

@app.route('/api/log-call-event', methods=['POST'])
def log_call_event():
    data = request.json or {}
    event = data.get('event')
    worker_name = data.get('worker_name', 'Worker')
    service_type = data.get('service_type', 'service')
    location = data.get('location', 'location')
    time = data.get('time', 'time')
    price = data.get('price', '0')
    
    if event == 'dialing':
        print(f"\n==================================================")
        print(f"📞 CALL INITIATED: Dialing Ustad {worker_name} (+92-300-1111111)...")
        print(f"   Status: Ringing... 🔔")
        print(f"==================================================\n")
    elif event == 'connected':
        print(f"\n==================================================")
        print(f"🟢 Call Answered! AI Dispatcher speaking...")
        print(f'🤖 AI Voice: "Assalam o Alaikum {worker_name} bhai. {service_type} ka kaam hai. {location} mein, kal {time}. Total bill Rs.{price} hai. Accept karne ke liye 1 dabaein."')
        print(f"==================================================\n")
    elif event == 'accepted':
        print(f"\n==================================================")
        print(f"⌨️ Worker pressed: 1 (Accept)")
        print(f'👨 Ustad {worker_name}: "Ji bilkul, main farigh hoon. Main kal time par pahunch jaunga. Shukriya!"')
        print(f"✅ Status: Worker Accepted")
        print(f"==================================================\n")
    elif event == 'completed':
        print(f"\n==================================================")
        print(f"📴 Call Hung Up. Transitioning user to Live Job Tracking.")
        print(f"==================================================\n")
        
    return {"status": "success"}


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    # Run the 9-agent pipeline
    result = run_pipeline(query)
    
    if "error" in result:
        return f"<h1>Error</h1><p>{result['error']}</p><a href='/'>Go Back</a>"
        
    # Send the final selected provider to the results page
    return render_template('results.html', 
        service_type=result['service_type'],
        location=result.get('location', 'Unknown'),
        complexity=result['complexity'],
        provider=result['provider'],
        total_cost=result['total_cost'],
        pricing_details=result['pricing_details'],
        date=result['date'],
        time=result['time']
    )

@app.route('/live-job/<booking_id>')
def live_job(booking_id):
    bookings_list = []
    if os.path.exists('bookings.json'):
        try:
            with open('bookings.json', 'r', encoding='utf-8') as f:
                bookings_list = json.load(f)
        except Exception:
            pass
    # Find booking
    booking = None
    for b in bookings_list:
        if b['booking_id'] == booking_id:
            booking = b
            break
    if not booking:
        # fallback booking
        booking = {
            "booking_id": booking_id,
            "provider_name": "Ustad Tariq",
            "service_type": "AC Technician",
            "customer_area": "G-13",
            "scheduled_date": "Tomorrow",
            "scheduled_time": "10:00 AM",
            "total_cost": 1500,
            "safe_mode": "on",
            "guardian_phone": "+923001234567"
        }
    return render_template('live-job.html', booking=booking)

@app.route('/complete-job', methods=['POST'])
def complete_job():
    booking_id = request.form.get('booking_id')
    provider_name = request.form.get('provider_name')
    service_type = request.form.get('service_type')
    total_cost = request.form.get('total_cost')
    
    # Update status in bookings.json to "completed"
    bookings_list = []
    if os.path.exists('bookings.json'):
        try:
            with open('bookings.json', 'r', encoding='utf-8') as f:
                bookings_list = json.load(f)
            for b in bookings_list:
                if b['booking_id'] == booking_id:
                    b['status'] = 'completed'
                    break
            with open('bookings.json', 'w', encoding='utf-8') as f:
                json.dump(bookings_list, f, indent=4)
        except Exception:
            pass
            
    return render_template('payment.html',
        booking_id=booking_id,
        provider_name=provider_name,
        service_type=service_type,
        price=total_cost
    )

@app.route('/dispute/<booking_id>')
def dispute(booking_id):
    return render_template('dispute.html', booking_id=booking_id)

@app.route('/report-dispute', methods=['POST'])
def report_dispute():
    booking_id = request.form.get('booking_id')
    dispute_type = request.form.get('dispute_type')
    resolution = request.form.get('resolution')
    
    # Update status in bookings.json to "disputed"
    bookings_list = []
    if os.path.exists('bookings.json'):
        try:
            with open('bookings.json', 'r', encoding='utf-8') as f:
                bookings_list = json.load(f)
            for b in bookings_list:
                if b['booking_id'] == booking_id:
                    b['status'] = 'disputed'
                    b['dispute'] = {
                        "type": dispute_type,
                        "resolution": resolution
                    }
                    break
            with open('bookings.json', 'w', encoding='utf-8') as f:
                json.dump(bookings_list, f, indent=4)
        except Exception:
            pass
            
    print(f"\n==================================================")
    print(f"DISPUTE LOGGED for Booking {booking_id}!")
    print(f"Type: {dispute_type}")
    print(f"Resolution Action: {resolution}")
    print(f"==================================================\n")
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
        <title>Dispute Filed</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 min-h-screen flex items-center justify-center p-6 text-center">
        <div class="bg-white border border-gray-200 rounded-2xl p-8 max-w-sm w-full shadow-lg space-y-4">
            <div class="w-16 h-16 bg-red-100 text-red-600 rounded-full flex items-center justify-center mx-auto">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            </div>
            <h2 class="text-xl font-bold text-red-600">Dispute Filed</h2>
            <p class="text-sm text-gray-700 font-semibold">{resolution}</p>
            <p class="text-xs text-gray-400">Our support team will handle the refund transaction within 24 hours. Redirecting...</p>
        </div>
        <script>
            setTimeout(() => {{
                window.location.href = '/';
            }}, 3000);
        </script>
    </body>
    </html>
    """

@app.route('/guardian-notify', methods=['POST'])
def guardian_notify():
    booking_id = request.form.get('booking_id')
    guardian_phone = request.form.get('guardian_phone')
    print(f"\n==================================================")
    print(f"🚨 EMERGENCY PANIC ACTIVATED for Booking {booking_id}!")
    print(f"Instantly dispatched alert WhatsApp SMS to {guardian_phone} and emergency security response force.")
    print(f"==================================================\n")
    return {"status": "success"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    print(f"Starting Mahir AI Flask Server on http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
