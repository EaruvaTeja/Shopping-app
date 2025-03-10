import uuid
import webbrowser
import razorpay

# Dummy databases
user_db = {
    "user1": "userpass",  #demo user id {user1}/{user2} and the password is {userpass} to test try 
    "user2": "userpass"
}

admin_db = {
    "admin": "adminpass" #demo admin id {admin} and password is {adminpass} to test try
}

# Session storage (maps session id to user type and username)
sessions = {}

# Categories (category_id: category_name)
categories = {
    "C1": "Footwear",
    "C2": "Clothing",
    "C3": "Electronics"
}


# Dummy product catalog (product_id: {name, category_id, price})
catalog = {
    "P1": {"name": "Boots", "category_id": "C1", "price": 2500},
    "P2": {"name": "Jacket", "category_id": "C2", "price": 3500},
    "P3": {"name": "Smartphone", "category_id": "C3", "price": 15000},
    "P4": {"name": "Sneakers", "category_id": "C1", "price": 1800}
}

# User carts: mapping username to a dictionary of {product_id: quantity}
user_carts = {}

'''# Demo payment test
client = razorpay.Client(auth=("rzp_test_yjboSPRAoVvP6f", "WQht0SWUxswPjQ9PRWxcZYnp"))'''


# Payment options if we enter option 3 as upi it direclty opens the razorpay link {demo only}
payment_options = ["Net Banking", "PayPal", "UPI", "Debit Card"]

def generate_session(user_type, username):
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"type": user_type, "username": username}
    return session_id

def display_welcome():
    print("\036   Welcome to the Demo Marketplace\n")
    
def login():
    print("LOGIN:")
    role = input("Enter login type (user/admin): ").strip().lower()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if role == "user":
        if username in user_db and user_db[username] == password:
            session_id = generate_session("user", username)
            print(f"User '{username}' logged in successfully. Session id: {session_id}\n")
            # initialize cart if doesn't exist
            if username not in user_carts:
                user_carts[username] = {}
            return session_id
        else:
            print("Invalid user credentials.\n")
            return None
    elif role == "admin":
        if username in admin_db and admin_db[username] == password:
            session_id = generate_session("admin", username)
            print(f"Admin '{username}' logged in successfully. Session id: {session_id}\n")
            return session_id
        else:
            print("Invalid admin credentials.\n")
            return None
    else:
        print("Invalid login type.\n")
        return None

def view_catalog():
    print("\nProduct Catalog:")
    for pid, details in catalog.items():
        category_name = categories.get(details["category_id"], "Unknown")
        print(f"Product ID: {pid} | Name: {details['name']} | Category: {category_name} | Price: Rs. {details['price']}")
    print()

