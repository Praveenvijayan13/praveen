import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="Service History", page_icon="🔧")

st.title("🔧 Service History")

# Database Connection
conn = sqlite3.connect("database/spareparts.db", check_same_thread=False)
cursor = conn.cursor()

# Create Service Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS servicehistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_no TEXT,
    part_id TEXT,
    part_name TEXT,
    quantity INTEGER,
    technician TEXT,
    service_date TEXT
)
""")

conn.commit()

# Add Service Record
st.subheader("➕ Add Service Record")

vehicle_no = st.text_input("Vehicle Number")
part_id = st.text_input("Part ID")
part_name = st.text_input("Part Name")
quantity = st.number_input("Quantity Used", min_value=1, step=1)
technician = st.text_input("Technician Name")
service_date = st.date_input("Service Date", value=date.today())

if st.button("💾 Save Service"):

    cursor.execute("""
    INSERT INTO servicehistory
    (vehicle_no, part_id, part_name, quantity, technician, service_date)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        vehicle_no,
        part_id,
        part_name,
        quantity,
        technician,
        str(service_date)
    ))

    # Reduce inventory stock
    cursor.execute("""
    UPDATE spareparts
    SET stock = stock - ?
    WHERE part_id = ?
    """,
    (
        quantity,
        part_id
    ))

    conn.commit()

    st.success("✅ Service Record Saved")
    st.success("📦 Inventory Updated")

st.divider()

# Display Service Records
st.subheader("📋 Service History")

df = pd.read_sql_query(
    "SELECT * FROM servicehistory",
    conn
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Summary
st.subheader("📊 Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Services", len(df))

with col2:
    if len(df) > 0:
        st.metric("Parts Used", int(df["quantity"].sum()))
    else:
        st.metric("Parts Used", 0)

conn.close()