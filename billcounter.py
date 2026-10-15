def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal = subtotal + item["quantity"] * item["price"]
    return subtotal
def calculate_discount(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.10
    elif subtotal >= 2000:
        return subtotal * 0.05
    else:
        return 0
def calculate_tax(amount):
    return amount * 0.18
items = []
n = int(input("Enter number of products: "))
for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    items.append(product)
subtotal = calculate_subtotal(items)
discount = calculate_discount(subtotal)
amount_after_discount = subtotal - discount
tax = calculate_tax(amount_after_discount)
final_amount = amount_after_discount + tax
print("\n")
print("=" * 50)
print("********************SHOPPING BILL*****************")
print("=" * 50)
print("Product\t\tQuantity\tPrice\tAmount")
print("-" * 50)
for item in items:
    amount = item["quantity"] * item["price"]
    print(
        item["name"],
        "\t\t",
        item["quantity"],
        "\t\t",
        item["price"],
        "\t",
        amount
    )
print("-" * 50)
print("Subtotal:     $", round(subtotal, 2))
print("Discount:     $", round(discount, 2))
print("Tax (18%):    $", round(tax, 2))
print("Final Amount: $", round(final_amount, 2))
print("=" * 50)
print("******************Thank You! Visit Again*****************")
print("=" * 50)
