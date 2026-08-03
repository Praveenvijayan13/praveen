import streamlit as st

st.set_page_config(
    page_title="AI Auto Spare Parts PLM",
    page_icon="🚗",
    layout="wide"
)

# --------------------------
# LOGIN CHECK
# --------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔒 Login Required")

    st.warning("Please login from the Login page before using the system.")

    st.page_link("login.py", label="🔑 Open Login Page")

    st.stop()

# --------------------------
# DASHBOARD
# --------------------------

st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.success(f"Welcome {st.session_state.user_name}")

st.info(f"Role : {st.session_state.role}")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Spare Parts", 125)

with col2:
    st.metric("Suppliers", 18)

st.divider()

st.subheader("Main Modules")

st.success("📦 Spare Parts")

st.success("🏭 Manufacturing")

st.success("📋 Inventory")

st.success("🚚 Suppliers")

st.success("🔧 Service History")

st.success("🤖 AI Prediction")

st.success("📊 Analytics")

st.success("♻️ End Of Life")

st.success("📄 Reports")

st.success("👥 User Management")

st.divider()

if st.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.user_name = ""
    st.session_state.role = ""

    st.switch_page("login.py")