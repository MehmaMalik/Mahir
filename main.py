import sys
import os
import json
import datetime

# Try to load .env manually
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    for enc in ['utf-8', 'utf-16', 'utf-16-le']:
        try:
            with open(env_path, 'r', encoding=enc) as f:
                for line in f:
                    if '=' in line and not line.strip().startswith('#'):
                        k, v = line.strip().split('=', 1)
                        # Remove quotes if present
                        v_val = v.strip().strip("'").strip('"')
                        os.environ[k.strip()] = v_val
            break
        except Exception:
            continue

# Add agents folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from agent1_language import process_language
from agent2_complexity import classify_complexity
from agent3_discovery import discover_providers
from agent4_matching import rank_providers
from agent5_scheduling import schedule_job
from agent6_pricing import calculate_pricing
from agent7_booking import create_booking
from agent8_safety import monitor_safety
from agent9_dispute import handle_dispute

def run_pipeline(user_query):
    print("\n" + "="*60)
    print("[STARTING MAHIR AI BACKEND PIPELINE]")
    print("="*60 + "\n")
    
    # --- AGENT 1 ---
    a1_result = process_language(user_query)
    if not a1_result:
        return {"error": "Agent 1 failed to parse request."}
        
    service_type = a1_result.get("service_type")
    # Clean up service_type
    if service_type and isinstance(service_type, str):
        service_type = service_type.lower()
        if "ac" in service_type:
            service_type = "ac technician"
            
    if not service_type or service_type == "null":
        return {"error": a1_result.get("confirmation_question", "Service type not detected.")}
        
    location = a1_result.get("location", "Unknown")
    
    # --- AGENT 2 ---
    a2_result = classify_complexity(json.dumps(a1_result))
    if not a2_result:
        return {"error": "Agent 2 failed to classify complexity."}
    complexity = a2_result.get("complexity", "Basic")
    
    # --- AGENT 3 ---
    # Dummy lat/lng for G-13 (approx: 33.6420, 72.9815)
    top_5 = discover_providers(service_type, complexity, 33.6420, 72.9815, customer_city=location)
    if not top_5:
        # Fallback: try without city filter
        top_5 = discover_providers(service_type, "Basic", 24.8000, 67.0400, customer_city=None)
        if not top_5:
            return {"error": f"No {complexity} {service_type} available near you in {location}."}
        
    # --- AGENT 4 ---
    best_provider = rank_providers(top_5)
    if not best_provider:
        return {"error": "Agent 4 failed to rank providers."}
        
    # --- AGENT 5 ---
    # Parse time logic simply for demo (kal subah -> tomorrow 10am)
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    scheduled = schedule_job(best_provider['worker_id'], tomorrow, "10:00", "11:00", top_5[1:])
    
    # --- AGENT 6 ---
    is_same_day = False
    pricing_details = calculate_pricing(service_type, best_provider['distance_km'], complexity, is_same_day, False)
    total_cost = pricing_details['total']
    
    # --- AGENT 7 ---
    create_booking(best_provider['name'], "+92-300-1111111", service_type, location, tomorrow, "10:00", total_cost)
    
    # --- AGENT 8 (Simulation) ---
    print("\n[SIMULATING POST-BOOKING SAFETY]")
    monitor_safety(True, best_provider['name'], "12345-6789012-3", "10:00 AM", 60, 70) # 10 min overtime
    
    # --- AGENT 9 (Simulation) ---
    print("\n[SIMULATING POST-JOB DISPUTE]")
    handle_dispute("NO_SHOW", "BKG-DEMO-123", best_provider['name'], total_cost)
    
    print("\n" + "="*60)
    print("[PIPELINE COMPLETE]")
    print("="*60 + "\n")
    
    return {
        "service_type": service_type,
        "complexity": complexity,
        "provider": best_provider,
        "total_cost": total_cost,
        "pricing_details": pricing_details,
        "date": tomorrow,
        "time": "10:00",
        "location": location
    }

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AC bilkul kaam nahi kar raha, kal subah G-13, budget zyada nahi hai"
    run_pipeline(query)
