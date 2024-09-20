import re

# Products available in the store by category
products = {
     "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# Function to sort and display products by price
def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("Invalid sort order.")
        return None

    for i, product in enumerate(sorted_products, 1):
        print(f"{i}. {product[0]} - ${product[1]}")
    
    return sorted_products

# Display products without sorting
def display_products(products_list):
    for i, (product_name, product_price) in enumerate(products_list, 1):
        print(f"{i}. {product_name} - ${product_price}")

# Display product categories and allow user to select one
def display_categories():
    print("Categories available:")
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")
    
    try:
        choice = int(input("Select a category (number): ")) - 1
        if 0 <= choice < len(products):
            return choice
        else:
            print("Invalid category selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# Add a product to the shopping cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

# Display the shopping cart and the total cost
def display_cart(cart):
    total_cost = 0
    for product_name, product_price, quantity in cart:
        product_total = product_price * quantity
        total_cost += product_total
        print(f"{product_name} - ${product_price} x {quantity} = ${product_total}")
    print(f"Total cost: ${total_cost}")  # Remove extra newline



# Generate and print a receipt
def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product_name, product_price, quantity in cart:
        print(f"{quantity} x {product_name} - ${product_price} = ${product_price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

# Validate name (must contain both first and last name)
def validate_name(name):
    return bool(re.match(r'^[A-Za-z]+\s[A-Za-z]+$', name))

# Validate email (relaxed to allow formats like "john@doe")
def validate_email(email):
    pattern = r"[^@]+@[^@]+"
    return bool(re.match(pattern, email))

# Main shopping program
def main():
    cart = []
    
    # Get user's name and validate
    name = input("Enter your name (First and Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name (First and Last): ")

    # Get user's email and validate
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    # Shopping process
    while True:
        category_index = display_categories()
        if category_index is None:
            continue
        
        category_name = list(products.keys())[category_index]
        products_list = products[category_name]

        print(f"Products in {category_name}:")
        display_products(products_list)

        sort_order = input("Sort products? (asc/desc or skip): ")
        if sort_order in ["asc", "desc"]:
            sorted_products = display_sorted_products(products_list, sort_order)
        else:
            sorted_products = products_list

        # Select a product
        product_choice = input("Select a product (number): ")
        if not product_choice.isdigit() or int(product_choice) not in range(1, len(sorted_products) + 1):
            print("Invalid product selection.")
            continue

        product_index = int(product_choice) - 1
        product = sorted_products[product_index]

        # Select quantity
        quantity = input("Enter quantity: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity.")
            continue

        add_to_cart(cart, product, int(quantity))
        display_cart(cart)

        # Continue shopping or checkout
        action_choice = input("Select 1 to continue shopping, 2 to checkout: ")
        if action_choice == "2":
            address = input("Enter your delivery address: ")
            total_cost = sum(item[1] * item[2] for item in cart)
            generate_receipt(name, email, cart, total_cost, address)
            break

# Run the main program if the script is run directly
if __name__ == "__main__":
    main()
