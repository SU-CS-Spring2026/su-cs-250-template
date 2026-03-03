# su-cs-250-template
🛠 Student Quick-Start: Submitting Your Code
Follow these steps to download your assignment, write your Python code, and submit it for AI grading

# 1. Set up Your Computer (One-time only)
Check for Git: 
'''Type git --version. If it says "not recognized," download it from git-scm.com.

Configure your name:

```git config --global user.name "Your Full Name"```  
```git config --global user.email "your-moodle-email@saylor.org"```  

# 2. Get Your Assignment
Click the Invitation Link provided in Moodle and click "Accept Assignment."

Once your repository is ready, copy the URL (it looks like https://github.com/YourClassroom/repo-name.git).

In your Command Prompt, type:

```git clone [PASTE_URL_HERE]```  
```cd [REPO_NAME]```  

# 3. Write and Test Your Code
Open student_code.py in your favorite editor (Notepad, VS Code, etc.).

After writing your logic, test it locally by running:

```python student_code.py```  

# 4. Submit Your Work
When you are ready to be graded, run these three commands in order:

```git add student_code.py```  
```git commit -m "Finished the case study logic" ```  
```git push origin main```  

💡 Pro-Tip: Your grade is not final until you "push." Once you do, go to the Actions tab on your GitHub page to see the AI feedback from Gemini!
