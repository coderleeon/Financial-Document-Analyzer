import os
from crewai import Agent
import google.generativeai as genai
from tools import pdf_reader_tool

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Simple LLM wrapper for CrewAI compatibility
class GeminiLLM:
    def __init__(self, model_name="gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)
        self.model_name = model_name

    def invoke(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return SimpleResponse(response.text)
        except Exception as e:
            return SimpleResponse(f"LLM Error: {str(e)}")

    def __str__(self):
        return f"GeminiLLM({self.model_name})"

class SimpleResponse:
    def __init__(self, content):
        self.content = content

# Initialize Gemini LLM
llm = GeminiLLM("gemini-1.5-flash")

# Senior Financial Analyst Agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide comprehensive financial analysis based on the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with 15+ years of expertise in "
        "analyzing corporate financial statements, market trends, and investment opportunities. "
        "You provide thorough, evidence-based financial analysis with clear insights and "
        "actionable recommendations. You excel at identifying key financial metrics, "
        "trends, and potential risks or opportunities in financial documents."
    ),
    tools=[pdf_reader_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)

# Document Verification Specialist
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify the quality, completeness, and authenticity of financial documents",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous document specialist, ensuring that all financial "
        "reports and statements are of high quality, free from errors, and contain "
        "all necessary sections for a comprehensive analysis. Your work ensures "
        "the financial analyst has reliable data to work with."
    ),
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)