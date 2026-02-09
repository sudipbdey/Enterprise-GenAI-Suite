import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

llm = ChatOpenAI(model="gpt-4o", temperature=0)

# --- 1. Executive Summary Generator ---
def generate_summary(report_text):
    prompt = PromptTemplate.from_template("""
    Act as a Senior Business Analyst. Summarize this report into a 150-word executive summary.
    Include a Markdown table of key metrics and a dedicated 'Risks/Opportunities' section.
    Report: {report}
    """)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"report": report_text})

# --- 2. Client Email Draft ---
def draft_client_email(progress, milestones, client_name="[Client Name]"):
    prompt = PromptTemplate.from_template("""
    Write a formal professional email summarizing: {progress}. 
    Milestones: {milestones}. Include placeholders for project name and deadline.
    Include a bulleted list of action items.
    """)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"progress": progress, "milestones": milestones})

# --- 3. Policy Compliance Checker ---
def check_compliance(policy_text):
    prompt = PromptTemplate.from_template("""
    Review this HR policy for missing clauses or ambiguity.
    Output ONLY valid JSON with keys: issues, severity, recommendations.
    Policy: {policy}
    """)
    chain = prompt | llm | JsonOutputParser()
    return chain.invoke({"policy": policy_text})

# --- 4. Meeting Minutes Summarizer ---
def summarize_meeting(transcript):
    prompt = PromptTemplate.from_template("""
    Summarize this transcript into: ## Decisions and ## Action Items (with owners/deadlines).
    Provide a confidence score (0-100%) for each item.
    Transcript: {transcript}
    """)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"transcript": transcript})

# --- 5. Market Analysis Brief ---
def market_analysis(articles):
    prompt = PromptTemplate.from_template("""
    Generate a market analysis brief. Include a SWOT analysis and highlight top 3 trends with citations.
    Output format: Narrative summary followed by JSON of trends.
    Articles: {articles}
    """)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"articles": articles})
