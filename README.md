# su-cs-250-template
🛠 Student Quick-Start: Submitting Your Code
Follow these steps to download your assignment, write your Python code, and submit it for AI grading

# Enter your code directly in GitHub  
### 1. Click the Invitation Link provided in Moodle and click "Accept Assignment."
### 2. Select student_code.py  
### 3. Click the pencil icon 
### 4. Enter your code  
### 5. Click "Commit Changes"

## Set up Git and run from local repository
Check for Git: 
'''Type git --version. If it says "not recognized," download it from git-scm.com.

Configure your name:

```git config --global user.name "Your Full Name"```  
```git config --global user.email "your-moodle-email@saylor.org"```  

## 1. Get Your Assignment
Click the Invitation Link provided in Moodle and click "Accept Assignment."

Once your repository is ready, copy the URL (it looks like https://github.com/YourClassroom/repo-name.git).

In your Command Prompt, type:

```git clone [PASTE_URL_HERE]```  
```cd [REPO_NAME]```  

## 2. Write and Test Your Code
Open student_code.py in your favorite editor (Notepad, VS Code, etc.).

After writing your logic, test it locally by running:

```python student_code.py```  

## 3. Submit Your Work
When you are ready to be graded, run these three commands in order:

```git add student_code.py```  
```git commit -m "<your name>: Submitting the CS250 unit 5 assignment" ```  
```git push origin main```  

### ✅ Submission Checklist
- [ ] **Import Check:** Does your `student_code.py` have `import math` at the top?
- [ ] **Formula Check:** Are you using `math.sqrt()`?  
- [ ] **Rounding:** Have you used round(result, 2) or an f-string to clean up the long decimal?
- [ ] **Return Type:** Is your function returning a number, not a string?
- [ ] **Final Save:** Did you save the file before your final `git commit`?

💡 Pro-Tip: Your grade is not final until you "push." Once you do, go to the Actions tab on your GitHub page to see the AI feedback from Gemini!
