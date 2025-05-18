import streamlit as st
from database import conn, c

def list_skill(user_id):
    st.title("💡 Offer Your Skill")

    # Form input
    skill = st.text_input("📖 What skill are you offering?")
    price = st.slider("💰 Set your price (or barter for free)", 0, 100)
    barter = st.checkbox("🔄 Barter instead of payment?")

    # Submit button
    if st.button("📢 List Skill"):
        if skill.strip() == "":
            st.error("Please enter a skill name.")
            return

        barter_val = 1 if barter else 0

        # Insert into database
        c.execute(
            "INSERT INTO skills (user_id, skill_name, price, barter) VALUES (?, ?, ?, ?)",
            (user_id, skill, price, barter_val)
        )
        conn.commit()

        st.success(f"✅ {skill} listed successfully! Someone will reach out soon.")

        # Prevent infinite loop and refresh page
        st.stop()
        st.experimental_rerun()


def find_skill():
    st.title("🎯 Find a Skill to Learn")

    # LEFT JOIN so we still see skills even if user is missing
    c.execute("""
        SELECT 
            skills.skill_name, 
            skills.price, 
            skills.barter, 
            COALESCE(users.username, 'Unknown') 
        FROM skills 
        LEFT JOIN users ON skills.user_id = users.id
    """)
    skills = c.fetchall()

    # Debug info – can be removed later
    with st.expander("🛠 Debug: Show Raw Table Data"):
        c.execute("SELECT * FROM skills")
        st.write("Skills Table:", c.fetchall())

        c.execute("SELECT * FROM users")
        st.write("Users Table:", c.fetchall())

    # Show results
    if not skills:
        st.info("No skills listed yet.")
        return

    for skill_name, price, barter, username in skills:
        price_text = "Barter" if barter else f"₹{price}"
        st.markdown(f"**{skill_name}** by *{username}* — Price: {price_text}")
