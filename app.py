import streamlit as st
import time

# --- 1. पेज सेटअप ---
st.set_page_config(page_title="X-Gen Harmony | Anil Blogger", page_icon="⚡", layout="wide")

# स्टाइल को ठीक किया गया है
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ffcc; }
    h1 { color: #ff0055; text-align: center; }
</style>
""", unsafe_allow_all_html=True)

# --- 2. सीक्रेट कोड्स ---
SECRET_CODES = ["ANIL2211K_VIP", "GANGAPUR_PRO_30", "XGEN_MASTER_99"]

if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'premium' not in st.session_state: st.session_state.premium = False

# --- 3. लॉगिन स्क्रीन ---
if not st.session_state.logged_in:
    st.title("🔐 X-GEN LOGIN")
    email = st.text_input("Enter Gmail ID")
    if st.button("ENTER"):
        if "@gmail.com" in email:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Gmail!")

# --- 4. मेन ऐप ---
else:
    st.title("🎵 X-GEN AI MUSIC LAB")
    st.write("OWNER: ANIL BLOGGER | @anil2211k")
    st.write("---")
    
    prompt = st.text_area("Write song details (e.g. Sad, Romantic, DJ):")
    duration = st.number_input("Minutes (1-60)", 1, 60, 30)

    if duration > 30 and not st.session_state.premium:
        st.warning("💎 Premium Lock! Contact @anil2211k on Instagram for Code.")
        code_input = st.text_input("Enter Secret Code", type="password")
        if st.button("ACTIVATE"):
            if code_input in SECRET_CODES:
                st.session_state.premium = True
                st.success("Premium Active!")
                st.rerun()
            else:
                st.error("Wrong Code!")
    else:
        if st.button("🚀 GENERATE MUSIC"):
            with st.spinner("AI Rendering..."):
                time.sleep(5)
                st.success("✅ Ready!")
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

