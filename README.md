** Financial Document Analyzer**

This project is a sophisticated financial document analysis system built on the CrewAI framework. It uses two specialized AI agents powered by the Google Gemini API to provide deep insights from PDF financial reports.

The system features:

A Financial Document Verifier agent that checks the integrity and completeness of the uploaded PDF.

A Senior Financial Analyst agent that performs a comprehensive analysis based on a user's query.

A FastAPI web server that exposes the system as a simple and accessible API.

**Bugs and Fixes**
The original code suffered from dependency conflicts, often referred to as "dependency hell." The pip install commands attempted to install conflicting versions of core libraries like fastapi, uvicorn, and gradio, which caused the entire application to fail.

The Fix:

To solve this, I created a new installation script that specifies known-compatible versions for all the project's dependencies. This ensures a stable and reliable environment, allowing the application to run without conflicts.
