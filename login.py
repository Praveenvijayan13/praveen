import streamlit as st

st.set_page_config(
    page_title="AI Auto Spare Parts PLM",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# SESSION
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# -----------------------------
# USERS
# -----------------------------
USERS = {
    "admin": {
        "password": "admin123",
        "name": "Administrator",
        "role": "Administrator"
    },

    "dhanesh": {
        "password": "guide123",
        "name": "Mr. Dhanesh Babu",
        "role": "Project Guide"
    },

    "suresh": {
        "password": "guide456",
        "name": "Dr. Suresh",
        "role": "Faculty Guide"
    },

    "praveen": {
        "password": "240074",
        "name": "Praveen.V (24ME0074)",
        "role": "Student"
    },

    "praveenraj": {
        "password": "240073",
        "name": "Praveen Raj.R (24ME0073)",
        "role": "Student"
    }
}

# -----------------------------
# IF ALREADY LOGGED IN
# -----------------------------
if st.session_state.logged_in:

    st.sidebar.success(f"👋 Welcome\n\n{st.session_state.username}")
    st.sidebar.info(st.session_state.role)

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""

        st.rerun()

    st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

    st.success(f"Welcome, {st.session_state.username}")

    st.write("You have successfully logged into the PLM System.")

    st.subheader("Project Guide")
    st.write("Mr. Dhanesh Babu")

    st.subheader("Faculty Guide")
    st.write("Dr. Suresh")

    st.subheader("Developed By")

    st.write("Praveen.V (24ME0074)")
    st.write("Praveen Raj.R (24ME0073)")

    st.divider()

    st.info("Open Dashboard from the left sidebar.")

    st.stop()

# -----------------------------
# LOGIN PAGE
# -----------------------------
st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.subheader("Login Portal")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login", use_container_width=True):

    if username in USERS:

        if USERS[username]["password"] == password:

            st.session_state.logged_in = True
            st.session_state.username = USERS[username]["name"]
            st.session_state.role = USERS[username]["role"]

            st.success("Login Successful")

            st.switch_page("pages/1_Dashboard.py")

        else:
            st.error("Incorrect Password")

    else:
        st.error("Invalid Username")

st.divider()

st.markdown(
"""
### Login Credentials

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Administrator |
| dhanesh | guide123 | Project Guide |
| suresh | guide456 | Faculty Guide |
| praveen | 240074 | Student |
| praveenraj | 240073 | Student |

---

### Project Guide

**Mr. Dhanesh Babu**

### Faculty Guide

**Dr. Suresh**

### Developed By

- Praveen.V (24ME0074)

- Praveen Raj.R (24ME0073)

Department of Mechanical Engineering

Chennai Institute of Technology
"""
)