import json
import os
import sys
from datetime import datetime, timedelta

SCHEDULE_FILE = os.path.join(os.path.dirname(__file__), '..', 'provider_schedules.json')

def check_availability(provider_id, target_date, target_start, target_end):
    # Load schedules
    try:
        with open(SCHEDULE_FILE, 'r') as f:
            schedules = json.load(f)
    except Exception as e:
        print(f"Error loading schedules: {e}")
        return False, []
        
    provider_schedule = schedules.get(provider_id, {}).get(target_date, [])
    
    t_start = datetime.strptime(target_start, '%H:%M')
    t_end = datetime.strptime(target_end, '%H:%M')
    
    # Add 30 min buffer to requested slot for checking
    buffered_start = t_start - timedelta(minutes=30)
    buffered_end = t_end + timedelta(minutes=30)
    
    conflict = False
    for slot in provider_schedule:
        s_start = datetime.strptime(slot['start_time'], '%H:%M')
        s_end = datetime.strptime(slot['end_time'], '%H:%M')
        
        # Check overlap
        if (buffered_start < s_end and buffered_end > s_start):
            conflict = True
            break
            
    if not conflict:
        return True, []
        
    # Find 2 alternative slots
    # Assuming standard working hours 09:00 to 18:00
    work_start = datetime.strptime('09:00', '%H:%M')
    work_end = datetime.strptime('18:00', '%H:%M')
    
    duration = t_end - t_start
    
    alternatives = []
    current_check = work_start
    
    while current_check + duration <= work_end and len(alternatives) < 2:
        c_start = current_check
        c_end = current_check + duration
        
        c_buf_start = c_start - timedelta(minutes=30)
        c_buf_end = c_end + timedelta(minutes=30)
        
        c_conflict = False
        for slot in provider_schedule:
            s_start = datetime.strptime(slot['start_time'], '%H:%M')
            s_end = datetime.strptime(slot['end_time'], '%H:%M')
            if (c_buf_start < s_end and c_buf_end > s_start):
                c_conflict = True
                break
                
        if not c_conflict:
            alternatives.append((c_start.strftime('%H:%M'), c_end.strftime('%H:%M')))
            
        current_check += timedelta(minutes=30)
        
    return False, alternatives

def schedule_job(best_provider_id, target_date, target_start, target_end, backup_providers):
    print("\n=== AGENT 5: SCHEDULING LOGISTICS ===")
    print(f"Requested Slot: {target_date} from {target_start} to {target_end} (Includes 30min travel buffers)")
    
    is_available, alternatives = check_availability(best_provider_id, target_date, target_start, target_end)
    
    if is_available:
        print(f"SUCCESS: Provider {best_provider_id} is available for the requested slot.")
        return True
    
    print(f"CONFLICT: Provider {best_provider_id} is busy during this time due to overlaps or travel buffers.")
    
    if alternatives:
        print("Suggested Alternative Slots for this Provider:")
        for alt in alternatives:
            print(f" - {alt[0]} to {alt[1]}")
    else:
        print("No alternative slots found for this provider today.")
        
    print("\nChecking Next Best Providers...")
    for backup in backup_providers:
        b_id = backup['worker_id']
        b_avail, _ = check_availability(b_id, target_date, target_start, target_end)
        if b_avail:
            print(f"Alternative Action: Book Provider {b_id} ({backup['name']}) who is available right now!")
            return False
            
    print("No backup providers available for this slot either.")
    return False

if __name__ == "__main__":
    today_str = datetime.now().strftime('%Y-%m-%d')
    # Dummy data
    top_provider = 'W-1001'
    backups = [{'worker_id': 'W-1006', 'name': 'Kamran Shah'}, {'worker_id': 'W-1011', 'name': 'Tariq Mehmood'}]
    schedule_job(top_provider, today_str, "10:00", "11:00", backups)
