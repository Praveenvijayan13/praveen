import sqlite3

DATABASE = "database/spareparts.db"

def connect():
    return sqlite3.connect(DATABASE)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS spareparts (
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
    conn.close()

def add_part(part_id, part_name, category, price, stock, supplier):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO spareparts
    (part_id, part_name, category, price, stock, supplier)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (part_id, part_name, category, price, stock, supplier))

    conn.commit()
    conn.close()

def view_parts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM spareparts")

    rows = cursor.fetchall()

    conn.close()

    return rows

create_table()