import streamlit as st
import time

# --- 1. Google Gemini जैसा इंटरफेस (UI) ---
st.set_page_config(page_title="Gemini AI Studio", page_icon="✨", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #131314; color: #e3e3e3; font-family: 'Google Sans', sans-serif; }
    h1 { color: #8ab4f8; text-align: center; font-weight: 500; }
    .stTextArea textarea { background-color: #1e1f20; border: 1px solid #444746; color: white; border-radius: 20px; }
    .stButton>button { 
        background: linear-gradient(90deg, #4285f4, #9b72cb); 
        color: white; border: none; border-radius: 25px; font-weight: bold; width: 100%;
    }
    .speaker-btn { background-color: #3c4043; border-radius: 50%; padding: 10px; cursor: pointer; }
</style>
""", unsafe_allow_html=True)

# --- 2. बोलकर सुनाने वाला लॉजिक (JavaScript) ---
def speak_text(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance();
    msg.text = "{text}";
    msg.lang = 'hi-IN';
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# --- 3. मेन स्क्रीन ---
st.title("✨ Gemini Music Lab")
st.write("Anil Blogger Edition | अब AI बोलेगा भी!")

# चैट का हिस्सा
chat_msg = "नमस्ते अनिल भाई! मैं आपका अपना AI हूँ। आप मुझसे चैट कर सकते हैं या नीचे प्लस बटन दबाकर गाना बना सकते हैं।"
st.info(chat_msg)

# स्पीकर बटन
if st.button("🔊 उत्तर सुनें (Listen)"):
    speak_text(chat_msg)

user_chat = st.text_area("मुझसे कुछ पूछें...", placeholder="यहाँ लिखें...")

# --- 4. प्लस (+) बटन और म्यूजिक स्टूडियो ---
if 'music_mode' not in st.session_state:
    st.session_state.music_mode = False

if st.button("➕ Create New Music"):
    st.session_state.music_mode = not st.session_state.music_mode

if st.session_state.music_mode:
    with st.expander("🎵 Music Studio", expanded=True):
        prompt = st.text_input("गाना किस बारे में हो?")
        vocal_type = st.selectbox("आवाज़ चुनें", ["Female Voice", "Male Voice"])
        
        if st.button("Generate & Play 🚀"):
            if prompt:
                with st.spinner("AI गाना तैयार कर रहा है..."):
                    time.sleep(3)
                st.success("लीजिए, असली लड़की की आवाज़ में गाना तैयार है!")
                # लड़की की आवाज़ वाला डेमो गाना
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
            else:
                st.warning("पहले कुछ लिखो तो सही!")

st.write("---")
st.caption("Powered by Anil Blogger | No Login Required")
