import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  

def parse_task(text):
    prompt = f"""
Extract the following fields from this task description and return a clean JSON object:
- title
- priority
- due_date
- category

Only output raw JSON. Do not include code blocks or text.

Task: {text}
"""

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        print("\n Gemini Raw Output-")
        print(raw)
        print("\n")

        # Remove any triple backticks if Gemini still returns them
        if raw.startswith("```json") or raw.startswith("```"):
            raw = raw.replace("```json", "").replace("```", "").strip()

        # Convert to Python dictionary
        return json.loads(raw)

    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        return None
    except Exception as e:
        print("General error:", e)
        return None
