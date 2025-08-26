class Inventory:

    def __init__(self, id, name, stock, price, sku, category, supplier, location, weight, dimensions, 
        reorder_level, serial_number, cost_price):
         
         self.id = id
         self.name = name
         self.stock = stock
         self.price = price
         self.sku = sku
         self.category = category
         self.supplier = supplier
         self.location = location
         self.weight = weight
         self.dimensions = dimensions
         self.reorder_level = reorder_level
         self.serial_number = serial_number
         self.cost_price = cost_price

    #Utility Methods
    def update_stock(self, new_stock);
        self.stock = new_stock

    def update_price(self, new_price):
        self.price = new_price

    def profit_margin(self, cost_price):
        return ((self.price - cost_price) / self.price) * 100
         


