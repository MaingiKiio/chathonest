ChatHonest: Mental Health Chatbot for Kenyan Youth 😎
ChatHonest is a lit, AI-powered mental health chatbot built for Kenyan youth (ages 13–24), bringing stigma-free support straight to your vibes. Aligned with SDG 3: Good Health and Well-Being, it helps tackle stress, anxiety, and more with noma tips, psychoeducation, and local resources, all wrapped in a Gen Z, Sheng-fueled tone (think “zii,” “moto,” “fam”). Whether you’re in Nairobi or the mtaa, ChatHonest keeps it real with bilingual (English/Swahili) responses via a sleek Streamlit web-app. Spill the tea, and let’s keep your vibes honest and sawa! 🔥
Features

Bilingual Vibes: Chat in English or Swahili, with Sheng slang to keep it noma.
Mental Health Hacks: Evidence-based tips (e.g., breathing exercises, grounding) for stress and anxiety, pulled from WHO guidelines.
Kenyan Resources: Connects to legit helplines like Befrienders Kenya (+254736542304) and Mental 360 (mental360.or.ke).
Low-Bandwidth: Built for Kenya’s mobile-heavy, spotty internet vibes.
Anonymous & Safe: No user data stored, keeping it 100% zii.
Optional Supabase: Dynamic helpline updates (if you hook it up).

Tech Stack

Frontend: Streamlit (mobile-friendly, Gen Z-lit interface)
Backend: Python with regex for rule-based NLP
Database: Supabase (optional, for helpline storage)
Deployment: Streamlit Cloud for a public URL

Prerequisites
To test or deploy ChatHonest, you’ll need:

Python 3.8+ (download here)
VSCode (you’ve got this! 🎉)
Git (optional, for deployment)
Supabase account (optional, for helpline database)
GitHub account (for Streamlit Cloud deployment)

Setup Instructions
1. Clone or Download the Project

Clone the repo: git clone https://github.com/your-username/ChatHonest.git
Or download the ZIP and extract to a folder (e.g., C:\Users\YourName\ChatHonest).
Open the folder in VSCode: File > Open Folder.

2. Install Dependencies

Open VSCode’s terminal (Ctrl+` or View > Terminal).
Navigate to the project folder: cd path/to/ChatHonest.
Install packages: pip install -r requirements.txt
This installs streamlit and supabase. If errors, try pip install streamlit supabase.



3. (Optional) Set Up Supabase

Sign up at supabase.com and create a project.
Get your Supabase URL and Key from the project settings.
Set environment variables in VSCode’s terminal:
Windows: set SUPABASE_URL=your-supabase-url and set SUPABASE_KEY=your-supabase-key
Mac/Linux: export SUPABASE_URL=your-supabase-url and export SUPABASE_KEY=your-supabase-key


Create a helplines table in Supabase:
Columns: id (int, auto-increment), name (text), contact (text)
Example data: INSERT INTO helplines (name, contact) VALUES ('Befrienders Kenya', '+254736542304');


Skip this if not using Supabase; the app works fine without it.

4. Run Locally

In VSCode’s terminal, run: streamlit run mental_health_chatbot.py
A browser should open at http://localhost:8501. If not, go there manually.
Test the chatbot:
Select English or Swahili.
Try inputs like:
“I’m stressed” or “msongo” (get breathing tips + helplines).
“I’m anxious” or “wasiwasi” (get grounding tips).
“help” or “msaada” (get resource list).
“Yo” (get the “spill the tea” vibe).


Check the Gen Z Sheng vibe (“noma,” “zii,” “moto,” “fam”).



5. Troubleshoot

Python Not Found: Ensure Python is in PATH (python --version should show 3.8+). Reinstall Python, checking “Add to PATH.”
Module Not Found: Run pip install streamlit supabase again.
Port Conflict: Try streamlit run mental_health_chatbot.py --server.port 8502 and go to http://localhost:8502.
Supabase Errors: Comment out Supabase lines in mental_health_chatbot.py (lines 7–9, supabase_helplines block) if not using it.

Deployment
To share ChatHonest with the world:

Push to GitHub:
Initialize Git in VSCode (Source Control tab or git init).
Commit: git add ., git commit -m "Initial commit".
Create a GitHub repo and push: git remote add origin your-repo-url, git push -u origin main.


Deploy to Streamlit Cloud:
Sign into cloud.streamlit.io with GitHub.
Create a new app, select your repo, and set mental_health_chatbot.py as the main file.
Add Supabase URL/key as environment variables in app settings (if using).
Deploy and get a public URL (e.g., https://your-app-name.streamlit.app).


Test Live: Open the URL, interact, and share with your fam!

Usage

Open the app in a browser.
Choose English or Swahili.
Drop your thoughts (e.g., “I’m stressed about exams”).
Get zii tips or helplines in a Gen Z, Sheng-heavy tone.
Stay anonymous, keep it noma, and vibe with ChatHonest!

Project Structure

mental_health_chatbot.py: Main Streamlit app with chatbot logic.
requirements.txt: Lists dependencies (streamlit, supabase).
README.md: This file, your guide to the project.

Future Enhancements

More Sheng slang (e.g., “shuka,” “dem”) for extra mtaa vibes.
Machine learning (e.g., Hugging Face) for smarter replies.
WhatsApp integration for wider reach.
Partnerships with Mental 360 or Shamiri Institute for validation.
Anonymous feedback to keep responses lit.

Contributing
Got ideas to make ChatHonest more noma? Fork the repo, tweak the code, and submit a pull request. Let’s keep the vibes honest! 🙌
License
MIT License – feel free to use, share, and remix this project.
Contact
Questions? Hit up the repo’s issues page or DM your fam on X. Stay zii, and keep your vibes moto! 😎
