import sys

def handle_dispute(dispute_type, booking_id, provider_name, customer_paid):
    print("\n=== AGENT 9: DISPUTE RESOLUTION ===")
    print(f"Processing Dispute for Booking {booking_id} against {provider_name}.")
    print(f"Dispute Type: {dispute_type}")
    
    print("\nReasoning & Action:")
    if dispute_type == "NO_SHOW":
        print("Reasoning: The provider completely failed to arrive for the scheduled job, violating platform reliability standards.")
        print(f"Action: Issuing full refund of Rs. {customer_paid} to the customer. Applying a formal WARNING to {provider_name}'s profile and temporarily docking their visibility score.")
        
    elif dispute_type == "QUALITY_COMPLAINT":
        refund_amount = round(customer_paid * 0.20, 2)
        print("Reasoning: The customer reported substandard service quality. To retain customer trust without devastating the provider's earnings over a subjective claim, a standard 20% partial refund is applied.")
        print(f"Action: Issuing partial refund of Rs. {refund_amount}. Requiring {provider_name} to submit photos of completed work for future jobs.")
        
    elif dispute_type == "PRICE_DISPUTE":
        print("Reasoning: The provider allegedly charged the customer an amount different from the app's quoted total.")
        print("Action: Initiating automated audit of invoice. Refunding the exact difference between the app quote and the physical charge to the customer. Deducting the difference from the provider's payout ledger.")
        
    elif dispute_type == "PROVIDER_CANCELS":
        print("Reasoning: The provider accepted the job but canceled beforehand, leaving the customer stranded.")
        print(f"Action: Automatically re-routing the job to the next available highest-ranked provider. Adding Rs. 200 Loyalty Credit to the customer's wallet for the inconvenience.")
        
    elif dispute_type == "UNRESOLVED":
        print("Reasoning: The nature of this dispute falls outside the standard automated rubric, potentially involving severe damage or behavioral issues.")
        print("Action: ESCALATING immediately to the Human Review Dashboard. Suspending payouts for this job until a human agent resolves the ticket.")
        
    else:
        print("Unknown dispute type.")

if __name__ == "__main__":
    disputes = ["NO_SHOW", "QUALITY_COMPLAINT", "PRICE_DISPUTE", "PROVIDER_CANCELS", "UNRESOLVED"]
    # Test all 5 to show reasoning flow
    for d in disputes:
        handle_dispute(d, "BKG-A1B2C3D4", "Ahmed Khan", 1500)
        print("-" * 40)
