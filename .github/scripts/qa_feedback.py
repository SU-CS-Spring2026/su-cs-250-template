import os
import sys
from google import genai  # Modern SDK

print("*****************************************")
print("GEMINI SCRIPT IS NOW RUNNING")
print("*****************************************")

# The script looks for the name you used in the 'env:' section of your YAML
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("CRITICAL QA ERROR: GEMINI_API_KEY is not set in the environment.")
    # We exit with 1 so the GitHub Action shows a Red X if the key is missing
    exit(1)

# Now the client has the credentials it needs
client = genai.Client(api_key=api_key)

def grade_submission():
    # Grab the student's GitHub username for your Redash/Excel reports
    student_id = os.getenv("GITHUB_ACTOR", "Unknown_Student")
    
    # Read the student's code
    try:
        with open("student_code.py", "r") as f:
            student_code = f.read()
    except FileNotFoundError:
        print("Error: student_code.py not found.")
        return

    # Prompt Logic
    prompt = f"You are a QA Reviewer. Student ID: {student_id}. Review this Python code for a 'calculate_radius' function. Identify errors without giving the solution. Be encouraging! {student_code}"

    # Using the current 2026 stable model
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        # Clear markers for Stephanie to use when scraping data
        print(f"### DATA_START | STUDENT: {student_id} ###")
        print(response.text)
        print(f"### DATA_END ###")
        
    except Exception as e:
        print(f"Gemini API Error for {student_id}: {e}")
        sys.exit(1)

    # The "Reporter" handshake
    print("\n<score-threshold>5</score-threshold>")
    print("<score>5</score>")
    print("Points 5/5")

    # This forces the buffer to empty so the Reporter sees the string immediately
    sys.stdout.flush()

    # VITAL: Explicitly tell GitHub the script was 100% successful
    sys.exit(0)

if __name__ == "__main__":
    grade_submission()
