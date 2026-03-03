import os
import google.generativeai as genai

# Setup Gemini (Using the Secret we added to the Organization)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash')

def grade_submission():
    # Read the student's actual code file
    try:
        with open("student_code.py", "r") as f:
            student_code = f.read()
    except FileNotFoundError:
        print("Error: student_code.py not found.")
        return

    # The Prompt for the AI
    prompt = f"""
    You are a QA Reviewer for an MBA Python course. 
    The student is working on a 'calculate_radius' function.
    The student's code failed the tests. Review this code:
    {student_code}
    """

    # Ensure this line starts at the EXACT same column as 'prompt' above
    response = model.generate_content(prompt)
    print("\n--- QA FEEDBACK FROM GEMINI ---")
    print(response.text)
    print("-------------------------------\n")

if __name__ == "__main__":
    grade_submission()
