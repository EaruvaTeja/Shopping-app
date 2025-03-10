# Shopping-app

shopping-app

March 7, 2025

**1 Technical Documentation for Shopping App Using Python**

1. **Overview**

The Shopping App is a backend e-commerce application developed in Python, designed to simulate a marketplace where users can browse products, add items to their carts, and complete purchases via various payment options. The application features user and admin login functionalities, category management, and a product catalog. It aims to provide a seamless shopping experience without incorporating front-end UX/UI or database connectivity.

2. **Technical Specifications**
1. **Architecture**
- **Backend Framework:** Python
- **Session Management:** In-memory session storage using a dictionary
- **User Authentication:** Basic authentication with username and password
- **Product Catalog:** Simple dictionary-based storage for product details
- **Cart Management:** User-specific cart management based on session IDs
- **Payment Options:** Simulation of various payment checkout options
2. **Dependencies**
- Python 3.x
- (Optional) uuid library for generating unique session IDs
3. **Requirements**
- Python installed on your machine.
- A code editor or IDE to write and execute Python scripts.
3. **Installation/Setup Instructions**
1. **Install Python:** Ensure you have Python 3.x installed on your system. You can download it from [python.org.](https://www.python.org/downloads/)
1. **Create a New Python File:** Create a new file named shopping\_app.py.
1. **Copy the Code:** Copy the following sample code into your shopping\_app.py file.

import uuid

- *Dummy databases for users and admin* user\_db = {

"user1": "userpass",

"user2": "userpass"

}

admin\_db = {

"admin": "adminpass" }

- *Session storage (maps session id to user type and username)* sessions = {}
- *Categories (category\_id: category\_name)* categories = {

"C1": "Footwear",

"C2": "Clothing",

"C3": "Electronics",

"C4": "Accessories"

}

- *Dummy product catalog (product\_id: {name, category\_id, price})* catalog = {

"P1": {"name": "Boots", "category\_id": "C1", "price": 2500}, "P2": {"name": "Coat", "category\_id": "C2", "price": 3500}, "P3": {"name": "Jacket", "category\_id": "C2", "price": 4000}, "P4": {"name": "Cap", "category\_id": "C4", "price": 800}

}

- *Cart storage* carts = {}

  **def** welcome\_message():

print("Welcome to the Demo Marketplace")

**def** user\_login(username, password):

**if** username **in** user\_db **and** user\_db[username] == password:

session\_id = str(uuid.uuid4())

sessions[session\_id] = {"user\_type": "user", "username": username} print(f"User {username} logged in. Session ID: {session\_id}") **return** session\_id

**else**:

print("Invalid username or password.") **return** None

**def** admin\_login(username, password):

**if** username **in** admin\_db **and** admin\_db[username] == password:

session\_id = str(uuid.uuid4())

sessions[session\_id] = {"user\_type": "admin", "username": username} print(f"Admin {username} logged in. Session ID: {session\_id}") **return** session\_id

**else**:

print("Invalid admin username or password.") **return** None

**def** view\_catalog():

print("Product Catalog:")

**for** product\_id, details **in** catalog.items():

print(f"ID: {product\_id}, Name: {details['name']}, Category: {categories[details['category\_id' **def** add\_to\_cart(session\_id, product\_id, quantity):

**if** session\_id **in** sessions **and** sessions[session\_id]["user\_type"] == "user":

**if** product\_id **in** catalog:

**if** session\_id **not in** carts:

carts[session\_id] = {}

carts[session\_id][product\_id] = quantity

print(f"Added {quantity} of {catalog[product\_id]['name']} to cart.")

**else**:

print("Invalid product ID.") **else**:

print("User is not logged in.")

**def** view\_cart(session\_id):

**if** session\_id **in** carts:

print("Your Cart:")

**for** product\_id, quantity **in** carts[session\_id].items():

print(f"ID: {product\_id}, Name: {catalog[product\_id]['name']}, Quantity: {quantity}

**else**:

print("Your cart is empty.")

**def** remove\_from\_cart(session\_id, product\_id):

**if** session\_id **in** carts **and** product\_id **in** carts[session\_id]:

**del** carts[session\_id][product\_id]

print(f"Removed {catalog[product\_id]['name']} from cart.")

**else**:

print("Product not in cart.")

**def** checkout(payment\_method):

print(f"Your order is successfully placed. Payment method: {payment\_method}")

- *Running the application*

**if** \_\_name\_\_ == "\_\_main\_\_":

welcome\_message()

user\_sid = user\_login("user1", "userpass") view\_catalog()

add\_to\_cart(user\_sid, "P1", 1)

view\_cart(user\_sid) checkout("UPI")

4. **Run the Application:** Open a terminal/command prompt, navigate to the directory where shopping\_app.py is saved, and run the command:

   python shopping\_app.py

4. **Usage Examples**
1. **Welcome Message:** The application will display a welcome message upon startup.
1. **User Login:** Call the user\_login(username, password) function to log in a user. Exam- ple:

   user\_sid = user\_login("user1", "userpass")

3. **View Product Catalog:** Use the view\_catalog() function to display available products.
3. **Add Items to Cart:** To add an item to the cart, call: add\_to\_cart(user\_sid, "P1", 1)
3. **View Cart:** The view\_cart(session\_id) function displays all items in the user’s cart.
3. **Checkout:** To simulate a checkout, call:

   checkout("UPI")

5. **Error Handling and Troubleshooting**
- **Invalid Login Credentials:** Ensure the username and password match those in the respec- tive databases.
- **No Access to Cart:** Ensure you are logged in as a user before trying to access the cart.
- **Invalid Product ID:** Check that the product ID exists in the catalog before adding it to the cart.
- **Empty Cart Notification:** If the cart is empty, a notification will be displayed when trying to view the cart.
6. **Best Practices**
- Keep user passwords hashed in a real application (not in plain text).
- Use a persistent database for storing user and product data.
- Implement thorough error handling for a better user experience.
- Secure session management to prevent unauthorized access.

This documentation serves as a guide to understand and implement the shopping application back- end in Python. Follow each section carefully to set up and explore the application successfully.
4
