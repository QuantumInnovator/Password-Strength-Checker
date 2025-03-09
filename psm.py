import re
import streamlit as st

# Page styling
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔒", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {text-align: center;} 
.stTextInput {width: 60% !important; margin: auto;}
.stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
.stButton button:hover{background-color: #45a049;}            
</style>
""", unsafe_allow_html=True)

# Title
st.title("🔐 Password Strength Meter")
st.write("📝 Enter your password to check its strength 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0 
    feedback = []

    if len(password) >= 8:
        score += 1  # Increased score by 1
    else:
        feedback.append("⚠️ Password should be at least **8 characters** long")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔡 Password should contain both **uppercase and lowercase** letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔢 Password should contain at least **one digit**")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("🔣 Password should contain at least **one special character** (e.g., !@#)")

    # Display password strength
    if score == 4:
        st.success("✅ **Strong Password!** 🔥 Your password is secure! 🔒")
    elif score == 3:
        st.warning("⚠️ **Medium Strength!** Try adding more complexity! 🚀")
    else:
        st.error("❌ **Weak Password!** Consider making it stronger! 😟")

    # Feedback section
    if feedback: 
        with st.expander("💡 **Password Tips** 📌"): 
            for item in feedback:
                st.write(item)

# Input field
password = st.text_input("🔑 Enter your password", type="password", help="🛡️ Make sure your password is strong!")

# Button working
if st.button("🔍 Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password before checking!")
