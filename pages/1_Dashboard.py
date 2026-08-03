import streamlit as st

# -----------------------------
# LOGIN CHECK
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.switch_page("login.py")
    st.stop()

# -----------------------------
# DASHBOARD
# -----------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

st.success(f"Welcome {st.session_state.user_name}")

st.info(f"Role : {st.session_state.role}")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Spare Parts", 120)

with col2:
    st.metric("Suppliers", 18)

with col3:
    st.metric("Inventory Items", 350)

st.divider()

st.subheader("Project Modules")

st.success("📦 Spare Parts")

st.success("🏭 Manufacturing")

st.success("📋 Inventory")

st.success("🚚 Suppliers")

st.success("🔧 Service History")

st.success("🤖 AI Prediction")

st.success("📈 Analytics")

st.success("♻️ End Of Life")

st.success("📄 Reports")

st.success("👥 User Management")

st.divider()

if st.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.user_name = ""
    st.session_state.role = ""

    st.switch_page("login.py")