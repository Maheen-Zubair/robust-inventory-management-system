# 🛒 Inventory Management System (Object-Oriented Python)

This project is a simple **Inventory Management System** developed using Python and Object-Oriented Programming (OOP).  
It manages different types of products like **Electronics**, **Grocery**, and **Clothing** using inheritance and polymorphism.

---

## 📌 Features

- Add, Remove, Restock, and Sell products
- Three types of products: `Electronics`, `Grocery`, and `Clothing`
- Track total inventory value
- Remove expired grocery products
- Search products by name or type
- Clean and modular OOP structure using:
  - Abstract Base Classes (`ABC`)
  - Inheritance
  - Encapsulation
  - Polymorphism

---

## 🧱 Class Structure

### 1. `Product` (Abstract Base Class)

- Attributes:
  - `_product_id`, `_name`, `_price`, `_quantity_in_stock`
- Methods:
  - `restock(amount)`
  - `sell(quantity)`
  - `get_total_value()`
  - `__str__()` (abstract)

---

### 2. Subclasses of Product

#### 🖥️ Electronics

- Extra Attributes: `brand`, `warranty_years`
- Overrides: `__str__`

#### 🥫 Grocery

- Extra Attribute: `expiry_date`
- Methods: `is_expired()`
- Overrides: `__str__` (adds freshness status)

#### 👗 Clothing

- Extra Attributes: `size`, `material`
- Overrides: `__str__`

---

### 3. `Inventory`

Manages all products using a dictionary `_products`.

- Methods:
  - `add_product(product)`
  - `remove_product(product_id)`
  - `search_by_name(name)`
  - `search_by_type(product_type)`
  - `list_all_products()`
  - `sell_product(product_id, quantity)`
  - `restock_product(product_id, quantity)`
  - `total_inventory_value()`
  - `remove_expired_products()`


