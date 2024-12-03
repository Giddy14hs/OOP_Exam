class Product:
    def __init__(self, productID, name, quantity, price):
        self.productID = productID
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount

    def calculate_total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"ProductID: {self.productID}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.productID] = product

    def search_product(self, identifier):
        for product in self.products.values():
            if product.productID == identifier or product.name == identifier:
                return product
        return None

    def total_inventory_value(self):
        return sum(product.calculate_total_value() for product in self.products.values())

# Example usage
product1 = Product(1, "Laptop", 10, 500)
product2 = Product(2, "Mouse", 50, 20)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

print(inventory.search_product(1))
print("Total Inventory Value:", inventory.total_inventory_value())
