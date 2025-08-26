class Inventory:

    def __init__(self, id, name, stock, price, sku, category, supplier, location, weight, dimensions, 
        reorder_level,  created_at, updated_at):
         
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
         self.created_at = created_at
         self.updated_at = updated_at


