import sqlite3
from inventory import Inventory

#Establish a connection to the database
conn = sqlite3.connect('inventory_stock.db') 

#Create our cursor for executing SQL commands
cursor = conn.cursor()

#Create our products table that tracks the warehouse
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            stock INTEGER,
            price REAL,
            supplier TEXT,
            location TEXT,
            weight REAL,
            box_dimensions TEXT,
            serial_number TEXT UNIQUE,
            manufacture_price REAL
       )""")

conn.commit()

#Prefilled Data with Inventory class
item_1 = Inventory(1, "T-Shirt", 100, 19.99, "XSupply", "Warehouse 1", 5.1, "10x10x10cm", 
"SN123456", 10.00)
item_2 = Inventory(2, "Sweater", 50, 39.99, "XSupply", "Warehouse 2", 8.3, "15x15x15cm",
"SN654321", 20.00)
item_3 = Inventory(3, "Jeans", 75, 49.99, "YSupply", "Warehouse 1", 12.5, "15x20x20cm",
"SN789012", 25.00)


#Add Items to database
cursor.execute("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
               (item_1.id, item_1.name, item_1.stock, item_1.price, item_1.supplier, item_1.location,
                item_1.weight, item_1.box_dimensions, item_1.serial_number, item_1.manufacture_price))
cursor.execute("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (item_2.id, item_2.name, item_2.stock, item_2.price, item_2.supplier, item_2.location,
                item_2.weight, item_2.box_dimensions, item_2.serial_number, item_2.manufacture_price))
cursor.execute("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (item_3.id, item_3.name, item_3.stock, item_3.price, item_3.supplier, item_3.location,
                item_3.weight, item_3.box_dimensions, item_3.serial_number, item_3.manufacture_price))

conn.commit()





