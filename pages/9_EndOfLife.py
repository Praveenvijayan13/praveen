import streamlit as st
import pandas as pd

st.title("♻️ End Of Life Management")

st.subheader("Dispose / Recycle Spare Parts")

part_id = st.text_input("Part ID")

part_name = st.text_input("Part Name")

quantity = st.number_input(
    "Quantity",
    min_value=1
)

method = st.selectbox(
    "Disposal Method",
    [
        "Recycle",
        "Scrap",
        "Reuse"
    ]
)

date = st.date_input("Disposal Date")

if st.button("Save Record"):

    df = pd.DataFrame({
        "Part ID":[part_id],
        "Part Name":[part_name],
        "Quantity":[quantity],
        "Method":[method],
        "Date":[date]
    })

    st.success("✅ End Of Life Record Saved Successfully")

    st.subheader("End Of Life Records")

    st.dataframe(df, use_container_width=True)