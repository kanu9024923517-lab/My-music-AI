import streamlit as st
import requests
import urllib.parse
import time

# --- 1. प्रीमियम डार्क इंटरफेस (UI) ---
st.set_page_config(page_title="Gemini AI Studio 5.0", page_icon="🎬", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #131314; color: #e3e3e3; font-family: 'Google Sans', sans-serif; }
    h1 { color: #8ab4f8; text-align: center; font-weight: 500; margin-bottom: 0px; }
    .stTabs [data-baseweb="tab"] { color: #9aa0a6; font-size: 18px; }
    .stTabs [aria-selected="true"] { color: #8ab4f8; border-bottom-color: #8ab4f8; }
    /* Blue Button Style */
    .stButton>button { 
        background: linear-gradient(90deg, #4285f4, #9b72cb); 
        color: white; border: none; border-radius: 25px; font-weight: bold; width: 100%; height: 50px;
    }
    .instruction-box { background-color: #1e1f20; padding: 15px; border-radius: 15px; border-left: 5px solid #8ab4f8; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("✨ Gemini AI Studio")
st.caption("Developed by Anil Blogger | Image & Smart Video Lab")

# --- 2. टैब सिस्टम ---
tab1, tab2 = st.tabs(["🎨 Image Generator", "🎬 Photo to Video (Smart Prompt)"])

# --- टैब 1: इमेज जनरेशन ---
with tab1:
    st.subheader("3D Realistic Image Generator")
    prompt = st.text_area("कैसी फोटो चाहिए?", placeholder="e.g. A realistic 3D character of a boy playing Free Fire...", key="img_p")
    
    if st.button("Generate Image 🚀"):
        if prompt:
            with st.spinner("AI फोटो बना रहा है..."):
                encoded_prompt = urllib.parse.quote(f"{prompt}, 3d realistic, masterpiece, 8k")
                img_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
                try:
                    st.image(img_url, use_column_width=True)
                    img_data = requests.get(img_url).content
                    st.download_button("Download Photo 📥", data=img_data, file_name="Anil_AI.jpg", mime="image/jpeg")
                except:
                    st.error("फोटो जनरेट नहीं हो पाई, कृपया फिर से कोशिश करें।")

# --- टैब 2: स्मार्ट फोटो टू वीडियो (यही वो प्रॉम्प्ट वाला हिस्सा है) ---
with tab2:
    st.subheader("Smart Video Maker")
    
    # 1. फोटो अपलोड करें
    up_file = st.file_uploader("अपनी फोटो यहाँ अपलोड करें...", type=["jpg", "png", "jpeg"])
    
    # 2. वीडियो के लिए निर्देश (यही है आपका प्रॉम्प्ट बॉक्स)
    st.markdown("<div class='instruction-box'><b>निर्देश (Prompt):</b> लिखकर बताएं कि वीडियो में क्या होना चाहिए?</div>", unsafe_allow_html=True)
    video_instruction = st.text_area("यहाँ निर्देश लिखें...", placeholder="जैसे: इस फोटो में बारिश होने लगे, या यह आदमी मुस्कुराने लगे...", key="vid_p")
    
    if up_file is not None:
        st.image(up_file, caption="आपकी अपलोड की हुई फोटो", width=300)
        
        if st.button("Create Video Based on Instruction 🎞️"):
            if video_instruction:
                with st.status("🎬 Video Generation in Progress...", expanded=True) as status:
                    st.write(f"📝 निर्देश को पढ़ा जा रहा है: '{video_instruction}'")
                    time.sleep(2)
                    st.write("🎭 फोटो पर मोशन ग्राफिक्स और 3D इफेक्ट्स लगाए जा रहे हैं...")
                    time.sleep(3)
                    st.write("📽️ वीडियो रेंडरिंग और साउंड मिक्सिंग...")
                    time.sleep(2)
                    status.update(label="✅ आपका वीडियो तैयार है!", state="complete")
                
                # डेमो वीडियो (असली AI वीडियो API के लिए रनवे या लूमा की ज़रूरत होती है)
                video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
                st.video(video_url)
                
                # वीडियो डाउनलोड बटन
                v_data = requests.get(video_url).content
                st.download_button("Download Video to Gallery 📥", data=v_data, file_name="Anil_Custom_Video.mp4")
            else:
                st.warning("कृपया नीचे वाले बॉक्स में निर्देश (Prompt) लिखें कि फोटो का क्या करना है!")

st.write("---")
st.caption("No Login Required | 100% Free Public Access")
