import sqlite3
from inventory import Inventory

class DatabaseManager:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products (
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
        self.conn.commit()

    #Utility Methods
    def add_item(self, item: Inventory):
        self.cursor.execute("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                            (item.id, item.name, item.stock, item.price, item.supplier, item.location,
                             item.weight, item.box_dimensions, item.serial_number, item.manufacture_price))
        self.conn.commit()

    def get_all_items(self):
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()
        return [Inventory(*row) for row in rows]

    def get_item_by_serial(self, serial_number):
        self.cursor.execute("SELECT * FROM products WHERE serial_number=?", (serial_number,))
        row = self.cursor.fetchone()
        return Inventory(*row) if row else None

    def delete_item(self, item_id):
        self.cursor.execute("DELETE FROM products WHERE id=?", (item_id,))
        self.conn.commit()

    def update_stock(self, item_id, new_stock):
        self.cursor.execute("UPDATE products SET stock=? WHERE id=?", (new_stock, item_id))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def profit_margin(self, cost_price):
        return ((self.price - cost_price) / self.price) * 100
        
    def get_sku(self):
        return f"{self.name[:3].upper()}-{self.id}-{self.serial_number[-4:]}"