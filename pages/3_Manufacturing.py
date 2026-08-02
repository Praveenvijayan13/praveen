import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="Manufacturing", page_icon="🏭")

st.title("🏭 Manufacturing Management")

# -------------------------------
# Database Connection
# -------------------------------
conn = sqlite3.connect("database/spareparts.db", check_same_thread=False)
cursor = conn.cursor()

# -------------------------------
# Create Manufacturing Table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS manufacturing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id TEXT,
    part_name TEXT,
    quantity INTEGER,
    mfg_date TEXT
)
""")

conn.commit()

# -------------------------------
# Add Manufacturing Record
# -------------------------------

st.subheader("➕ Add Manufacturing Record")

part_id = st.text_input("Part ID (Example: SP001)")
part_name = st.text_input("Part Name")
quantity = st.number_input("Manufactured Quantity", min_value=1, step=1)
mfg_date = st.date_input("Manufacturing Date", value=date.today())

if st.button("💾 Save Record"):

    if part_id == "" or part_name == "":
        st.warning("Please enter Part ID and Part Name.")

    else:

        # Save Manufacturing Record
        cursor.execute("""
        INSERT INTO manufacturing
        (part_id, part_name, quantity, mfg_date)
        VALUES (?, ?, ?, ?)
        """,
        (
            part_id,
            part_name,
            quantity,
            str(mfg_date)
        ))

        # Check Spare Part Exists
        cursor.execute(
            "SELECT stock FROM spareparts WHERE part_id=?",
            (part_id,)
        )

        result = cursor.fetchone()

        if result:

            # Update Stock
            cursor.execute("""
            UPDATE spareparts
            SET stock = stock + ?
            WHERE part_id = ?
            """,
            (
                quantity,
                part_id
            ))

            conn.commit()

            st.success("✅ Manufacturing Record Saved")
            st.success("📦 Inventory Updated Successfully")

        else:

            conn.commit()

            st.warning("⚠ Part ID not found in Spare Parts Database.")

# -------------------------------
# Manufacturing Records
# -------------------------------

st.divider()

st.subheader("📋 Manufacturing Records")

df = pd.read_sql_query(
    "SELECT * FROM manufacturing",
    conn
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# Statistics
# -------------------------------

st.divider()

st.subheader("📊 Manufacturing Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Records",
        len(df)
    )

with col2:

    if len(df) > 0:
        st.metric(
            "Total Manufactured",
            int(df["quantity"].sum())
        )
    else:
        st.metric(
            "Total Manufactured",
            0
        )

conn.close()