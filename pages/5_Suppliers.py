import streamlit as st
import pandas as pd

st.title("🚚 Suppliers Management")

st.subheader("➕ Add Supplier")

supplier_id = st.text_input("Supplier ID")
supplier_name = st.text_input("Supplier Name")
company = st.text_input("Company")
phone = st.text_input("Phone Number")
email = st.text_input("Email")

if st.button("Save Supplier"):

    df = pd.DataFrame({
        "Supplier ID":[supplier_id],
        "Supplier Name":[supplier_name],
        "Company":[company],
        "Phone":[phone],
        "Email":[email]
    })

    st.success("✅ Supplier Saved Successfully")

    st.subheader("Supplier Details")

    st.dataframe(df, use_container_width=True)