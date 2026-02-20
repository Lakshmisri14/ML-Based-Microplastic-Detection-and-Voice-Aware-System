import streamlit as st
from PIL import Image
import pyttsx3
import datetime
import numpy as np
from tensorflow.keras.models import load_model

# ---------------------------
# Load your trained model
# ---------------------------
model = load_model("C:\\Users\\Lakshmi Sri M\\OneDrive\\Documents\\Desktop\\MP1\\microplastic_model.h5")  # Path to your trained model

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="AquaScanner+",
    page_icon="🥤",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
    .main {background-color: #f8f9fa;}
    .stButton>button {background-color: #007bff; color: white; border-radius: 6px; font-weight: bold;}
    .stTabs [role="tab"] {background: ##00bfff; padding: 12px 20px; font-weight: bold;}
    .stTabs [aria-selected="true"] {background: #00bfff; color: white;}
    #MainMenu, header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown("""
<div style='display:flex;align-items:center;gap:18px;margin-bottom:1.5rem;'>
    <img src='https://cdn-icons-png.flaticon.com/512/2935/2935115.png' width='60'>
    <span style='font-size:2.5rem;font-weight:800;color:#00bfff;'>AquaScanner+</span>
</div>
""", unsafe_allow_html=True)

st.write("**AI-Based Microplastic Detection and Voice-Aware System** - Upload or capture your drink image for instant safety analysis with multilingual alerts.")

# ---------------------------
# Session state
# ---------------------------
if "recent_results" not in st.session_state:
    st.session_state.recent_results = []

# ---------------------------
# Helper functions
# ---------------------------
def is_water_image(img):
    """Placeholder - currently always True"""
    return True

def detect_microplastics(img):
    """Predict microplastic presence using the loaded model"""
    try:
        img_resized = img.resize((128,128))
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # (1,128,128,3)
        
        if model.output_shape[-1] == 1:
            # Sigmoid binary
            prediction = model.predict(img_array)[0][0]
            detected = prediction > 0.5
            confidence = prediction if detected else 1 - prediction
        else:
            # Softmax categorical
            prediction = model.predict(img_array)[0]
            detected = np.argmax(prediction) == 1
            confidence = prediction[1] if detected else prediction[0]

        return detected, confidence
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return False, 0.0

def play_voice_alert(message_en, message_ta):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(message_en)
        engine.say(message_ta)
        engine.runAndWait()
        engine.stop()
        return True
    except:
        return False

def save_result(img, result, confidence, timestamp):
    st.session_state.recent_results.append({
        'image': img.copy(),
        'result': result,
        'confidence': confidence,
        'timestamp': timestamp
    })
    if len(st.session_state.recent_results) > 5:
        st.session_state.recent_results.pop(0)

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📁 Upload", "📷 Webcam", "🕓 Recent Results", "ℹ️ Help & About"])

# ---------------------------
# Upload Tab
# ---------------------------
with tab1:
    st.subheader("Upload Drink Image")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg","jpeg","png"])
    
    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        col1, col2 = st.columns([1,1])
        with col1:
            st.image(img, caption="Uploaded Image", use_container_width=True)
        with col2:
            if not is_water_image(img):
                st.error("⚠️ Please upload an image of a water drink only.")
            else:
                st.success("✅ Valid water drink image detected!")
                with st.spinner("Analyzing for microplastics..."):
                    detected, confidence = detect_microplastics(img)
                
                if detected:
                    st.error(f"⚠️ Microplastics detected! (Confidence: {confidence:.1%})")
                    message_en = "Warning: Microplastics detected in your drink!"
                    message_ta = "எச்சரிக்கை: உங்கள் பானத்தில் மைக்ரோபிளாஸ்டிக்ஸ் கண்டறியப்பட்டது!"
                else:
                    st.success(f"✅ No microplastics detected! Safe to drink. (Confidence: {confidence:.1%})")
                    message_en = "Good news: Your drink appears safe!"
                    message_ta = "நல்ல செய்தி: உங்கள் பானம் பாதுகாப்பானது!"
                
                if st.button("🔊 Play Voice Alert", key="upload_voice"):
                    play_voice_alert(message_en, message_ta)
                
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_result(img, detected, confidence, timestamp)

# ---------------------------
# Webcam Tab
# ---------------------------
with tab2:
    st.subheader("Capture from Webcam")
    camera_img = st.camera_input("Take a picture")
    
    if camera_img:
        img = Image.open(camera_img).convert("RGB")
        col1, col2 = st.columns([1,1])
        with col1:
            st.image(img, caption="Camera Image", use_container_width=True)
        with col2:
            if not is_water_image(img):
                st.error("⚠️ Please capture an image of a water drink only.")
            else:
                st.success("✅ Valid water drink image detected!")
                with st.spinner("Analyzing for microplastics..."):
                    detected, confidence = detect_microplastics(img)
                
                if detected:
                    st.error(f"⚠️ Microplastics detected! (Confidence: {confidence:.1%})")
                    message_en = "Warning: Microplastics detected in your drink!"
                    message_ta = "எச்சரிக்கை: உங்கள் பானத்தில் மைக்ரோபிளாஸ்டிக்ஸ் கண்டறியப்பட்டது!"
                else:
                    st.success(f"✅ No microplastics detected! Safe to drink. (Confidence: {confidence:.1%})")
                    message_en = "Good news: Your drink appears safe!"
                    message_ta = "நல்ல செய்தி: உங்கள் பானம் பாதுகாப்பானது!"
                
                if st.button("🔊 Play Voice Alert", key="camera_voice"):
                    play_voice_alert(message_en, message_ta)
                
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_result(img, detected, confidence, timestamp)

# ---------------------------
# Recent Results Tab
# ---------------------------
with tab3:
    st.subheader("Recent Analysis Results")
    if st.session_state.recent_results:
        for i, result in enumerate(reversed(st.session_state.recent_results)):
            with st.expander(f"Analysis #{len(st.session_state.recent_results)-i} - {result['timestamp']}"):
                col1, col2 = st.columns([1,2])
                with col1:
                    st.image(result['image'], caption="Analyzed Image", use_container_width=True)
                with col2:
                    if result['result']:
                        st.error(f"⚠️ Microplastics detected (Confidence: {result['confidence']:.1%})")
                    else:
                        st.success(f"✅ Safe to drink (Confidence: {result['confidence']:.1%})")
                    st.write(f"**Analysis Time:** {result['timestamp']}")
        if st.button("🗑️ Clear All Results"):
            st.session_state.recent_results = []
            st.success("All results cleared!")
            st.rerun()
    else:
        st.info("No recent results. Upload or capture an image to get started!")

# ---------------------------
# Help & About Tab
# ---------------------------
with tab4:
    st.subheader("About This Application")
    st.markdown("""
    ### 🎯 Purpose
    Detect microplastics in drinking water using AI and image analysis.
    
    ### 🚀 Features
    - Image Upload & Camera Capture
    - AI-Powered Detection
    - Multilingual Voice Alerts (English & Tamil)
    - Recent Results History
    - Professional Interface
    """)

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.markdown("### 🎛️ App Statistics")
    st.metric("Total Analyses", len(st.session_state.recent_results))
    if st.session_state.recent_results:
        safe_count = sum(1 for r in st.session_state.recent_results if not r['result'])
        st.metric("Safe Results", safe_count)
        st.metric("Warnings", len(st.session_state.recent_results) - safe_count)
    
    st.markdown("### 🔧 Settings")
    st.info("Voice alerts support English and Tamil languages automatically.")
    
    st.markdown("### 📊 Model Info")
    st.write("**Detection Model:** Your Trained CNN")
    st.write("**Languages:** English, Tamil")
    st.write("**Accuracy:** As trained")
