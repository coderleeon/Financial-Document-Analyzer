import os
from crewai import Crew, Task
from agents import financial_analyst, verifier
from tools import pdf_reader_tool
from typing import Dict, Any

def analyze_financial_pdf(file_path: str, query: str) -> Dict[str, Any]:
    """
    Analyzes a financial PDF using the CrewAI framework.
    """
    print(f"Starting analysis for file: {file_path} with query: {query}")

    # Define tasks
    pdf_verification_task = Task(
        description=f"Verify the contents of the PDF file located at {file_path}.",
        agent=verifier,
        expected_output="A summary of the document's structure, completeness, and a confirmation that it is a valid financial document."
    )

    financial_analysis_task = Task(
        description=(
            f"Analyze the financial data from the document located at {file_path}. "
            f"Address the user's specific query: '{query}'. "
            "Identify key financial metrics, trends, and provide insights. "
            "Use the 'PDF Document Reader' tool to read the file content."
        ),
        agent=financial_analyst,
        expected_output="A detailed, comprehensive financial analysis report addressing the user's query."
    )

    # Instantiate the Crew
    crew = Crew(
        agents=[financial_analyst, verifier],
        tasks=[pdf_verification_task, financial_analysis_task],
        verbose=True
    )

    # Execute the crew and return the result
    result = crew.kickoff()
    return result