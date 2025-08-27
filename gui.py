import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory
from database import DatabaseManager

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