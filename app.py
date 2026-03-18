import streamlit as st
import time

# --- 1. पेज सेटअप ---
st.set_page_config(page_title="X-Gen Harmony | Anil Blogger", page_icon="⚡", layout="wide")

# सुधरा हुआ लुक (CSS)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ffcc; }
    h1 { color: #ff0055; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 2. डेटाबेस ---
SECRET_CODES = ["ANIL2211K_VIP", "GANGAPUR_PRO_30", "XGEN_MASTER_99"]

if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'premium' not in st.session_state: st.session_state.premium = False

# --- 3. लॉगिन ---
if not st.session_state.logged_in:
    st.title("🔐 X-GEN LOGIN")
    email = st.text_input("Enter Gmail ID")
    if st.button("ENTER"):
        if "@gmail.com" in email:
            st.session_state.logged_in = True
            st.rerun()
else:
    st.title("🎵 X-GEN AI MUSIC LAB")
    st.write("OWNER: ANIL BLOGGER | @anil2211k")
    
    prompt = st.text_area("Write song details:")
    duration = st.number_input("Minutes (1-60)", 1, 60, 30)

    if duration > 30 and not st.session_state.premium:
        st.warning("💎 Premium Lock! Contact @anil2211k on Instagram.")
        code_input = st.text_input("Redeem Code", type="password")
        if st.button("ACTIVATE"):
            if code_input in SECRET_CODES:
                st.session_state.premium = True
                st.success("Unlocked!")
                st.rerun()
    else:
        if st.button("🚀 GENERATE"):
            with st.spinner("Processing..."):
                time.sleep(3)
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

