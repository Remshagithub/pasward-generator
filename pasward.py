import random
import string
import streamlit as st

# Page Config
st.set_page_config(page_title="🔐 Password Generator", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .stButton button {
        width: 60%; background-color: #4CAF50; color: white; 
        font-size: 18px; border-radius: 8px;
    }
    .stButton button:hover {background-color: #45a049;}
    .stTextInput {width: 60%; margin: auto;}
    </style>
    """, unsafe_allow_html=True)

# Page Title
st.title("🔐 Secure Password Generator")
st.write("Generate a strong password with a mix of letters, numbers, and symbols.")

# Password Generator Function
def generate_password(length=12):
    if length < 8:
        st.warning("⚠ Password should be at least *8 characters* for better security.")
        return ""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# User Input for Password Length
length = st.slider("🔢 Select password length:", min_value=8, max_value=32, value=12)

# Generate Button
if st.button("🔄 Generate Password"):
    new_password = generate_password(length)
    if new_password:
        st.success(f"🔑 *Generated Password:* {new_password}")
