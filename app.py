import streamlit as st

st.set_page_config(
    page_title="AI Auto Spare Parts PLM",
    page_icon="🚗",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("🚗 AI Auto Spare Parts PLM")

st.sidebar.markdown("---")

st.sidebar.subheader("🏫 Institution")
st.sidebar.write("Chennai Institute of Technology")

st.sidebar.subheader("📚 Department")
st.sidebar.write("Mechanical Engineering")

st.sidebar.subheader("👨‍🎓 Project Team")

st.sidebar.write("""
Praveen.V (24ME0074)

Praveen raj.R (24ME0073)
""")

st.sidebar.subheader("🎓 Academic Year")
st.sidebar.write("2026 - 2027")

st.sidebar.markdown("---")

st.sidebar.success("Welcome to the PLM System")

# ---------------- Main Page ----------------

st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.markdown("---")

st.header("📌 Project Objective")

st.write("""
The AI Auto Spare Parts Lifecycle Management System helps manage
automobile spare parts from manufacturing to end-of-life using
Product Lifecycle Management (PLM) concepts.
""")

st.markdown("---")

st.header("✨ Main Modules")

col1, col2 = st.columns(2)

with col1:
    st.success("📦 Spare Parts")
    st.success("🏭 Manufacturing")
    st.success("📋 Inventory")
    st.success("🚚 Suppliers")
    st.success("🔧 Service History")
    st.success("🤖 AI Prediction")

with col2:
    st.success("📊 Analytics")
    st.success("♻️ End Of Life")
    st.success("📄 Reports")
    st.success("👥 User Management")
    st.success("ℹ️ About")

st.markdown("---")

st.header("🛠 Technologies Used")

st.write("""
• Python

• Streamlit

• SQLite

• Pandas

• ReportLab
""")

st.markdown("---")

st.info("👈 Use the left sidebar to open the project modules.")

st.success("✅ AI Auto Spare Parts Lifecycle Management System Ready")