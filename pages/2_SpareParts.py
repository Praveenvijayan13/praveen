import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Spare Parts Management",
    page_icon="📦",
    layout="wide"
)

# ============================================================
# DATABASE
# ============================================================

DB_PATH = Path("database/spareparts.db")

# Make sure database folder exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(
    str(DB_PATH),
    check_same_thread=False
)

cursor = conn.cursor()

# ============================================================
# CREATE SPARE PARTS TABLE
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS spareparts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id TEXT UNIQUE NOT NULL,
    part_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0,
    stock INTEGER NOT NULL DEFAULT 0,
    supplier TEXT NOT NULL
)
""")

conn.commit()

# ============================================================
# TITLE
# ============================================================

st.title("📦 Spare Parts Management")

st.divider()

# ============================================================
# ADD NEW SPARE PART
# ============================================================

st.subheader("➕ Add New Spare Part")

col1, col2 = st.columns(2)

with col1:

    part_id = st.text_input(
        "Part ID",
        placeholder="Example: SP001"
    )

with col2:

    part_name = st.text_input(
        "Part Name",
        placeholder="Example: Brake Pad"
    )

col3, col4 = st.columns(2)

with col3:

    category = st.selectbox(
        "Category",
        [
            "Brake",
            "Engine",
            "Transmission",
            "Suspension",
            "Wheel",
            "Electrical",
            "Cooling",
            "Exterior",
            "Lighting",
            "Steering",
            "Other"
        ]
    )

with col4:

    price = st.number_input(
        "Price (₹)",
        min_value=0.0,
        value=0.0,
        step=50.0
    )

col5, col6 = st.columns(2)

with col5:

    stock = st.number_input(
        "Stock",
        min_value=0,
        value=0,
        step=1
    )

with col6:

    supplier = st.text_input(
        "Supplier",
        placeholder="Example: Bosch"
    )

# ============================================================
# SAVE SPARE PART
# ============================================================

if st.button("💾 Save Part", use_container_width=True):

    part_id_clean = part_id.strip().upper()
    part_name_clean = part_name.strip()
    supplier_clean = supplier.strip()

    if part_id_clean == "":

        st.warning("⚠️ Please enter Part ID.")

    elif part_name_clean == "":

        st.warning("⚠️ Please enter Part Name.")

    elif supplier_clean == "":

        st.warning("⚠️ Please enter Supplier.")

    else:

        try:

            # Check duplicate Part ID
            cursor.execute(
                """
                SELECT id
                FROM spareparts
                WHERE part_id = ?
                """,
                (part_id_clean,)
            )

            existing = cursor.fetchone()

            if existing:

                st.error(
                    f"❌ Part ID {part_id_clean} already exists."
                )

            else:

                # Insert spare part
                cursor.execute(
                    """
                    INSERT INTO spareparts
                    (
                        part_id,
                        part_name,
                        category,
                        price,
                        stock,
                        supplier
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        part_id_clean,
                        part_name_clean,
                        category,
                        float(price),
                        int(stock),
                        supplier_clean
                    )
                )

                conn.commit()

                st.success(
                    f"✅ {part_id_clean} - "
                    f"{part_name_clean} added successfully!"
                )

        except sqlite3.Error as e:

            conn.rollback()

            st.error(
                "❌ Database error while saving spare part."
            )

            st.code(str(e))

# ============================================================
# SEARCH
# ============================================================

st.divider()

st.subheader("🔍 Search Spare Part")

search = st.text_input(
    "Search by Part ID, Name, Category or Supplier",
    placeholder="Example: SP001 or Brake or Bosch"
)

# ============================================================
# DISPLAY DATA
# ============================================================

if search.strip() == "":

    df = pd.read_sql_query(
        """
        SELECT
            id,
            part_id,
            part_name,
            category,
            price,
            stock,
            supplier
        FROM spareparts
        ORDER BY id ASC
        """,
        conn
    )

else:

    search_value = f"%{search.strip()}%"

    df = pd.read_sql_query(
        """
        SELECT
            id,
            part_id,
            part_name,
            category,
            price,
            stock,
            supplier
        FROM spareparts
        WHERE
            part_id LIKE ?
            OR part_name LIKE ?
            OR category LIKE ?
            OR supplier LIKE ?
        ORDER BY id ASC
        """,
        conn,
        params=(
            search_value,
            search_value,
            search_value,
            search_value
        )
    )

# ============================================================
# SPARE PARTS LIST
# ============================================================

st.subheader("📋 Spare Parts List")

if len(df) > 0:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No spare parts found. "
        "Add your first spare part above."
    )

# ============================================================
# SUMMARY
# ============================================================

st.divider()

st.subheader("📊 Spare Parts Summary")

col1, col2, col3 = st.columns(3)

with col1:

    total_parts = pd.read_sql_query(
        """
        SELECT COUNT(*) AS total
        FROM spareparts
        """,
        conn
    ).iloc[0]["total"]

    st.metric(
        "Total Spare Parts",
        int(total_parts)
    )

with col2:

    total_stock = pd.read_sql_query(
        """
        SELECT COALESCE(SUM(stock), 0) AS total
        FROM spareparts
        """,
        conn
    ).iloc[0]["total"]

    st.metric(
        "Total Stock",
        int(total_stock)
    )

with col3:

    total_value = pd.read_sql_query(
        """
        SELECT COALESCE(SUM(price * stock), 0) AS total
        FROM spareparts
        """,
        conn
    ).iloc[0]["total"]

    st.metric(
        "Inventory Value",
        f"₹{float(total_value):,.2f}"
    )

# ============================================================
# EXPORT CSV
# ============================================================

st.divider()

st.subheader("📥 Export Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="SpareParts.csv",
    mime="text/csv",
    use_container_width=True
)

# ============================================================
# CLOSE DATABASE
# ============================================================

conn.close()
