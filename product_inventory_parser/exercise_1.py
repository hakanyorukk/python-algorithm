from collections import Counter

class InvalidProductError(Exception): pass

class Product:

    def __init__(self, name, category, price, quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity

    @classmethod
    def from_line(cls, line):
        try:
            name,category,price,quantity=line.split(",")
            price=float(price)
            quantity=int(quantity)
        except ValueError:
            raise InvalidProductError("Invalid product")
        else:
            return cls(name.strip(),category.strip(),price,quantity)

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Quantity: {self.quantity}"

class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self):
        return round(sum((p.price * p.quantity) for p in self.products), 2)

    def count_by_category(self):
        return dict(Counter(p.category for p in self.products))

    def most_expensive(self):
        if not self.products:
            return None
        return max(self.products, key=lambda p:p.price)

    def __repr__(self):
        return f"Inventory: {self.products}"

def read_from_file(filename):
    lines=[]
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File couldn't find")
        return []
    else:
        return lines

def main():
    lines = read_from_file("sample.txt")
    skipped=0
    inventory = Inventory()
    for line in lines:
        if not line.strip():
            continue
        try:
            inventory.add_product(Product.from_line(line.strip()))
        except InvalidProductError:
            skipped+=1
    print(f"Skipped {skipped} malformed lines")
    print(f"Total value: {inventory.total_value():.2f}")
    print(f"Count by category: {inventory.count_by_category()}")
    print(f"Most expensive: {inventory.most_expensive()}")


if __name__ == "__main__": main()

