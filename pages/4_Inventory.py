import streamlit as st
import sqlite3
import pandas as pd

st.title("📦 Inventory Management")

conn = sqlite3.connect("database/spareparts.db")

df = pd.read_sql_query("""
SELECT
part_id,
part_name,
category,
stock
FROM spareparts
""", conn)

st.subheader("Current Inventory")

st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Update Stock")

part = st.selectbox(
    "Select Part",
    df["part_id"]
)

new_stock = st.number_input(
    "New Stock",
    min_value=0
)

if st.button("Update Stock"):

    conn.execute(
        "UPDATE spareparts SET stock=? WHERE part_id=?",
        (new_stock, part)
    )

    conn.commit()

    st.success("✅ Inventory Updated Successfully")

conn.close()