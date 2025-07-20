import csv

# Open and read the CSV file
with open('products.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    print("Product List:")
    print("-" * 30)

    for row in reader:
        print(f"ID: {row['id']}")
        print(f"Name: {row['name']}")
        print(f"Price: ${row['price']}")
        print(f"Quantity: {row['quantity']}")
        print("-" * 30)
