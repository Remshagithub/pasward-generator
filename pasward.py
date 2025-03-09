import re
import streamlit as st
# page styling
st.set_page_config(page_title="Password Checker by Rimsha", page_icon="🔒", layout="centered")
# custom css
st.markdown(
    """
    <style>
    .main {text-align: center;}
    .stTextInput {width: 50%; !important;margin: 0 auto;}
    .stButton button {width: 50%; background-color: #f63366; color: white; font-size: 20px;}
     .stButton button:hover {background-color: #f63366;}
    </style>""", unsafe_allow_html=True)
# page title
st.title("Password generator")
st.write("Enter your password to check its strength")
#  function to check password sterength
def check_password_strength(password):
    score = 0
    feedback = []
    if len(password) > 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain both upper and lower case characters")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit(0-9)")
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character (!@#$%^&*)")
        #  display password strength
    if score == 4:
        st.success("Password is strong")
    elif score == 3:
        st.info("Password is medium")
    else:
        st.error("week password❌")
        #  feedback
        if feedback:
            with st.expander("improve your password"):
                for item in feedback:
                    st.write(item)
                    password = st.text_input("Enter your password", type="password",help="Enter your strong password")

                    #button working
                    if st.button("Check strength"):
                        if password:
                            check_password_strength(password)
                        else:
                            st.warning("Please enter your password")