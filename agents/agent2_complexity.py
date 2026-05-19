import os
import sys
import json

def classify_complexity(job_details_json):
    print("\n=== AGENT 2: COMPLEXITY CLASSIFICATION ===")
    print(f"Evaluating Job Details: {job_details_json}\n")
    
    try:
        job_details = json.loads(job_details_json)
    except:
        job_details = {}
        
    urgency = job_details.get("urgency", "medium").lower()
    service = job_details.get("service_type", "plumber").lower()
    
    complexity = "Basic"
    if "ac" in service or urgency == "high":
        complexity = "Intermediate"
    if "ac" in service and urgency == "high":
        complexity = "Complex"
        
    data = {
        "complexity": complexity,
        "reasoning": f"Rule-based evaluation: Service matches type '{service}' and urgency matches level '{urgency}'."
    }
    print(f"Classification: {data['complexity']}")
    print(f"Reasoning: {data['reasoning']}")
    return data

if __name__ == "__main__":
    dummy_input = '{"language": "Roman Urdu", "service_type": "plumber", "location": "DHA Phase 2", "time": "kal", "urgency": "high", "budget_sensitivity": "high"}'
    input_data = sys.argv[1] if len(sys.argv) > 1 else dummy_input
    classify_complexity(input_data)
