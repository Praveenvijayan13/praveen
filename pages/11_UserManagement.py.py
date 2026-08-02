import streamlit as st
import pandas as pd

st.title("👥 User Management")

st.subheader("Add New User")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

role = st.selectbox(
    "Role",
    [
        "Admin",
        "Manager",
        "Employee"
    ]
)

if st.button("Create User"):

    df = pd.DataFrame({
        "Username":[username],
        "Role":[role]
    })

    st.success("✅ User Created Successfully")

    st.subheader("Current Users")

    st.dataframe(df, use_container_width=True, hide_index=True)