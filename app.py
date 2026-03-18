import streamlit as st
import time

# --- 1. स्टाइल और लुक ---
st.set_page_config(page_title="X-Gen Harmony | Anil Blogger", page_icon="⚡", layout="wide")
st.markdown("<style>.stApp { background-color: #000; color: #00ffcc; }</style>", unsafe_allow_all_html=True)

# --- 2. सीक्रेट कोड्स (Database) ---
SECRET_CODES = ["ANIL2211K_VIP", "GANGAPUR_PRO_30", "XGEN_MASTER_99"]

if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'premium' not in st.session_state: st.session_state.premium = False

# --- 3. लॉगिन सिस्टम ---
if not st.session_state.logged_in:
    st.title("🔐 X-GEN LOGIN")
    email = st.text_input("अपनी Gmail ID यहाँ लिखें")
    if st.button("ENTER SYSTEM"):
        if "@gmail.com" in email:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("कृपया वैध Gmail ID डालें!")

# --- 4. मुख्य ऐप इंटरफेस ---
else:
    st.title("🎵 X-GEN AI MUSIC LAB")
    st.write("OWNER: ANIL BLOGGER | ID: @anil2211k")
    st.write("---")
    
    prompt = st.text_area("कैसा गाना चाहिए? यहाँ लिखें:")
    duration = st.number_input("कितने मिनट का गाना? (1-60)", 1, 60, 30)

    # प्रीमियम चेक
    if duration > 30 and not st.session_state.premium:
        st.warning("💎 प्रीमियम लॉक! 30 मिनट से ज्यादा के लिए इंस्टाग्राम @anil2211k पर मैसेज करें।")
        code_input = st.text_input("सीक्रेट कोड यहाँ डालें", type="password")
        if st.button("ACTIVATE PREMIUM"):
            if code_input in SECRET_CODES:
                st.session_state.premium = True
                st.success("प्रीमियम अनलॉक हो गया!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("गलत कोड! इंस्टाग्राम पर संपर्क करें।")
    else:
        if st.button("🚀 GENERATE MUSIC"):
            if prompt:
                with st.spinner("AI गाना रेंडर कर रहा है..."):
                    time.sleep(5)
                    st.success("✅ गाना सफलतापूर्वक तैयार!")
                    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
                    st.download_button("💾 डाउनलोड करें", "data", file_name="Anil_Music.mp3")
            else:
                st.warning("भाई, पहले बताओ तो सही कि कैसा गाना चाहिए!")
