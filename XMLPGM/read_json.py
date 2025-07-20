import json

with open('students.json') as file:
    data = json.load(file)


print("Market Name:", data["market_name"])
print("Location:", data["location"])
print("\nProducts:\n")


for product in data["products"]:
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']}")
    print(f"Quantity: {product['quantity']}")
    print("-" * 20)
