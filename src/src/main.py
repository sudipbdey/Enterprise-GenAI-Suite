from tools import (generate_summary, draft_client_email, 
                   check_compliance, summarize_meeting, market_analysis)

def run_assignment():
    print("🚀 Running Enterprise-GenAI-Suite Assignment Scenarios...")

    # 1. Summary
    print("\n--- 1. Executive Summary ---")
    print(generate_summary("Quarterly report: Revenue grew 10% to $5M. Churn at 2%..."))

    # 2. Email
    print("\n--- 2. Client Email ---")
    print(draft_client_email("Phase 1 complete", "Design approved, Backend started"))

    # 3. Compliance (JSON)
    print("\n--- 3. Policy Compliance Checker ---")
    print(check_compliance("Employees must work hard. No specific leave mentioned."))

    # 4. Meeting Minutes
    print("\n--- 4. Meeting Minutes ---")
    print(summarize_meeting("John agreed to fix the login bug by Friday. Sarah will call the client."))

    # 5. Market Analysis
    print("\n--- 5. Market Brief ---")
    print(market_analysis("Tech stocks rising due to AI demand. Oil prices stabilizing."))

if __name__ == "__main__":
    run_assignment()
