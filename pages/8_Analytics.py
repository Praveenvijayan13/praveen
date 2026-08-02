import streamlit as st
import pandas as pd

st.title("📊 Analytics Dashboard")

st.subheader("Business Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Parts", "1540")

with col2:
    st.metric("Inventory", "1230")

with col3:
    st.metric("Suppliers", "48")

with col4:
    st.metric("Monthly Sales", "₹2,45,000")

st.divider()

st.subheader("Monthly Spare Parts Sales")

sales = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[120,150,180,160,200,240]
})

st.line_chart(sales.set_index("Month"))

st.divider()

st.subheader("Category Wise Stock")

stock = pd.DataFrame({
    "Category":["Brake","Engine","Electrical","Body","Suspension"],
    "Stock":[120,90,70,40,60]
})

st.bar_chart(stock.set_index("Category"))

st.success("✅ Analytics Generated Successfully")