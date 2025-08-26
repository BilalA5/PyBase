import sqlite3

conn = sqlite3.connect('inventory.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            stock INTEGER,
            price REAL
            sku TEXT UNIQUE,
            category TEXT,
            supplier TEXT,
            location TEXT,
            weight TEXT,
            dimensions TEXT,
            reorder_level INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       )""")
    
cursor.execute("INSERT INTO products VALUES (5, 'Keychain', 50, 6.99)")

conn.commit()

cursor.execute("SELECT * FROM products WHERE id>=1")

print(cursor.fetchall())    

conn.commit()

conn.close()


