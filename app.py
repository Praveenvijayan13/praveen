import streamlit as st

st.set_page_config(
    page_title="AI Auto Spare Parts PLM",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# Login Check
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 Login Required")
    st.warning("Please login first.")
    st.page_link("login.py", label="🔑 Open Login Page")
    st.stop()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.success(f"👋 Welcome\n\n{st.session_state.username}")
st.sidebar.info(st.session_state.role)

if st.sidebar.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("login.py")

# -----------------------------
# Dashboard
# -----------------------------
st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.success(f"Welcome {st.session_state.username}")

st.info(f"Role : {st.session_state.role}")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Spare Parts", 125)

with col2:
    st.metric("Suppliers", 18)

st.divider()

st.subheader("Main Modules")

modules = [
    "📦 Spare Parts",
    "🏭 Manufacturing",
    "📋 Inventory",
    "🚚 Suppliers",
    "🔧 Service History",
    "🤖 AI Prediction",
    "📊 Analytics",
    "♻️ End Of Life",
    "📄 Reports",
    "👥 User Management"
]

for module in modules:
    st.success(module)

st.divider()

st.success("PLM System Running Successfully ✅")