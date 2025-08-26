import sqlite3

conn = sqlite3.connect('inventory.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            stock INTEGER,
            price REAL
            supplier TEXT,
            location TEXT,
            weight TEXT,
            dimensions TEXT,
            serial_number TEXT UNIQUE,
            manufacture_price REAL
       )""")
    
cursor.execute("INSERT INTO products VALUES (5, 'Keychain', 50, 6.99)")

conn.commit()

