# Shopping-app

March 7, 2025

# Technical Documentation for Shopping App Using Python

## 1. Overview

### Project Name
Creating a Shopping App Using Python

### Project Description
The goal of this project is to develop a simple e-commerce application in Python that supports user and admin login features, product categories, cart management, and payment processing. The application focuses on backend functionality without requiring user interface (UX/UI) design or database connectivity.

### Features
- Welcome message upon application start
- User and Admin login functionality
- Product catalog with multiple categories
- Cart management (add/remove items)
- Multiple payment options for checkout

## 2. Technical Specifications

### Architecture
- **Programming Language**: Python
- **Framework**: None (standalone Python script)
- **Data Storage**: In-memory dictionaries (simulating a database)
- **Functionality**:
  - User Authentication: User and Admin
  - Product Management: Categories and Items
  - Cart Management: Add/Remove Items
  - Payment Processing: Demo checkout options

### Modules
- `uuid`: For session ID generation
- `json`: For serializing and deserializing data (if needed for future extension)

## 3. Dependencies and Requirements

### Required Python Version
- Python 3.x

### Additional Libraries
- No additional libraries are required. All functionality is implemented using built-in Python features.

## 4. Installation/Setup Instructions

1. **Install Python**: Ensure that Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
   
2. **Clone/Download the Source Code**: Obtain the source code for the project. This can be done by cloning the Git repository or simply downloading the .py file.
   
3. **Run the Application**: Navigate to the directory containing the Python file and execute the following command:
   ```bash
   python shopping_app.py
   ```

## 5. Usage Examples

### Code Snippets
Here is an example code snippet demonstrating the core functionality of the application:

```python
import uuid

# Sample data for users, products, and cart
users = {"user": "password"}
admin = {"admin": "adminpass"}
products = {
    1: {"name": "Boots", "category": "Footwear", "price": 1000},
    2: {"name": "Coat", "category": "Clothing", "price": 2000},
    3: {"name": "Jacket", "category": "Clothing", "price": 1500},
    4: {"name": "Cap", "category": "Accessories", "price": 300}
}
cart = {}

def welcome_message():
    print("Welcome to the Demo Marketplace")

def login(username, password):
    if username in users and users[username] == password:
        session_id = str(uuid.uuid4())
        print(f"User {username} logged in with session ID {session_id}")
        return session_id
    elif username in admin and admin[username] == password:
        session_id = str(uuid.uuid4())
        print(f"Admin {username} logged in with session ID {session_id}")
        return session_id
    else:
        print("Login failed! Invalid credentials.")
        return None

def view_catalog():
    print("Product Catalog:")
    for product_id, product_info in products.items():
        print(f"ID: {product_id}, Name: {product_info['name']}, Price: Rs. {product_info['price']}")

# Example of adding items to the cart
def add_to_cart(session_id, product_id, quantity):
    if product_id in products:
        if session_id not in cart:
            cart[session_id] = {}
        cart[session_id][product_id] = quantity
        print(f"Added {quantity} of {products[product_id]['name']} to the cart.")
    else:
        print("Invalid product ID.")

welcome_message()
session = login("user", "password")
view_catalog()
add_to_cart(session, 1, 2)  # Example of adding 2 Boots to the cart
```

## 6. Document API Endpoints / Functions

### Functions

1. **welcome_message()**
   - Displays the welcome message to the user.
   
2. **login(username, password)**
   - Accepts a username and password.
   - Returns a session ID upon successful login.

3. **view_catalog()**
   - Displays a list of available products in the catalog.

4. **add_to_cart(session_id, product_id, quantity)**
   - Adds products to the user’s cart based on session ID.

## 7. Error Handling and Troubleshooting

- **Login Failure**: If the login fails, ensure the username and password are correct and that the user exists in the demo database.
- **Invalid Product ID**: If an invalid product ID is provided, a message indicating the error will be shown.
- **Session Management**: Ensure that you are using the correct session ID that was generated upon login. 

## 8. Best Practices for Technical Documentation

- Use clear and concise language.
- Provide code examples and usage scenarios.
- Include comprehensive information about function parameters and return types.
- Structure content logically for easy navigation.

## 9. Formatting and Structure

- Use headings and subheadings to categorize sections.
- Utilize code blocks for code snippets.
- Number the items in lists to improve readability.

## 10. ## Screenshots

### Screenshot 1
![Screenshot 1](ScreenShorts/Screenshot%201.jpg)

### Screenshot 2
![Screenshot 2](ScreenShorts/Screenshot%202.jpg)

### Screenshot 3
![Screenshot 3](ScreenShorts/Screenshot%203.jpg)

### Screenshot 4
![Screenshot 4](ScreenShorts/Screenshot%204.jpg)



## 11. Conclusion

This documentation provides a comprehensive overview of the Shopping App. The application demonstrates the implementation of backend features essential for an e-commerce platform, including user authentication, product management, and cart functionality. Users can extend this project by integrating a user interface and database connectivity for a complete shopping experience.
