import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# -----------------------------
# Check Login
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("Please login first.")
    st.stop()

# -----------------------------
# Username
# -----------------------------
username = st.session_state.get("username", "Guest")

# -----------------------------
# Logout Button
# -----------------------------
col1, col2 = st.columns([8, 1])

with col2:
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("login.py")

# -----------------------------
# Dashboard
# -----------------------------
st.title("📊 AI Auto Spare Parts PLM Dashboard")

st.success(f"Welcome {username}")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🚗 Spare Parts", "250")

with c2:
    st.metric("🏭 Manufacturing", "45")

with c3:
    st.metric("📦 Inventory", "180")

with c4:
    st.metric("🤖 AI Predictions", "22")

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("Project Information")
    st.write("**Project Name:**")
    st.info("AI Auto Spare Parts Lifecycle Management System")

    st.write("**Guide:**")
    st.success("Mr. Dhanesh Babu")

    st.write("**Version:**")
    st.info("Version 1.0")

with right:
    st.subheader("System Status")
    st.success("Database Connected")
    st.success("Inventory Updated")
    st.success("AI Module Active")
    st.success("Reports Ready")

st.markdown("---")

st.subheader("Modules")

m1, m2, m3 = st.columns(3)

with m1:
    st.info("Spare Parts")
    st.info("Manufacturing")
    st.info("Inventory")

with m2:
    st.info("Suppliers")
    st.info("Service History")
    st.info("Analytics")

with m3:
    st.info("AI Prediction")
    st.info("End Of Life")
    st.info("Reports")

st.markdown("---")

st.success("PLM System Running Successfully")