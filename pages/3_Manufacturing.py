import streamlit as st
import sqlite3
import pandas as pd
from datetime import date
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Manufacturing Management",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Manufacturing Management")

# ============================================================
# DATABASE PATH
# ============================================================

DB_PATH = Path("database/spareparts.db")

# Create database folder if it does not exist
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# ============================================================
# DATABASE CONNECTION
# ============================================================

conn = sqlite3.connect(
    str(DB_PATH),
    check_same_thread=False
)

cursor = conn.cursor()

# ============================================================
# CREATE MANUFACTURING TABLE
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS manufacturing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id TEXT NOT NULL,
    part_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    mfg_date TEXT NOT NULL
)
""")

conn.commit()

# ============================================================
# ADD MANUFACTURING RECORD
# ============================================================

st.subheader("➕ Add Manufacturing Record")

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

    quantity = st.number_input(
        "Manufactured Quantity",
        min_value=1,
        value=1,
        step=1
    )

with col4:

    mfg_date = st.date_input(
        "Manufacturing Date",
        value=date.today()
    )

# ============================================================
# SAVE RECORD
# ============================================================

if st.button("💾 Save Record", use_container_width=True):

    # Remove unnecessary spaces
    part_id = part_id.strip()
    part_name = part_name.strip()

    # Validate input
    if not part_id:

        st.warning("⚠️ Please enter Part ID.")

    elif not part_name:

        st.warning("⚠️ Please enter Part Name.")

    elif quantity <= 0:

        st.warning("⚠️ Quantity must be greater than zero.")

    else:

        try:

            # ------------------------------------------------
            # Check whether spare part exists
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT stock
                FROM spareparts
                WHERE part_id = ?
                """,
                (part_id,)
            )

            result = cursor.fetchone()

            # ------------------------------------------------
            # If spare part exists
            # ------------------------------------------------

            if result:

                # Save manufacturing record
                cursor.execute(
                    """
                    INSERT INTO manufacturing
                    (
                        part_id,
                        part_name,
                        quantity,
                        mfg_date
                    )
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        part_id,
                        part_name,
                        int(quantity),
                        str(mfg_date)
                    )
                )

                # Update spare-part stock
                cursor.execute(
                    """
                    UPDATE spareparts
                    SET stock = stock + ?
                    WHERE part_id = ?
                    """,
                    (
                        int(quantity),
                        part_id
                    )
                )

                # Save changes
                conn.commit()

                st.success(
                    f"✅ Manufacturing record saved for {part_id}"
                )

                st.success(
                    f"📦 Inventory increased by {quantity} units."
                )

                # Show updated stock
                cursor.execute(
                    """
                    SELECT stock
                    FROM spareparts
                    WHERE part_id = ?
                    """,
                    (part_id,)
                )

                updated_stock = cursor.fetchone()

                if updated_stock:

                    st.info(
                        f"📊 Current stock of {part_id}: "
                        f"{updated_stock[0]} units"
                    )

            # ------------------------------------------------
            # Spare part does not exist
            # ------------------------------------------------

            else:

                st.warning(
                    f"⚠️ Part ID '{part_id}' was not found "
                    "in the Spare Parts database."
                )

                st.info(
                    "Please add this spare part in the "
                    "Spare Parts module first."
                )

        except sqlite3.Error as e:

            # Undo incomplete transaction
            conn.rollback()

            st.error(
                "❌ Database error occurred while saving "
                "the manufacturing record."
            )

            st.code(str(e))

# ============================================================
# MANUFACTURING RECORDS
# ============================================================

st.divider()

st.subheader("📋 Manufacturing Records")

try:

    df = pd.read_sql_query(
        """
        SELECT
            id,
            part_id AS "Part ID",
            part_name AS "Part Name",
            quantity AS "Manufactured Quantity",
            mfg_date AS "Manufacturing Date"
        FROM manufacturing
        ORDER BY id DESC
        """,
        conn
    )

    if len(df) > 0:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No manufacturing records available yet."
        )

except Exception as e:

    st.error(
        "Unable to load manufacturing records."
    )

# ============================================================
# MANUFACTURING SUMMARY
# ============================================================

st.divider()

st.subheader("📊 Manufacturing Summary")

col1, col2, col3 = st.columns(3)

# ------------------------------------------------------------
# Total Records
# ------------------------------------------------------------

with col1:

    try:

        total_records = pd.read_sql_query(
            """
            SELECT COUNT(*) AS total
            FROM manufacturing
            """,
            conn
        ).iloc[0]["total"]

        st.metric(
            "Total Records",
            int(total_records)
        )

    except:

        st.metric(
            "Total Records",
            0
        )

# ------------------------------------------------------------
# Total Manufactured
# ------------------------------------------------------------

with col2:

    try:

        total_manufactured = pd.read_sql_query(
            """
            SELECT COALESCE(SUM(quantity), 0) AS total
            FROM manufacturing
            """,
            conn
        ).iloc[0]["total"]

        st.metric(
            "Total Manufactured",
            int(total_manufactured)
        )

    except:

        st.metric(
            "Total Manufactured",
            0
        )

# ------------------------------------------------------------
# Different Parts
# ------------------------------------------------------------

with col3:

    try:

        total_parts = pd.read_sql_query(
            """
            SELECT COUNT(DISTINCT part_id) AS total
            FROM manufacturing
            """,
            conn
        ).iloc[0]["total"]

        st.metric(
            "Parts Manufactured",
            int(total_parts)
        )

    except:

        st.metric(
            "Parts Manufactured",
            0
        )

# ============================================================
# CLOSE DATABASE
# ============================================================

conn.close()
