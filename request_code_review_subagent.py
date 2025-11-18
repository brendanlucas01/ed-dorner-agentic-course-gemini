
import asyncio
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv(override=True)

def request_code_review():
    """
    Requests a code review using the Gemini API.
    """
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=["Please provide a brief code review focusing on the Gemini API implementation. The review should be 2-3 paragraphs, highlighting the applied changes and their benefits for the project."]
        )
        print("--- Code Review ---")
        print(response.text)
        print("--------------------")
    except Exception as e:
        print(f"An error occurred during code review: {e}")

if __name__ == '__main__':
    request_code_review()
