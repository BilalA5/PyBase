from inventory import Inventory
from operations import DatabaseManager
import tkinter as tk
from gui import InventoryGUI

#Initalize Database Manager
database = "inventory_stock.db"
dbm = DatabaseManager(database)

#Create Warehouse Items

item_1 = Inventory(1, "T-Shirt", 100, 29.99, "Gildan", "Warehouse 1", 5.5, "15x10x1 cm", "SN12345678", 12.00)
item_2 = Inventory(2, "Sweater", 50, 14.99, "Gildan", "Warehouse 1", 7.2, "20x15x2 cm", "SN87654321", 20.00)
item_3 = Inventory(3, "Jeans", 75, 29.99, "Levi's", "Warehouse 2", 10.0, "30x20x3 cm", "SN11223344", 17.49)

#Add Items to Database
dbm.add_item(item_1)
dbm.add_item(item_2)
dbm.add_item(item_3)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()





