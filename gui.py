import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from operations import DatabaseManager

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.db = DatabaseManager()

        style = ttk.Style()
        style.theme_use("clam")  # Switches to a cross-platform theme
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
        style.map("TButton",
                  foreground=[("active", "white")],
                  background=[("active", "#45a049")])


        # Create widgets first
        self.create_widgets()

        # Now load products after product_table exists
        self.load_products()


    def create_widgets(self):
        # ===== PRODUCT TABLE =====
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        columns = ("ID", "Name", "Stock", "Price", "Supplier", "Location", "Weight", "Dimensions", "Serial", "Manufacture Price")
        self.product_table = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.product_table.heading(col, text=col)
            self.product_table.column(col, width=120)

        # Add vertical + horizontal scrollbars
        y_scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.product_table.yview)
        x_scroll = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.product_table.xview)

        self.product_table.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        self.product_table.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)


        # ====== SCROLLABLE FORM FRAME ======
        form_container = tk.Frame(self.root)
        form_container.pack(fill=tk.X, padx=10, pady=10)

        # Canvas to enable scrolling
        form_canvas = tk.Canvas(form_container, height=120)
        form_canvas.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Horizontal Scrollbar
        scrollbar_x = ttk.Scrollbar(form_container, orient=tk.HORIZONTAL, command=form_canvas.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure canvas scrolling
        form_canvas.configure(xscrollcommand=scrollbar_x.set)
        form_canvas.bind('<Configure>', lambda e: form_canvas.configure(scrollregion=form_canvas.bbox("all")))

        # Frame inside canvas to hold the form
        form_frame = tk.Frame(form_canvas)
        form_canvas.create_window((0, 0), window=form_frame, anchor="nw")

        # ====== FORM FIELDS ======
        labels = [
            "ID", "Name", "Stock", "Price", "Supplier",
            "Location", "Weight", "Box Dimensions",
            "Serial Number", "Manufacture Price"
        ]
        self.entries = {}

        for idx, label in enumerate(labels):
            # Arrange all inputs in a **single horizontal row**
            tk.Label(form_frame, text=label).grid(row=0, column=idx * 2, padx=5, pady=5, sticky="w")

            entry_width = 20 if label == "Manufacture Price" else 18
            entry = tk.Entry(form_frame, width=entry_width)
            entry.grid(row=0, column=idx * 2 + 1, padx=5, pady=5)
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
    
    def add_product(self):
        """Add a new product"""
        try:
            item = Inventory(
                int(self.entries["ID"].get()),
                self.entries["Name"].get(),
                int(self.entries["Stock"].get()),
                float(self.entries["Price"].get()),
                self.entries["Supplier"].get(),
                self.entries["Location"].get(),
                float(self.entries["Weight"].get()),
                self.entries["Box Dimensions"].get(),
                self.entries["Serial Number"].get(),
                float(self.entries["Manufacture Price"].get())
            )
            self.db.add_item(item)
            self.load_products()
            messagebox.showinfo("Success", "Product added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add product: {e}")

    def update_stock(self):
        """Update stock for a product"""
        try:
            item_id = int(self.entries["ID"].get())
            new_stock = int(self.entries["Stock"].get())
            self.db.update_stock(item_id, new_stock)
            self.load_products()
            messagebox.showinfo("Success", "Stock updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update stock: {e}")

    def delete_product(self):
        """Delete a product"""
        try:
            item_id = int(self.entries["ID"].get())
            self.db.delete_item(item_id)
            self.load_products()
            messagebox.showinfo("Deleted", "Product deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete product: {e}")

    def search_product(self):
        """Search product by serial number"""
        try:
            serial_number = self.entries["Serial Number"].get()
            product = self.db.get_item_by_serial(serial_number)
            if product:
                messagebox.showinfo("Product Found", f"Name: {product.name}\nStock: {product.stock}\nPrice: {product.price}")
            else:
                messagebox.showinfo("Not Found", "No product found with this serial number")
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {e}")
