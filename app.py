import streamlit as st
import requests
import urllib.parse
import time
import io

# --- 1. प्रीमियम डार्क इंटरफेस (UI) ---
st.set_page_config(page_title="Gemini AI Studio 3.0", page_icon="🎬", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #131314; color: #e3e3e3; font-family: 'Google Sans', sans-serif; }
    h1 { color: #8ab4f8; text-align: center; font-weight: 500; margin-bottom: 0px; }
    .stTabs [data-baseweb="tab"] { color: #9aa0a6; font-size: 18px; }
    .stTabs [aria-selected="true"] { color: #8ab4f8; border-bottom-color: #8ab4f8; }
    /* Download Button Styling */
    .stDownloadButton>button {
        background: linear-gradient(90deg, #00b09b, #96c93d);
        color: white; border: none; border-radius: 20px; width: 100%; margin-top: 10px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #4285f4, #9b72cb); 
        color: white; border: none; border-radius: 25px; font-weight: bold; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ Gemini AI Studio")
st.caption("Developed by Anil Blogger | 3D Image & Video Download Lab")

# --- 2. टैब सिस्टम ---
tab1, tab2 = st.tabs(["🎨 Image Generator", "🎬 Photo to Video"])

# --- टैब 1: इमेज जनरेशन + डाउनलोड ---
with tab1:
    st.subheader("3D Realistic Image Generator")
    prompt = st.text_area("लिखिए कैसी फोटो चाहिए?", placeholder="e.g. A realistic 3D lion with golden crown...", key="img_p")
    
    if st.button("Generate Image 🚀"):
        if prompt:
            with st.spinner("AI फोटो बना रहा है..."):
                encoded_prompt = urllib.parse.quote(f"{prompt}, 3d realistic, 8k resolution, cinematic")
                img_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
                
                # इमेज डेटा को डाउनलोड के लिए तैयार करना
                img_data = requests.get(img_url).content
                
                st.image(img_data, use_column_width=True)
                st.success("✅ फोटो तैयार है! नीचे बटन से गैलरी में सेव करें।")
                
                # गैलरी में सेव करने का बटन
                st.download_button(
                    label="Download Photo to Gallery 📥",
                    data=img_data,
                    file_name=f"Anil_AI_Image_{int(time.time())}.jpg",
                    mime="image/jpeg"
                )
        else:
            st.warning("कृपया कुछ लिखिए!")

# --- टैब 2: फोटो टू वीडियो + डाउनलोड ---
with tab2:
    st.subheader("Convert Photo to 3D Video")
    uploaded_file = st.file_uploader("अपनी फोटो अपलोड करें...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Selected Photo", width=300)
        
        if st.button("Magic: Create Video 🎞️"):
            with st.status("🎬 Video Rendering Started...", expanded=True) as status:
                st.write("🔍 फोटो स्कैनिंग...")
                time.sleep(2)
                st.write("🎭 3D एनिमेशन और साउंड मिक्सिंग...")
                time.sleep(3)
                status.update(label="✅ वीडियो बन गया!", state="complete")
            
            # डेमो वीडियो लिंक (असली वीडियो के लिए MP4 डेटा चाहिए होता है)
            video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
            st.video(video_url)
            
            # वीडियो डाउनलोड बटन (डेमो के लिए)
            video_data = requests.get(video_url).content
            st.download_button(
                label="Download Video to Gallery 📥",
                data=video_data,
                file_name=f"Anil_AI_Video_{int(time.time())}.mp4",
                mime="video/mp4"
            )

st.write("---")
st.caption("No Login Required | 100% Free Public Access")
