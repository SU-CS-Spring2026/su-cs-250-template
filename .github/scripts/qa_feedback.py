print("*****************************************")
print("GEMINI SCRIPT IS NOW RUNNING")
print("*****************************************")

import os
from google import genai  # Correct New SDK import

# 1. Setup the Client
# The new SDK uses a Client object. It automatically finds "GEMINI_API_KEY"
# in your environment variables, so we don't need os.environ manually.
client = genai.Client()

def grade_submission():
    # Read the student's actual code file
    try:
        with open("student_code.py", "r") as f:
            student_code = f.read()
    except FileNotFoundError:
        print("Error: student_code.py not found.")
        return

    # 2. The Prompt for the AI
    prompt = f"""
    You are a QA Reviewer for the CS250 Python course. 
    The student is working on a 'calculate_radius' function.
    The student's code failed the tests. Identify the error without giving them the final code. 
    Review this code:
    {student_code}
    """

    # 3. Generate Content using the Client
    # We use 'gemini-2.5-flash' which is the current stable high-speed model.
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        print("\n--- QA FEEDBACK FROM GEMINI ---")
        print(response.text)
        print("-------------------------------\n")
    except Exception as e:
        print(f"Gemini API Error: {e}")

if __name__ == "__main__":
    grade_submission()
