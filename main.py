import sqlite3

conn = sqlite3.connect('inventory.db')

if conn:
    pass
else:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                id INTEGER,
                name TEXT,
                stock INTEGER,
                price REAL
                )""")

    conn.commit()

    conn.close()
