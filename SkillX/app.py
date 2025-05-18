
import streamlit as st
from auth import signup, login
from database import create_tables
import skills
import contact

# ✅ Page Configuration
st.set_page_config(page_title="SkillSwap 🔄", page_icon="🔄", layout="wide")

# ✅ Create Initial Tables
create_tables()

# ✅ Sidebar with Profile and Navigation
with st.sidebar:
    st.image("SkillX/profile.png", width=100, caption="Aisha Junaid")  # Profile image
    st.markdown("""
        <style>
        [data-testid="stImage"] img {
            border-radius: 50%;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    menu = st.selectbox(
        "🚀 Navigation",
        ["🏠 Home", "📝 Sign Up", "🔐 Login", "🔍 Find a Skill", "💡 Offer a Skill", "📬 Contact Us"]
    )

# ✅ Page Routing

# 🏠 Home Page
if menu == "🏠 Home":
    st.title("🔄 Welcome to **SkillSwap Pakistan**")
    st.subheader("👩‍🎓 Learn & 🧑‍🏫 Teach Skills Effortlessly!")
    st.markdown("""
        ### 🌟 Why Use SkillSwap?
        - 🎯 **Find Experts**: Learn from skilled professionals.
        - 💡 **Offer a Skill**: Teach and earn money or barter.
        - 🔐 **Secure & Simple**: Easy login/signup with encrypted passwords.
    """)
    st.success("Join today and start swapping skills with confidence! 🚀")

# 📝 Sign Up
elif menu == "📝 Sign Up":
    signup()

# 🔐 Login
elif menu == "🔐 Login":
    user = login()
    if user:
        st.session_state['user_id'] = user['email']
        st.session_state['user_name'] = user['name']
        st.success(f"Hello, {user['name']}! You're logged in.")

# 🔍 Find Skill
elif menu == "🔍 Find a Skill":
    if 'user_id' in st.session_state:
        skills.find_skill()
    else:
        st.warning("Please log in to find skills.")

# 💡 Offer a Skill
elif menu == "💡 Offer a Skill":
    if 'user_id' in st.session_state:
        skills.list_skill(st.session_state['user_id'])
    else:
        st.warning("Please log in to offer your skills.")

# 📬 Contact Us
elif menu == "📬 Contact Us":
    contact.contact_page()

# ✅ Footer
st.markdown("---")
st.markdown("🏆 **SkillSwap Pakistan** – Made with ❤️ by **Aisha Junaid**")
