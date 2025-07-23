import streamlit as st
import re
from supabase import create_client, Client
import os

# Supabase setup (optional, comment out if not using)
SUPABASE_URL = os.getenv("SUPABASE_URL", "your-supabase-url")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-supabase-key")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Response dictionary with English and Swahili triggers
responses = {
    r"(stress|stressed|pressure|msongo|shinikizo)": {
        "message_en": "Yo, fam, stress is tryna mess with your honest vibes! Let’s keep it noma: Breathe in for 4 secs, hold for 4, exhale for 4. Do it 3 times. Wanna more zii tricks or a helpline to stay moto?",
        "message_sw": "Pole, fam, msongo unajaribu kuharibu vibes zako za honest! Tufanye iwe noma: Vuta pumzi kwa sekunde 4, shikilia kwa 4, toa kwa 4. Rudia mara 3. Unataka tricks za zii au nambari ya msaada ili uwe moto?",
        "resources": [
            "Befrienders Kenya: +254736542304 or +254722178177",
            "Mental 360: Visit mental360.or.ke",
            "EMKF Crisis Line: 0800 723 253"
        ]
    },
    r"(anxiety|anxious|nervous|wasiwasi|hofu)": {
        "message_en": "Ayo, fam, anxiety’s tryna fade your honest vibes. Let’s spark it up: Name 5 things you see around you to stay zii. Wanna try or grab a helpline to keep it noma?",
        "message_sw": "Nakuelewa, fam, wasiwasi unajaribu kufade vibes zako za honest. Tuwasha tena: Taja vitu 5 unavyoona karibu nawe ili uwe zii. Unataka kujaribu au kuchukua nambari ya msaada ili iwe noma?",
        "resources": [
            "Befrienders Kenya: +254722178177",
            "CBT Kenya: +254739935333",
            "Kamili Organisation: kamilimentalhealth.org"
        ]
    },
    r"(help|support|msaada)": {
        "message_en": "You ain’t solo, fam! Here’s some lit resources to keep your honest vibes strong and noma.",
        "message_sw": "Hauko peke yako, fam! Hapa kuna rasilimali za moto ili kuweka vibes zako za honest imara na noma.",
        "resources": [
            "Befrienders Kenya: +254736542304 or +254722178177",
            "Mental 360: mental360.or.ke",
            "Niskize: 0900 620 800"
        ]
    },
    r".*": {
        "message_en": "Yo, fam, I’m here to catch your honest vibes. What’s the tea today? Spill it, or I can hook you up with some noma support to stay zii.",
        "message_sw": "Yo, fam, niko hapa kukupata vibes zako za honest. Tea iko aje leo? Shuka nayo, au naweza kukuunganisha na msaada wa noma ili uwe zii.",
        "resources": []
    }
}

# Fetch resources from Supabase (optional)
def fetch_helplines():
    try:
        response = supabase.table("helplines").select("*").execute()
        return [f"{row['name']}: {row['contact']}" for row in response.data]
    except:
        return []

# Streamlit app
st.title("ChatHonest: Mental Health Support for Kenyan Youth")
st.write("A lit spot to spill your tea and keep it real, in English or Swahili. Drop what’s popping, and I’ll hit you with zii tips or resources. Stay noma, fam! 😎")

# Language selection
language = st.selectbox("Choose Language / Chagua Lugha", ["English", "Swahili"])

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("What’s the tea with your vibes today, fam? / Tea yako leo iko aje, fam?")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Find matching response
    bot_response = None
    for pattern, response in responses.items():
        if re.search(pattern, user_input.lower()):
            bot_response = response["message_sw" if language == "Swahili" else "message_en"]
            if response["resources"]:
                bot_response += "\n\n**Resources / Rasilimali**:\n" + "\n".join(response["resources"])
            break

    # Fallback to default response
    if not bot_response:
        bot_response = responses[r".*"]["message_sw" if language == "Swahili" else "message_en"]

    # Append Supabase helplines (if enabled)
    supabase_helplines = fetch_helplines()
    if supabase_helplines:
        bot_response += "\n\n**More Resources / Rasilimali za Ziada**:\n" + "\n".join(supabase_helplines)

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})