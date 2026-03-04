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
    # FIX: Define student_id from the environment for the prompt and output
    student_id = os.getenv("GITHUB_ACTOR", "Unknown_Student")
    
    filename = "student_code.py" 
    current_score = 5  # Start with a perfect score

    # 1. EXECUTION STEP: Run the code first to get the data
    stdout, stderr = run_student_code(filename)

    # 2. QA Check: Deduct points based on captured data
    if stderr:
        current_score -= 2
    elif not stdout.strip():
        current_score -= 1

    # FIX: Removed extra parenthesis from previous version
    current_score = max(0, current_score)
    
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
            model='gemini-2.0-flash', # Model available for your tier
            contents=prompt
        )
        
        clean_text = sanitize_feedback(response.text)

        print(f"### DATA_START | STUDENT: {student_id} ###")
        print(clean_text)
        print(f"### DATA_END ###")
        
    except Exception as e:
        print(f"Gemini API Error for {student_id}: {e}")
        sys.exit(1)

    # 3. REPORTER HANDSHAKE: Now dynamically using current_score
    print(f"\n<score-threshold>5</score-threshold>")
    print(f"<score>{current_score}</score>")
    print(f"Points {current_score}/5
    print(f"Hello World")

    # This forces the buffer to empty so the Reporter sees the string immediately
    sys.stdout.flush()

    # VITAL: Explicitly tell GitHub the script was 100% successful
    sys.exit(0)

if __name__ == "__main__":
    grade_submission()