def add_to_cart(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "user":
        print("Only users can add items to the cart.\n")
        return

    username = session["username"]
    view_catalog()
    pid = input("Enter product ID to add: ").strip()
    if pid not in catalog:
        print("Invalid product ID.\n")
        return
    try:
        quantity = int(input("Enter quantity: ").strip())
        if quantity <= 0:
            print("Quantity must be positive.\n")
            return
    except ValueError:
        print("Invalid quantity input.\n")
        return

    cart = user_carts[username]
    cart[pid] = cart.get(pid, 0) + quantity
    print(f"Added {quantity} of {catalog[pid]['name']} to cart.\n")

def remove_from_cart(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "user":
        print("Only users can remove items from the cart.\n")
        return

    username = session["username"]
    cart = user_carts.get(username, {})
    if not cart:
        print("Your cart is empty.\n")
        return
    print("\nCurrent Cart Items:")
    for pid, qty in cart.items():
        print(f"Product ID: {pid} | Name: {catalog[pid]['name']} | Quantity: {qty}")
    pid = input("Enter product ID to remove: ").strip()
    if pid not in cart:
        print("Product not in cart.\n")
        return
    try:
        quantity = int(input("Enter quantity to remove: ").strip())
        if quantity <= 0:
            print("Quantity must be positive.\n")
            return
    except ValueError:
        print("Invalid quantity input.\n")
        return

    if quantity >= cart[pid]:
        del cart[pid]
        print(f"Removed all of {catalog[pid]['name']} from cart.\n")
    else:
        cart[pid] -= quantity
        print(f"Removed {quantity} of {catalog[pid]['name']} from cart.\n")

def view_cart(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "user":
        print("Only users have carts.\n")
        return
    username = session["username"]
    cart = user_carts.get(username, {})
    if not cart:
        print("Your cart is empty.\n") 
    else:
        print("\nYour Cart:")
        total = 0
        for pid, qty in cart.items():
            price = catalog[pid]["price"]
            print(f"Product: {catalog[pid]['name']} | Quantity: {qty} | Price per unit: Rs. {price}")
            total += price * qty
        print(f"Total Amount: Rs. {total}\n")

def checkout(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "user":
        print("Only users can perform checkout.\n")
        return
    username = session["username"]
    cart = user_carts.get(username, {})
    if not cart:
        print("Your cart is empty. Nothing to checkout.\n")
        return

    total = sum(catalog[pid]["price"] * qty for pid, qty in cart.items())
    print("\nPayment Options:")
    for idx, option in enumerate(payment_options, 1):
        print(f"{idx}. {option}")
    try:
        choice = int(input("Select payment option (enter number): ").strip())
        if 1 <= choice <= len(payment_options):
            selected = payment_options[choice - 1]
            

            if selected == "UPI":
                print(f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs. {total}")
                webbrowser.open("https://razorpay.me/@earuvateja")
                  # Directly opens my razorpay website to pay {Demo only}
            else:
                print(f"Your payment order of using {selected}. Total amount: Rs. {total} is beeing processed... please complete the payment")
                webbrowser.open("https://razorpay.me/@earuvateja")
                  # Directly opens my razorpay website to pay {Demo only}
            user_carts[username] = {}
        else:
            print("Invalid payment option.\n")
    except ValueError:
        print("Invalid input. Payment aborted.\n")


''' i have tryed to make a test razor pay using api but it is takes time more than usual,
      so i have just included my own razorpay as a test pay link

    def test_razorpay():
    # Your code to handle Razorpay test payment redirection
    print("Simulating Razorpay redirection...")

# For testing, checkout():
# checkout(session_id)  # session_id 
'''

'''#Checkout Razor pay test
def create_order(amount, currency="INR", receipt="order_rcptid_11"):
    # amount in the smallest currency unit (e.g., paise for INR)
    order_data = {
        "amount": int(amount * 100),  # convert rupees to paise
        "currency": currency,
        "receipt": receipt,
        "payment_capture": 1  # auto-capture payment on successful transaction
    }
    order = client.order.create(data=order_data)
    return order
'''


def admin_add_product(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "admin":
        print("Only admin can add products.\n")
        return

    pid = input("Enter new product ID: ").strip()
    if pid in catalog:
        print("Product ID already exists.\n")
        return
    name = input("Enter product name: ").strip()
    print("Available Categories:")
    for cid, cname in categories.items():
        print(f"{cid}: {cname}")
    category_id = input("Enter category ID: ").strip()
    if category_id not in categories:
        print("Invalid category ID.\n")
        return
    try:
        price = float(input("Enter product price: ").strip())
    except ValueError:
        print("Invalid price input.\n")
        return

    catalog[pid] = {"name": name, "category_id": category_id, "price": price}
    print(f"Product '{name}' added successfully.\n") 
     #Admin can delete or add products or categories only during a certain execution status, not in the permanent database.
     #Saving to the real-time database is a complex task that involves MongoDB, SQL, or other technologies, so I have created a demo instead.

def admin_update_product(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "admin":
        print("Only admin can update products.\n")
        return

    pid = input("Enter product ID to update: ").strip()
    if pid not in catalog:
        print("Product not found.\n")
        return
    print("Enter new details (leave blank to keep current value):")
    current = catalog[pid]
    name = input(f"Product name [{current['name']}]: ").strip()
    print("Available Categories:")
    for cid, cname in categories.items():
        print(f"{cid}: {cname}")
    category_id = input(f"Category ID [{current['category_id']}]: ").strip()
    price_input = input(f"Price [{current['price']}]: ").strip()
    
    if name:
        current['name'] = name
    if category_id:
        if category_id in categories:
            current['category_id'] = category_id
        else:
            print("Invalid category ID. Keeping existing category.")
    if price_input:
        try:
            current['price'] = float(price_input)
        except ValueError:
            print("Invalid price input. Keeping existing price.")
    print(f"Product '{pid}' updated successfully.\n")

def admin_delete_product(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "admin":
        print("Only admin can delete products.\n")       #user cannot delete/add products or categories
        return

    pid = input("Enter product ID to delete: ").strip()
    if pid in catalog:
        del catalog[pid]
        print(f"Product '{pid}' deleted successfully.\n")  #admin can able to delete/add products or categories 
    else:
        print("Product not found.\n")

def admin_add_category(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "admin":
        print("Only admin can add categories.\n")      #user cannot delete/add product or categories
        return

    cid = input("Enter new category ID: ").strip()
    if cid in categories:
        print("Category ID already exists.\n")
        return
    name = input("Enter category name: ").strip()
    categories[cid] = name
    print(f"Category '{name}' added successfully.\n")    #Category/product will be added/delete only in execution status not in db

def admin_delete_category(session_id):
    session = sessions.get(session_id)
    if not session or session["type"] != "admin":
        print("Only admin can delete categories.\n")
        return

    cid = input("Enter category ID to delete: ").strip()
    if cid not in categories:
        print("Category not found.\n")
        return
    # Check if any product belongs to this category
    in_use = [pid for pid, prod in catalog.items() if prod["category_id"] == cid]
    if in_use:
        print("Cannot delete category. One or more products belong to this category.\n")
        return
    del categories[cid]
    print(f"Category '{cid}' deleted successfully.\n")

def user_menu(session_id): #session
    while True:
        print("User Menu:")
        print("1. View Catalog")
        print("2. View Cart")
        print("3. Add Item to Cart")
        print("4. Remove Item from Cart")
        print("5. Checkout")
        print("6. Logout")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            view_catalog()
        elif choice == "2":
            view_cart(session_id)
        elif choice == "3":
            add_to_cart(session_id)
        elif choice == "4":
            remove_from_cart(session_id)
        elif choice == "5":
            checkout(session_id)
        elif choice == "6":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")

def admin_menu(session_id):
    while True:
        print("Admin Menu:")
        print("1. View Catalog")
        print("2. Add New Product")
        print("3. Update Existing Product")
        print("4. Delete Product")
        print("5. Add New Category")
        print("6. Delete Category")
        print("7. Logout")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            view_catalog()
        elif choice == "2":
            admin_add_product(session_id)
        elif choice == "3":
            admin_update_product(session_id)
        elif choice == "4":
            admin_delete_product(session_id)
        elif choice == "5":
            admin_add_category(session_id)
        elif choice == "6":
            admin_delete_category(session_id)
        elif choice == "7":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")

def main():
    display_welcome()
    session_id = login()
    if not session_id:
        return
    user_type = sessions[session_id]["type"]
    if user_type == "user":
        user_menu(session_id)
    elif user_type == "admin":
        admin_menu(session_id)
    else:
        print("Unknown session type.\n")

if __name__ == "__main__":
    main()
