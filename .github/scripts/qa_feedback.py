import os
import sys
import subprocess
import re
from google import genai  # Modern SDK

print("*****************************************")
print("GEMINI SCRIPT IS NOW RUNNING")
print("*****************************************")


def sanitize_feedback(text):
    if not text:
        return ""
    replacements = {
        '\u202f': ' ', '\u00a0': ' ', '\u201c': '"', '\u201d': '"',
        '\u2018': "'", '\u2019': "'", '\u2013': '-', '\u2014': '--',
        '\u2026': '...'
    }
    for unicode_char, ascii_char in replacements.items():
        text = text.replace(unicode_char, ascii_char)
    
    # The Safety Net: Removes remaining non-ASCII characters
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    return text.strip()

# 2. NEW FUNCTION: Place this right before grade_submission()
def run_student_code(file_path):
    try:
        result = subprocess.run(['python3', file_path], capture_output=True, text=True, timeout=5)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)
        
# The script looks for the name you used in the 'env:' section of your YAML
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("CRITICAL QA ERROR: GEMINI_API_KEY is not set in the environment.")
    # We exit with 1 so the GitHub Action shows a Red X if the key is missing
    exit(1)

# Now the client has the credentials it needs
client = genai.Client(api_key=api_key)

def grade_submission():
    student_id = os.getenv("GITHUB_ACTOR", "Unknown_Student")
    
    # FIX 1: Define the filename clearly so the script knows what to run
    filename = "student_code.py" 

    # EXECUTION STEP: Run the code before reading the file
    stdout, stderr = run_student_code(filename)
    
    # Read the student's code
    try:
        with open(filename, "r") as f:
            student_code = f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    # Prompt Logic
    prompt = (
        f"You are a QA Reviewer. Student ID: {student_id}. "
        f"Review this Python code: {student_code}. "
        f"\n\nACTUAL EXECUTION OUTPUT:\n{stdout}"
        f"\n\nEXECUTION ERRORS:\n{stderr}"
        "\nIdentify errors without giving the solution. Be encouraging!"
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        # FIX 2: Apply the sanitizer to the response text here
        clean_text = sanitize_feedback(response.text)

        print(f"### DATA_START | STUDENT: {student_id} ###")
        print(clean_text)
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
