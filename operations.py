from inventory import Inventory

#Utility Methods
def update_stock(self, new_stock):
    self.stock = new_stock

def update_price(self, new_price):
    self.price = new_price

def profit_margin(self, cost_price):
    return ((self.price - cost_price) / self.price) * 100
    
def make_sku(self):
    return f"{self.name[:3].upper()}-{self.id}-{self.serial_number[-4:]}"