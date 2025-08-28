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

    # ====== FORM FRAME ======
        form_frame = tk.Frame(self.root, pady=10)
        form_frame.pack(fill=tk.X)

        labels = ["ID", "Name", "Stock", "Price", "Supplier", "Location", "Weight", "Box Dimensions", "Serial Number", "Manufacture Price"]
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(form_frame, text=label).grid(row=idx // 5, column=(idx % 5) * 2, padx=5, pady=5)
            entry = tk.Entry(form_frame, width=15)
            entry.grid(row=idx // 5, column=(idx % 5) * 2 + 1, padx=5, pady=5)
            self.entries[label] = entry

        # ====== BUTTONS ======
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.pack(fill=tk.X)

        tk.Button(button_frame, text="Add Product", bg="#27AE60", fg="white", command=self.add_product).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Stock", bg="#2980B9", fg="white", command=self.update_stock).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Product", bg="#C0392B", fg="white", command=self.delete_product).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Search by Serial", bg="#8E44AD", fg="white", command=self.search_product).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Refresh", bg="#F39C12", fg="white", command=self.load_products).pack(side=tk.LEFT, padx=5)

    def load_products(self):
        """Load all products into the table"""
        for item in self.product_table.get_children():
            self.product_table.delete(item)
        products = self.db.get_all_items()
        for product in products:
            self.product_table.insert("", tk.END, values=(
                product.id, product.name, product.stock, product.price,
                product.supplier, product.location, product.weight,
                product.box_dimensions, product.serial_number, product.manufacture_price
            ))
