import streamlit as st
import sqlite3
import pandas as pd
import os

st.set_page_config(page_title="Spare Parts", page_icon="📦")

st.title("📦 Spare Parts Management")

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("database/spareparts.db", check_same_thread=False)
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS spareparts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id TEXT,
    part_name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER,
    supplier TEXT
)
""")

conn.commit()

# Create Images Folder
os.makedirs("images", exist_ok=True)

# -----------------------------
# Add Spare Part
# -----------------------------

st.subheader("➕ Add New Spare Part")

part_id = st.text_input("Part ID")

part_name = st.text_input("Part Name")

category = st.selectbox(
    "Category",
    [
        "Brake",
        "Engine",
        "Transmission",
        "Suspension",
        "Electrical",
        "Body"
    ]
)

price = st.number_input(
    "Price (₹)",
    min_value=0.0
)

stock = st.number_input(
    "Stock",
    min_value=0
)

supplier = st.text_input("Supplier")

# Upload Image
image = st.file_uploader(
    "Upload Spare Part Image",
    type=["jpg", "jpeg", "png"]
)

if st.button("💾 Save Part"):

    cursor.execute("""
    INSERT INTO spareparts
    (part_id,part_name,category,price,stock,supplier)
    VALUES(?,?,?,?,?,?)
    """,
    (
        part_id,
        part_name,
        category,
        price,
        stock,
        supplier
    ))

    conn.commit()

    st.success("✅ Spare Part Saved Successfully!")

    if image is not None:

        image_path = os.path.join("images", image.name)

        with open(image_path, "wb") as f:
            f.write(image.getbuffer())

        st.success("📷 Image Uploaded Successfully")

        st.image(
            image,
            caption=part_name,
            width=250
        )

st.divider()

# -----------------------------
# Search
# -----------------------------

st.subheader("🔍 Search Spare Part")

search = st.text_input("Search by Part ID, Name or Supplier")

if search == "":
    df = pd.read_sql_query(
        "SELECT * FROM spareparts",
        conn
    )
else:
    df = pd.read_sql_query(f"""
    SELECT * FROM spareparts
    WHERE
    part_id LIKE '%{search}%'
    OR part_name LIKE '%{search}%'
    OR supplier LIKE '%{search}%'
    """, conn)

st.subheader("📋 Spare Parts List")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Export CSV
# -----------------------------

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "SpareParts.csv",
    "text/csv"
)

conn.close()