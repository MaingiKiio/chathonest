# ChatHonest: Mental Health Chatbot for Kenyan Youth 😎

**ChatHonest** is an AI-powered mental health chatbot for Kenyan youth (ages 13–24), delivering stigma-free support with a Gen Z, Sheng-fueled vibe. Aligned with **SDG 3: Good Health and Well-Being**, it tackles stress and anxiety with noma tips, psychoeducation, and local resources. Built with Streamlit, it’s bilingual (English/Swahili), low-bandwidth, and anonymous—perfect for urban and rural fam. Spill the tea, keep it zii, and let’s make mental health moto! 🔥

## Features

- **Bilingual Vibes**: Chat in English or Swahili with Sheng slang (e.g., “noma,” “zii”).
- **Mental Health Hacks**: Evidence-based tips (e.g., breathing exercises, grounding) from WHO guidelines.
- **Kenyan Resources**: Verified helplines like Befrienders Kenya (+254736542304) and Mental 360.
- **Low-Bandwidth**: Optimized for Kenya’s mobile-heavy, spotty internet.
- **Anonymous & Safe**: No user data stored, keeping it 100% zii.
- **Optional Supabase**: Dynamic helpline updates (if enabled).

## Tech Stack

- **Frontend**: Streamlit (mobile-friendly, Gen Z-lit interface)
- **Backend**: Python with regex for rule-based NLP
- **Database**: Supabase (optional, for helplines)
- **Deployment**: Streamlit Cloud

## Prerequisites

- Python 3.8+ ([download](https://www.python.org/downloads/))
- VSCode (installed 🎉)
- Git (optional, for deployment)
- GitHub account (for Streamlit Cloud)
- Supabase account (optional, for helpline database)

## Setup Instructions

### 1. Clone or Download the Project

- Clone the repo:
  ```bash
  git clone https://github.com/your-username/ChatHonest.git
  ```
- Or download the ZIP and extract to a folder (e.g., `C:\Users\YourName\ChatHonest`).
- Open in VSCode: `File > Open Folder`.

### 2. Install Dependencies

- Open VSCode’s terminal (`Ctrl+`` or `View > Terminal`).
- Navigate to the project folder:
  ```bash
  cd path/to/ChatHonest
  ```
- Install packages:
  ```bash
  pip install -r requirements.txt
  ```
  - Installs `streamlit` and `supabase`. If errors, try:
    ```bash
    pip install streamlit supabase
    ```

### 3. (Optional) Set Up Supabase

- Sign up at [supabase.com](https://supabase.com) and create a project.
- Get your Supabase URL and Key from project settings.
- Set environment variables in VSCode’s terminal:
  - **Windows**:
    ```bash
    set SUPABASE_URL=your-supabase-url
    set SUPABASE_KEY=your-supabase-key
    ```
  - **Mac/Linux**:
    ```bash
    export SUPABASE_URL=your-supabase-url
    export SUPABASE_KEY=your-supabase-key
    ```
- Create a `helplines` table in Supabase:
  - Columns: `id` (int, auto-increment), `name` (text), `contact` (text).
  - Example data:
    ```sql
    INSERT INTO helplines (name, contact) VALUES ('Befrienders Kenya', '+254736542304');
    ```
- Skip if not using Supabase; the app works without it.

### 4. Run Locally

- In VSCode’s terminal, run:
  ```bash
  streamlit run mental_health_chatbot.py
  ```
- A browser should open at `http://localhost:8501`. If not, go there manually.
- Test the chatbot:
  - Select English or Swahili.
  - Try inputs:
    - “I’m stressed” or “msongo” (breathing tips + helplines).
    - “I’m anxious” or “wasiwasi” (grounding tips).
    - “help” or “msaada” (resource list).
    - “Yo” (“spill the tea” response).
  - Check the Sheng vibe (“noma,” “zii,” “moto,” “fam”).

### 5. Troubleshoot

- **Python Not Found**: Verify `python --version` shows 3.8+. Reinstall Python, checking “Add to PATH.”
- **Module Not Found**: Run `pip install streamlit supabase` again.
- **Port Conflict**: Try:
  ```bash
  streamlit run mental_health_chatbot.py --server.port 8502
  ```
  Then go to `http://localhost:8502`.
- **Supabase Errors**: Comment out Supabase lines in `mental_health_chatbot.py` (lines 7–9, `supabase_helplines` block) if not used.

## Deployment

Share **ChatHonest** with the world:

1. **Push to GitHub**:
   - Initialize Git in VSCode (`Source Control` tab or `git init`).
   - Commit:
     ```bash
     git add .
     git commit -m "Initial commit"
     ```
   - Create a GitHub repo and push:
     ```bash
     git remote add origin your-repo-url
     git push -u origin main
     ```

2. **Deploy to Streamlit Cloud**:
   - Sign into [cloud.streamlit.io](https://cloud.streamlit.io) with GitHub.
   - Create a new app, select your repo, set `mental_health_chatbot.py` as the main file.
   - Add Supabase URL/key as environment variables in app settings (if used).
   - Deploy to get a public URL (e.g., `https://your-app-name.streamlit.app`).

3. **Test Live**: Open the URL and interact with the chatbot.

## Usage

- Open the app in a browser.
- Choose English or Swahili.
- Drop your thoughts (e.g., “I’m stressed about exams”).
- Get zii tips or helplines in a Gen Z, Sheng-heavy tone.
- Stay anonymous and keep it noma!

## Project Structure

- `mental_health_chatbot.py`: Main Streamlit app with chatbot logic.
- `requirements.txt`: Dependencies (`streamlit`, `supabase`).
- `README.md`: This file, your guide to the project.

## Future Enhancements

- More Sheng slang (e.g., “shuka,” “dem”) for mtaa vibes.
- Machine learning (e.g., Hugging Face) for smarter replies.
- WhatsApp integration for wider reach.
- Partnerships with Mental 360 or Shamiri Institute.
- Anonymous feedback for lit responses.

## Contributing

Got ideas to make ChatHonest more noma? Fork the repo, tweak, and submit a pull request. Let’s keep the vibes honest! 🙌

## License

MIT License – use, share, and remix freely.

## Contact

Questions? Drop them in the repo’s issues page or DM on X. Stay zii, and keep your vibes moto! 😎