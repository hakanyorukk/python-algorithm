from collections import defaultdict

inventory_lines = [
    "apple,3,0.50",
    "banana,6,0.25",
    "cherry,12,0.10",
    "date,0,2.00",
    "BROKEN LINE",
    "elderberry,4,free",
    "fig,2,1.50",
    "grape,20,0.05",
]


def parse_item(line):
    # parts = line.split(",")
    # name = parts[0]
    # qty = int(parts[1])
    # price = float(parts[2])
    try:
        name,qty,price=line.split(",")
        qty = int(qty)
        price = float(price)
    except (AttributeError, ValueError):
        raise Exception("Invalid data")
    else:
        return {"name": name, "qty": qty, "price": price}


def parse_all(lines):
    items = []
    for line in lines:
        try:
            item = parse_item(line)
            items.append(item)
        except Exception:
            continue
    return items


def total_value(items):
    total = 0
    for item in items:
        total += item["qty"] * item["price"]
    return total


def in_stock(items):
    result = []
    for item in items:
        if item["qty"] > 0:
            result.append(item["name"])
    return result


def average_price(items):
    total = 0
    for item in items:
        total += item["price"]
    return round(total / len(items), 1)


def cheapest_item(items):
    cheapest = items[0]
    for item in items:
        if item["price"] < cheapest["price"]:
            cheapest = item
    return cheapest


def restock_report(items, threshold=5):
    low = []
    for i in range(len(items)):
        if items[i]["qty"] <= threshold:
            low.append(items[i]["name"])
    return low


def price_lookup(items):
    lookup = defaultdict(list)
    for item in items:
        lookup[item["qty"]].append(item["price"])
    return lookup


def main():
    items = parse_all(inventory_lines)
    print("Parsed:      ", len(items), "items")
    print("Total value: ", total_value(items))
    print("In stock:    ", in_stock(items))
    print("Avg price:   ", average_price(items))
    print("Cheapest:    ", cheapest_item(items))
    print("Restock:     ", restock_report(items))
    print("Lookup:      ", price_lookup(items))


if __name__ == "__main__":
    main()