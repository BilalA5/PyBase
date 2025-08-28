import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from operations import DatabaseManager

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # Database Manager
        self.db = DatabaseManager()

        # UI Components
        self.create_widgets()
        self.load_products()

    def create_widgets(self):
        # ====== TITLE ======
        title = tk.Label(
            self.root,
            text="Inventory Management System",
            font=("Helvetica", 18, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=10
        )
        title.pack(fill=tk.X)

        # ====== TABLE FRAME ======
        table_frame = tk.Frame(self.root, padx=10, pady=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Product Table
        columns = ("ID", "Name", "Stock", "Price", "Supplier", "Location", "Weight", "Box Dimensions", "Serial Number", "Manufacture Price")
        self.product_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

        for col in columns:
            self.product_table.heading(col, text=col)
            self.product_table.column(col, width=120, anchor="center")

        self.product_table.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.product_table.yview)
        self.product_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
