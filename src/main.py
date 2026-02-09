
import os
import json
from dotenv import load_dotenv
from tools import (
    generate_summary, 
    draft_client_email, 
    check_compliance, 
    summarize_meeting, 
    market_analysis
)

# Load environment variables
load_dotenv()

def run_assignment_demo():
    # 1. Load the Test Data
    data_path = os.path.join('data', 'test_data.json')
    
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found. Please create the JSON file first.")
        return

    with open(data_path, 'r') as f:
        test_data = json.load(f)

    print("="*60)
    print("🚀 ENTERPRISE GEN-AI SUITE: SESSION 3 DELIVERABLES")
    print("="*60)

    # --- TASK 1: Executive Summary ---
    print("\n[TASK 1] Executive Summary Generator")
    summary = generate_summary(test_data['performance_report']['content'])
    print(summary)
    print("-" * 40)

    # --- TASK 2: Client Email Draft ---
    print("\n[TASK 2] Client Email Draft")
    email = draft_client_email(
        test_data['project_status']['progress'], 
        test_data['project_status']['milestones']
    )
    print(email)
    print("-" * 40)

    # --- TASK 3: Policy Compliance Checker ---
    print("\n[TASK 3] Policy Compliance Checker (JSON Output)")
    compliance = check_compliance(test_data['hr_policy']['content'])
    # Using json.dumps to ensure it prints as pretty-formatted JSON
    print(json.dumps(compliance, indent=4))
    print("-" * 40)

    # --- TASK 4: Meeting Minutes Summarizer ---
    print("\n[TASK 4] Meeting Minutes Summarizer (Markdown)")
    minutes = summarize_meeting(test_data['meeting_transcript']['transcript'])
    print(minutes)
    print("-" * 40)

    # --- TASK 5: Market Analysis Brief ---
    print("\n[TASK 5] Market Analysis Brief")
    # Joining the list of news articles into one string for the LLM
    news_string = " ".join([item['text'] for item in test_data['market_news']])
    market_brief = market_analysis(news_string)
    print(market_brief)
    
    print("\n" + "="*60)
    print("✅ DEMO COMPLETE: All 5 Scenarios Processed")
    print("="*60)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Missing OPENAI_API_KEY in .env file!")
    else:
        run_assignment_demo()
