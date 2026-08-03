import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# USER DATABASE
# -----------------------------

users = {

    "admin": {
        "password": "admin123",
        "name": "System Administrator",
        "role": "Administrator"
    },

    "praveen": {
        "password": "24ME0074",
        "name": "Praveen.V (24ME0074)",
        "role": "Student"
    },

    "praveenraj": {
        "password": "24ME0073",
        "name": "Praveen Raj.R (24ME0073)",
        "role": "Student"
    },

    "suresh": {
        "password": "drsuresh",
        "name": "Dr. Suresh",
        "role": "Project Guide"
    },

    "dhanesh": {
        "password": "dhanesh123",
        "name": "Mr. Dhanesh Babu",
        "role": "Project Guide"
    }

}

# -----------------------------
# INITIALIZE SESSION
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# -----------------------------
# IF ALREADY LOGGED IN
# -----------------------------

if st.session_state.logged_in:

    st.success(f"Welcome {st.session_state.user_name}")

    if st.button("Go to Dashboard"):
        st.switch_page("app.py")

    st.stop()

# -----------------------------
# LOGIN PAGE
# -----------------------------

st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.markdown("## 🔐 Login Portal")

st.markdown("---")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username in users:

        if password == users[username]["password"]:

            st.session_state.logged_in = True

            st.session_state.user_name = users[username]["name"]

            st.session_state.role = users[username]["role"]

            st.success("✅ Login Successful")

            st.balloons()

            st.switch_page("app.py")

        else:

            st.error("❌ Incorrect Password")

    else:

        st.error("❌ Username Not Found")

st.markdown("---")

st.markdown("### Login Accounts")

st.info("""
Administrator
Username : admin
Password : admin123
""")

st.info("""
Student
Username : praveen
Password : 24ME0074
""")

st.info("""
Student
Username : praveenraj
Password : 24ME0073
""")

st.info("""
Project Guide
Username : suresh
Password : drsuresh
""")

st.info("""
Project Guide
Username : dhanesh
Password : dhanesh123
""")

st.markdown("---")

st.caption("AI Auto Spare Parts Lifecycle Management System")