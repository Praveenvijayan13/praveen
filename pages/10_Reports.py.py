import streamlit as st
import sqlite3
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import os

st.title("📄 Reports")

conn = sqlite3.connect("database/spareparts.db")

df = pd.read_sql_query("SELECT * FROM spareparts", conn)

st.subheader("Spare Parts Report")

st.dataframe(df, use_container_width=True)

# CSV Download
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "SpareParts.csv",
    "text/csv"
)

# PDF Download
if st.button("Generate PDF"):

    pdf_file = "SpareParts_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    data = [list(df.columns)] + df.values.tolist()

    table = Table(data)

    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('GRID',(0,0),(-1,-1),1,colors.black),
        ('BACKGROUND',(0,1),(-1,-1),colors.beige)
    ]))

    doc.build([table])

    with open(pdf_file, "rb") as f:

        st.download_button(
            "📄 Download PDF",
            f,
            file_name="SpareParts_Report.pdf"
        )

conn.close()