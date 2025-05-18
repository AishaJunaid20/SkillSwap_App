import streamlit as st
import bcrypt
import json
import os

# ========== USER CLASS ==========
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email.lower()
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def to_dict(self):
        return {"name": self.name, "email": self.email, "password": self.password}

# ========== AUTH MANAGER ==========
class AuthManager:
    def __init__(self, db_path="users.json"):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                json.dump([], f)

    def load_users(self):
        with open(self.db_path, "r") as f:
            return json.load(f)

    def save_user(self, user: User):
        users = self.load_users()
        for u in users:
            if u["email"] == user.email:
                return False  # Duplicate email
        users.append(user.to_dict())
        with open(self.db_path, "w") as f:
            json.dump(users, f, indent=2)
        return True

    def get_user_by_email(self, email):
        users = self.load_users()
        for user in users:
            if user["email"] == email.lower():
                return user
        return None

# ========== SIGNUP FUNCTION ==========
def signup():
    st.subheader("Create an Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if not name or not email or not password:
            st.warning("Please fill all fields.")
            return

        user = User(name, email, password)
        auth = AuthManager()

        if auth.save_user(user):
            st.success("Signup successful! You can now log in.")
        else:
            st.error("Email already exists. Try logging in.")

# ========== LOGIN FUNCTION ==========
def login():
    st.subheader("Login to SkillSwap")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        auth = AuthManager()
        user = auth.get_user_by_email(email)

        if user:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                st.success(f"Welcome back, {user['name']}! 🎉")
                return user  # Return user info
            else:
                st.error("Incorrect password.")
        else:
            st.error("User not found. Please sign up.")
