import streamlit as st
from database import conn, c  # make sure your database connection is here

def contact_page():
    st.title("📬 Contact Us")

    name = st.text_input("👤 Your Name")
    email = st.text_input("📧 Your Email")
    message = st.text_area("✍️ Your Message")

    if st.button("📨 Send Message"):
        if not name.strip() or not email.strip() or not message.strip():
            st.error("Please fill all fields.")
        else:
            c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                      (name.strip(), email.strip(), message.strip()))
            conn.commit()
            st.success("✅ Message sent successfully.")
