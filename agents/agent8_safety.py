import sys

def monitor_safety(safe_mode_enabled, worker_name, worker_cnic, arrival_time, expected_duration_mins, actual_elapsed_mins):
    print("\n=== AGENT 8: SAFETY MONITOR ===")
    
    if not safe_mode_enabled:
        print("Safe Mode is OFF. Standard monitoring applied.")
        return
        
    print("Safe Mode is ON.")
    
    # WhatsApp Guardian Notification
    print("\n[Sending WhatsApp to Guardian...]")
    print(f"MESSAGE: 'Alert: Service provider {worker_name} (CNIC: {worker_cnic}) arrived at your registered location at {arrival_time}. We are actively monitoring the job.'")
    
    # Timer Check
    print(f"\nMonitoring Job Timer...")
    print(f"Expected Duration: {expected_duration_mins} minutes")
    print(f"Actual Elapsed Time: {actual_elapsed_mins} minutes")
    
    if actual_elapsed_mins > expected_duration_mins:
        overtime = actual_elapsed_mins - expected_duration_mins
        print(f"\n[ESCALATION ALERT] Job has exceeded expected duration by {overtime} minutes!")
        print("Triggering automated check-in call to customer and worker to verify safety.")
    else:
        print("\nJob is progressing within the expected timeframe. No alerts triggered.")

if __name__ == "__main__":
    monitor_safety(True, "Ahmed Khan", "42201-1234567-1", "10:00 AM", 60, 75)
