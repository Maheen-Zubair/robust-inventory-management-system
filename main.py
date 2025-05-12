from abc import ABC, abstractmethod
from datetime import date

# -------------------- Product Base Class --------------------
class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise Exception("Stock mein itna maal nahi hai.")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

# -------------------- Subclasses --------------------
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, brand, warranty_years):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.brand = brand
        self.warranty_years = warranty_years

    def __str__(self):
        return f"[Electronics] {self._name} - {self.brand} | Price: {self._price} | Stock: {self._quantity_in_stock} | Warranty: {self.warranty_years} years"

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.expiry_date = expiry_date

    def is_expired(self):
        return date.today() > self.expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return f"[Grocery] {self._name} | Price: {self._price} | Stock: {self._quantity_in_stock} | Expiry: {self.expiry_date} ({status})"

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name} | Size: {self.size} | Material: {self.material} | Price: {self._price} | Stock: {self._quantity_in_stock}"

# -------------------- Inventory Class --------------------
class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product._product_id in self._products:
            raise Exception("Duplicate Product ID not allowed.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p._name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if isinstance(p, product_type)]

    def list_all_products(self):
        for product in self._products.values():
            print(product)

    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = [pid for pid, p in self._products.items() if isinstance(p, Grocery) and p.is_expired()]
        for pid in to_remove:
            del self._products[pid]
