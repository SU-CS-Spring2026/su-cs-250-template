import os
import google.generativeai as genai

# Setup Gemini (Using the Secret we added to the Organization)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def grade_submission():
    # Read the student's actual code file
    try:
        with open("student_code.py", "r") as f:
            student_code = f.read()
    except FileNotFoundError:
        print("Error: student_code.py not found.")
        return

    # The Prompt for the AI - Specific to calculate_radius
    prompt = f"""
    You are a Student TA Grader for a CS250  Python course. 
    The student is working on a 'calculate_radius' function (where Area = pi * r^2).
    
    The student's code failed the automated tests. 
    Review the code below and provide a concise, encouraging hint. 
    
    Common pitfalls to check for:
    1. Forgetting to import the 'math' library.
    2. Using an incorrect formula (e.g., forgetting to square the radius).
    3. Returning the wrong data type (string instead of float).

    Student Code:
    {student_code}
    """}
    """

    # Generate and print feedback (this will appear in the GitHub Action logs)
    response = model.generate_content(prompt)
    print("\n--- QA FEEDBACK FROM GEMINI ---")
    print(response.text)
    print("-------------------------------\n")

if __name__ == "__main__":
    grade_submission()
