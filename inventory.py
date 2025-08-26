class Inventory:

    def __init__(self, id, name, stock, price, supplier, location, weight, box_dimensions, 
        serial_number, manufacture_price):
         
         self.id = id
         self.name = name
         self.stock = stock
         self.price = price
         self.supplier = supplier
         self.location = location
         self.weight = weight
         self.box_dimensions = box_dimensions
         self.serial_number = serial_number
         self.manufacture_price = manufacture_price

    #Utility Methods
    def update_stock(self, new_stock):
        self.stock = new_stock

    def update_price(self, new_price):
        self.price = new_price

    def profit_margin(self, cost_price):
        return ((self.price - cost_price) / self.price) * 100
    
    def make_sku(self):
        return f"{self.name[:3].upper()}-{self.id}-{self.serial_number[-4:]}"
         
    def __repr__(self):
        return f"Inventory({self.id}, {self.name}, {self.stock}, {self.price}, {self.supplier}, {self.location}, {self.weight}, {self.dimensions}, {self.serial_number}, {self.manufacture_price})"

