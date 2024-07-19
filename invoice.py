def get_user_input():
    customer_name = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        items.append((item_name, item_price, item_quantity))
    return customer_name, address, items

def generate_invoice(customer_name, address, items, filename='invoice.txt'):
    with open(filename, 'w') as f:
        f.write("Invoice\n")
        f.write("=======\n\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Address: {address}\n\n")
        f.write("Items:\n")
        f.write("------\n")
        total = 0
        for item_name, item_price, item_quantity in items:
            total_price = item_price * item_quantity
            total += total_price
            f.write(f"{item_name}: ${item_price:.2f} x {item_quantity} = ${total_price:.2f}\n")
        f.write("\n")
        f.write(f"Total Amount: ${total:.2f}\n")

if __name__ == "__main__":
    customer_name, address, items = get_user_input()
    generate_invoice(customer_name, address, items)
    print("Invoice generated successfully.")
