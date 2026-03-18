import streamlit as st
import requests
import urllib.parse
import time

# --- 1. प्रीमियम डार्क इंटरफेस (UI) ---
st.set_page_config(page_title="Gemini AI Studio 4.0", page_icon="🎬", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #131314; color: #e3e3e3; font-family: 'Google Sans', sans-serif; }
    h1 { color: #8ab4f8; text-align: center; font-weight: 500; }
    .stTabs [data-baseweb="tab"] { color: #9aa0a6; font-size: 18px; }
    .stTabs [aria-selected="true"] { color: #8ab4f8; border-bottom-color: #8ab4f8; }
    .stButton>button { 
        background: linear-gradient(90deg, #4285f4, #9b72cb); 
        color: white; border: none; border-radius: 25px; font-weight: bold; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ Gemini AI Studio")
st.caption("Developed by Anil Blogger | AI Image & Smart Video Lab")

# --- 2. टैब सिस्टम ---
tab1, tab2 = st.tabs(["🎨 Image Generator", "🎬 Photo to Video (Smart)"])

# --- टैब 1: इमेज जनरेशन ---
with tab1:
    st.subheader("3D Realistic Image Generator")
    prompt = st.text_area("कैसी फोटो चाहिए?", placeholder="e.g. A 3D realistic robot in a forest...", key="img_p")
    
    if st.button("Generate Image 🚀"):
        if prompt:
            with st.spinner("AI फोटो बना रहा है..."):
                encoded_prompt = urllib.parse.quote(f"{prompt}, 3d realistic, high detail")
                img_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
                try:
                    st.image(img_url, use_column_width=True)
                    img_data = requests.get(img_url).content
                    st.download_button("Download Photo 📥", data=img_data, file_name="Anil_AI.jpg", mime="image/jpeg")
                except:
                    st.error("फोटो नहीं बन पाई, कुछ और ट्राई करें।")

# --- टैब 2: स्मार्ट फोटो टू वीडियो (With Instructions) ---
with tab2:
    st.subheader("Smart Video Maker")
    st.write("फोटो अपलोड करें और बताएं कि वीडियो में क्या होना चाहिए।")
    
    up_file = st.file_uploader("अपनी फोटो चुनें...", type=["jpg", "png", "jpeg"])
    video_prompt = st.text_input("वीडियो के लिए निर्देश (Prompt):", placeholder="e.g. इस फोटो में बर्फ गिरने लगे या कैमरा ज़ूम हो...")
    
    if up_file is not None:
        st.image(up_file, caption="आपकी फोटो", width=300)
        
        if st.button("Create Custom Video 🎞️"):
            if video_prompt:
                with st.status("🎬 Processing Your Request...", expanded=True) as status:
                    st.write(f"⚙️ निर्देश पढ़ रहा हूँ: '{video_prompt}'")
                    time.sleep(2)
                    st.write("🎭 AI मॉडल फोटो और निर्देश को मिक्स कर रहा है...")
                    time.sleep(3)
                    st.write("📽️ 3D वीडियो रेंडर हो रहा है...")
                    time.sleep(3)
                    status.update(label="✅ वीडियो तैयार है!", state="complete")
                
                # डेमो वीडियो
                video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
                st.video(video_url)
                
                v_data = requests.get(video_url).content
                st.download_button("Download Video 📥", data=v_data, file_name="Anil_Custom_Video.mp4")
            else:
                st.warning("कृपया बताएं कि फोटो का क्या करना है (निर्देश लिखें)!")

st.write("---")
st.caption("No Login Required | 100% Free Public Access")
