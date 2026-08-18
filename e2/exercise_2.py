raw_products = [
    {"sku": "AB-1234", "name": "  Wireless Mouse ", "price": "29.99", "qty": "150"},
    {"sku": "cd-5678", "name": "Keyboard", "price": "49.50", "qty": "0"},
    {"sku": "EF9999", "name": "Monitor", "price": "199.00", "qty": "25"},
    {"sku": "GH-1111", "name": "", "price": "15.00", "qty": "10"},
    {"sku": "IJ-2222", "name": "Webcam", "price": "free", "qty": "5"},
    {"sku": "KL-3333", "name": "Headset", "price": "-10.00", "qty": "8"},
    {"sku": "MN-4444", "name": "Cable", "price": "5.99", "qty": "-3"},
    {"sku": "OP-5555", "name": "Dock", "price": "89.99"},
]
class ValidationError(Exception): pass

def check_sku(sku):
    try:
        sku_let, sku_num = sku.split("-")
    except:
        raise ValidationError("Invalid sku!")
    if len(sku_let) == 2 and len(sku_num) == 4 and sku_let.isalpha() and sku_num.isdigit():
        return f"{sku_let.upper()}-{sku_num}"
    raise ValidationError("Invalid sku!")

def check_name(name):
    name = name.strip()
    if name:
        return name

    raise ValidationError("Invalid name")

def check_price(price):
    try:
        price = float(price)
    except ValueError:
        raise ValidationError("Invalid price!")

    if not price > 0:
        raise ValidationError("Invalid price!")
    return round(price, 2)

def check_qty(qty):
    try:
        qty = int(qty)
    except ValueError:
        raise ValidationError("Invalid quantity!")
    if qty >= 0:
        return qty
    raise ValidationError("Invalid quantity!")

def validate_products(products):
    valid = []
    invalid = []
    total_value = 0
    for product in products:
        required = {"sku", "name", "price", "qty"}
        missing = required - product.keys()

        if missing:
            invalid.append({"sku": product.get("sku", ""), "reason": f"missing fields: {missing}"})
            continue
        try:
            clean_sku = check_sku(product["sku"])
            clean_name = check_name(product["name"])
            clean_price = check_price(product["price"])
            clean_qty = check_qty(product["qty"])
            valid.append({"sku": clean_sku, "name": clean_name, "price": clean_price, "qty": clean_qty})
            total_value+=clean_price*clean_qty
        except ValidationError as e:
            invalid.append({"sku": product.get("sku", ""), "reason": str(e)})

    return {"valid": valid, "invalid": invalid, "summary": {"count_valid": len(valid), "count_invalid": len(invalid), "total_value": total_value}}


def main():
    print(validate_products(raw_products))

if __name__ == "__main__":
    main()
