import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="AI Prediction", page_icon="🤖")

st.title("🤖 AI Spare Parts Demand Prediction")

# Database Connection
conn = sqlite3.connect("database/spareparts.db")

df = pd.read_sql_query(
    "SELECT part_id, part_name, stock FROM spareparts",
    conn
)

if df.empty:

    st.warning("No Spare Parts Available")

else:

    st.subheader("Select Spare Part")

    selected = st.selectbox(
        "Part",
        df["part_name"]
    )

    row = df[df["part_name"] == selected].iloc[0]

    st.write("Part ID :", row["part_id"])

    st.write("Current Stock :", row["stock"])

    monthly_sales = st.number_input(
        "Average Monthly Sales",
        min_value=1,
        value=20
    )

    predicted = monthly_sales * 3

    st.divider()

    st.subheader("Prediction")

    st.metric(
        "Predicted Demand (Next 3 Months)",
        predicted
    )

    if row["stock"] < predicted:

        st.error("⚠ Reorder Required")

        st.write(
            "Suggested Order Quantity :",
            predicted - row["stock"]
        )

    else:

        st.success("✅ Current Stock is Enough")

conn.close()