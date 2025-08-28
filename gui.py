import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management Dashboard")
        self.root.geometry("1200x650")

        # ===== Top Header =====
        header = tb.Label(
            root,
            text="📦 Inventory Dashboard",
            font=("Helvetica", 20, "bold"),
            bootstyle="inverse-primary",
            padding=10
        )
        header.pack(fill="x")

        # ===== Main Container =====
        main_frame = tb.Frame(root, padding=10)
        main_frame.pack(fill="both", expand=True)

        # ===== Left Panel: Form + Buttons =====
        left_panel = tb.Frame(main_frame, width=400)
        left_panel.pack(side="left", fill="y", padx=(0,10))

        # Form Fields
        form_labels = [
            "Name", "Stock", "Price", "Supplier",
            "Location", "Weight", "Box Dimensions",
            "Serial No.", "Manufacturer Price"
        ]
        self.entries = {}

        for i, label in enumerate(form_labels):
            tb.Label(left_panel, text=label, bootstyle="light").grid(row=i, column=0, sticky="w", pady=5)
            width = 25 if label == "Manufacturer Price" else 20
            entry = tb.Entry(left_panel, width=width, bootstyle="light")
            entry.grid(row=i, column=1, pady=5)
            self.entries[label] = entry

        # Buttons
        button_frame = tb.Frame(left_panel, padding=(0,15))
        button_frame.grid(row=len(form_labels), column=0, columnspan=2, pady=20)

        self.add_btn = tb.Button(button_frame, text="Add", bootstyle="success", command=self.add_product)
        self.add_btn.pack(side="left", padx=5)

        self.update_btn = tb.Button(button_frame, text="Update", bootstyle="info", command=self.update_product)
        self.update_btn.pack(side="left", padx=5)

        self.delete_btn = tb.Button(button_frame, text="Delete", bootstyle="danger", command=self.delete_product)
        self.delete_btn.pack(side="left", padx=5)

        self.clear_btn = tb.Button(button_frame, text="Clear", bootstyle="secondary", command=self.clear_fields)
        self.clear_btn.pack(side="left", padx=5)

        # ===== Right Panel: Table =====
        right_panel = tb.Frame(main_frame)
        right_panel.pack(side="left", fill="both", expand=True)

        # Scrollbars
        self.scroll_x = tb.Scrollbar(right_panel, orient="horizontal")
        self.scroll_y = tb.Scrollbar(right_panel, orient="vertical")

        # Table
        columns = ("ID", "Name", "Stock", "Price", "Supplier", "Location", "Weight",
                   "Box Dimensions", "Serial No.", "Manufacturer Price")
        self.product_table = tb.Treeview(
            right_panel,
            columns=columns,
            show="headings",
            xscrollcommand=self.scroll_x.set,
            yscrollcommand=self.scroll_y.set,
            bootstyle="info"
        )

        self.scroll_x.config(command=self.product_table.xview)
        self.scroll_y.config(command=self.product_table.yview)

        # Pack scrollbars and table
        self.scroll_y.pack(side="right", fill="y")
        self.scroll_x.pack(side="bottom", fill="x")
        self.product_table.pack(fill="both", expand=True)

        # Define headings and column widths
        for col in columns:
            self.product_table.heading(col, text=col)
            self.product_table.column(col, width=130, anchor="center")

        # Load products
        self.load_products()

    # ===== CRUD Functions =====
    def load_products(self):
        # Clear table first
        self.product_table.delete(*self.product_table.get_children())

        # Sample data — replace with DB fetch
        sample_data = [
            (1, "Laptop", 12, 1200, "Dell", "A1", "2kg", "15x10x1", "SN123", 1000),
            (2, "Mouse", 50, 25, "Logitech", "B2", "0.1kg", "3x2x1", "SN456", 15),
        ]
        for row in sample_data:
            self.product_table.insert("", "end", values=row)

    def add_product(self):
        messagebox.showinfo("Info", "Add Product clicked!")

    def update_product(self):
        messagebox.showinfo("Info", "Update Product clicked!")

    def delete_product(self):
        messagebox.showinfo("Info", "Delete Product clicked!")

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, "end")
