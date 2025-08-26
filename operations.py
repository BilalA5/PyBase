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

    def add_item(self, item: Inventory):
        self.cursor.execute("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                            (item.id, item.name, item.stock, item.price, item.supplier, item.location,
                             item.weight, item.box_dimensions, item.serial_number, item.manufacture_price))
        self.conn.commit()









#Utility Methods
def update_stock(self, new_stock):
    self.stock = new_stock

def update_price(self, new_price):
    self.price = new_price

def profit_margin(self, cost_price):
    return ((self.price - cost_price) / self.price) * 100
    
def make_sku(self):
    return f"{self.name[:3].upper()}-{self.id}-{self.serial_number[-4:]}"