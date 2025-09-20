import os
import uvicorn
import nest_asyncio
import tempfile
import uuid

from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from main import analyze_financial_pdf
from pyngrok import ngrok
from google.colab import userdata

# Apply nest_asyncio to allow nested event loops (required for Colab)
nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Financial Document Analyzer API"}

@app.post("/analyze/")
async def analyze_pdf_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Provide comprehensive financial analysis")
):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(400, "Only PDF files supported")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        result = analyze_financial_pdf(tmp_path, query)
        return {
            "status": "success",
            "filename": file.filename,
            "analysis": result
        }
    finally:
        os.unlink(tmp_path)

print("FastAPI server created!")

# Start the server and expose it with ngrok
ngrok_tunnel = ngrok.connect(8000)
print(f"Public URL: {ngrok_tunnel.public_url}")

# Run the FastAPI app
uvicorn.run(app, host="0.0.0.0", port=8000)