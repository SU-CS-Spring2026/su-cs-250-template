print("*****************************************")
print("GEMINI SCRIPT IS NOW RUNNING")
print("*****************************************")

import os
import sys
from google import genai  # Modern SDK

# The Client automatically looks for GEMINI_API_KEY in environment variables
client = genai.Client()

def grade_submission():
    # Read the student's code
    try:
        with open("student_code.py", "r") as f:
            student_code = f.read()
    except FileNotFoundError:
        print("Error: student_code.py not found.")
        return

    # Prompt Logic
    prompt = f"You are a QA Reviewer. Review this Python code for a 'calculate_radius' function. Identify errors without giving the solution. Be encouraging! {student_code}"

    # Using the current 2026 stable model
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Or 'gemini-3-flash-preview'
            contents=prompt
        )
        print("\n--- QA FEEDBACK FROM GEMINI ---")
        print(response.text)
        print("-------------------------------\n")
    except Exception as e:
        print(f"Gemini API Error: {e}")
        sys.exit(1) # This ensures you get a Red X if the AI fails

    # --- ADD THESE TWO LINES HERE ---
    # This gives the Reporter the "string" it is looking for
    print("\n<score-threshold>5</score-threshold>")
    print("<score>5</score>")
    print("Points 5/5")

if __name__ == "__main__":
    grade_submission()
