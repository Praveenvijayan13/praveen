import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 AI Auto Spare Parts Lifecycle Management System")

st.markdown("### Professional Product Lifecycle Management Dashboard")

# -------------------------
# Database Connection
# -------------------------

conn = sqlite3.connect("database/spareparts.db")

# Spare Parts
try:
    parts = pd.read_sql_query(
        "SELECT * FROM spareparts",
        conn
    )
except:
    parts = pd.DataFrame()

# Manufacturing
try:
    manufacturing = pd.read_sql_query(
        "SELECT * FROM manufacturing",
        conn
    )
except:
    manufacturing = pd.DataFrame()

# Service History
try:
    service = pd.read_sql_query(
        "SELECT * FROM servicehistory",
        conn
    )
except:
    service = pd.DataFrame()

# -------------------------
# KPI Cards
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Total Spare Parts",
        len(parts)
    )

with col2:

    if len(parts) > 0:
        total_stock = int(parts["stock"].sum())
    else:
        total_stock = 0

    st.metric(
        "📋 Total Stock",
        total_stock
    )

with col3:

    st.metric(
        "🏭 Manufacturing",
        len(manufacturing)
    )

with col4:

    st.metric(
        "🔧 Services",
        len(service)
    )

st.divider()

# -------------------------
# Inventory Table
# -------------------------

st.subheader("📋 Current Inventory")

if len(parts) > 0:

    st.dataframe(
        parts,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No Spare Parts Available")

st.divider()

# -------------------------
# Low Stock Alert
# -------------------------

st.subheader("⚠ Low Stock Alert")

if len(parts) > 0:

    low = parts[parts["stock"] < 20]

    if len(low) == 0:

        st.success("✅ No Low Stock Items")

    else:

        st.warning("⚠ The following parts have low stock")

        st.dataframe(
            low,
            use_container_width=True,
            hide_index=True
        )

st.divider()

# -------------------------
# Inventory Chart
# -------------------------

st.subheader("📊 Inventory Stock Chart")

if len(parts) > 0:

    chart = parts[["part_name", "stock"]]

    st.bar_chart(
        chart.set_index("part_name")
    )

st.divider()

# -------------------------
# Recent Activity
# -------------------------

st.subheader("🕒 Recent Activity")

if len(manufacturing) > 0:

    st.success(
        f"🏭 Manufacturing Records : {len(manufacturing)}"
    )

if len(service) > 0:

    st.success(
        f"🔧 Service Records : {len(service)}"
    )

if len(parts) > 0:

    st.success(
        f"📦 Spare Parts : {len(parts)}"
    )

conn.close()