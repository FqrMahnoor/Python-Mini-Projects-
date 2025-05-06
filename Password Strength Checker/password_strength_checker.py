import re
import streamlit as st
import string
import random

# Streamlit page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑", layout="centered")
st.title("🔐 Password Strength Checker")

# Password input field
password = st.text_input("Enter your password", type="password")

# Password strength checker function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Password generator function
def password_generator():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*"
    all_chars = letters + digits + symbols
    return ''.join(random.choice(all_chars) for _ in range(8))

# Blacklist of common passwords
blacklist = ["admin","password123", "12345678", "pass1234", "admin1234","abc123","qwerty","123123","helloworld"]

# When user clicks "Submit" button
if st.button("Submit"):
    if not password:
        st.error("❌ Please enter a password before submitting.")
    
    else:
        score, feedback = check_password_strength(password)

    # Case-insensitive blacklist check
        if password.lower() in   blacklist:
            st.error("Password is too common!")
            st.info(f"Try this strong password: `{password_generator()}`")

        else:
        # Display feedback for password strength
            for f in feedback:
                st.error(f)
    
    # Display password strength status
            if score == 4:
                st.success("✅ Strong Password!")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions above.")
                st.info(f"Try this strong password: `{password_generator()}`")

    
    