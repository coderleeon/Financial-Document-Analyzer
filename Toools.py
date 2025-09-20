import os
import PyPDF2
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class PDFInput(BaseModel):
    """Input schema for PDF reading tool."""
    file_path: str = Field(..., description="Path to the PDF file to read")

class FinancialDocumentTool(BaseTool):
    name: str = "PDF Document Reader"
    description: str = "Read and extract text content from PDF financial documents"
    args_schema: Type[BaseModel] = PDFInput

    def _run(self, file_path: str) -> str:
        """
        Read PDF and extract text content
        """
        try:
            if not os.path.exists(file_path):
                return f"Error: File not found at {file_path}"

            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""

                print(f"📄 Processing PDF with {len(pdf_reader.pages)} pages...")

                for page_num, page in enumerate(pdf_reader.pages):
                    try:
                        page_text = page.extract_text()
                        text += page_text + "\n"
                        print(f"    Processed page {page_num + 1}")
                    except Exception as e:
                        print(f"    Could not read page {page_num + 1}: {e}")

                text = text.replace('\n\n\n', '\n\n')
                text = ' '.join(text.split())

                if text.strip():
                    text_length = len(text)
                    if text_length > 15000:
                        text = text[:15000] + "\n\n[Text truncated for processing...]"
                        print(f" Text truncated to 15k chars (original: {text_length} chars)")

                    print(f" Successfully extracted {len(text)} characters from PDF")
                    return text
                else:
                    return "Error: No readable text found in the PDF"

        except Exception as e:
            error_msg = f"Error reading PDF file: {str(e)}"
            print(f" {error_msg}")
            return error_msg

pdf_reader_tool = FinancialDocumentTool()