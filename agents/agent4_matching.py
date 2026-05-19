import os
import sys
import json

def rank_providers(providers):
    print("\n=== AGENT 4: MATCHING AND SELECTION ===")
    
    if not providers:
        print("No providers found to match.")
        return None
        
    # Max/Min bounds for normalization
    max_dist = max([p['distance_km'] for p in providers]) if providers else 1
    min_dist = min([p['distance_km'] for p in providers]) if providers else 0
    max_jobs = max([p['jobs_completed'] for p in providers]) if providers else 1
    
    # Avoid division by zero if all distances are exactly the same
    dist_range = max_dist - min_dist if max_dist > min_dist else 1
    
    scored_providers = []
    
    for p in providers:
        score = 0.0
        
        # 1. Distance (20%) - Lower is better. 1 = closest, 0 = furthest
        dist_score = 1.0 - ((p['distance_km'] - min_dist) / dist_range)
        score += dist_score * 20
        
        # 2. Rating (20%) - Out of 5.0
        rating_score = p['rating'] / 5.0
        score += rating_score * 20
        
        # 3. On Time Score (15%) - Out of 100
        ontime_score = p['on_time_score'] / 100.0
        score += ontime_score * 15
        
        # 4. Cancellation Rate (15%) - Lower is better. Assume max is 1.0 (100%)
        canc_score = max(0.0, 1.0 - p['cancellation_rate'])
        score += canc_score * 15
        
        # 5. Safety Score (10%) - Out of 100
        safety_score = p['safety_score'] / 100.0
        score += safety_score * 10
        
        # 6. Jobs Completed (10%) - Normalized to max jobs in group
        jobs_score = p['jobs_completed'] / max_jobs if max_jobs > 0 else 0
        score += jobs_score * 10
        
        # 7. Skill Level (5%)
        skill_score = 0.0
        if p['skill_level'] == 'Master Ustad':
            skill_score = 1.0
        elif p['skill_level'] == 'Verified Ustad':
            skill_score = 0.5
        elif p['skill_level'] == 'Rookie':
            skill_score = 0.25
        score += skill_score * 5
        
        # 8. PKM Verified (5%)
        pkm_score = 1.0 if p['pkm_verified'] else 0.0
        score += pkm_score * 5
        
        p_copy = p.copy()
        p_copy['total_score'] = round(score, 2)
        scored_providers.append(p_copy)
        
    # Sort by total score descending
    scored_providers.sort(key=lambda x: x['total_score'], reverse=True)
    
    for p in scored_providers:
        print(f"Provider: {p['name']} | Score: {p['total_score']}/100")
        
    best_provider = scored_providers[0]
    
    # Heuristic Reasoning
    reasoning = f"{best_provider['name']} was selected because they scored the highest total score of {best_provider['total_score']}/100 based on their proximity ({best_provider['distance_km']}km away) and an excellent rating of {best_provider['rating']}/5.0."
    
    print(f"\nFinal Selection: {best_provider['name']}")
    print(f"Reasoning:\n{reasoning}")
        
    return best_provider

if __name__ == "__main__":
    from agent3_discovery import discover_providers
    top_5 = discover_providers("plumber", "Basic", 24.8000, 67.0400)
    rank_providers(top_5)
