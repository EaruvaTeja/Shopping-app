import razorpay
from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Initialize Razorpay client with your test API keys
client = razorpay.Client(auth=("rzp_test_yjboSPRAoVvP6f", "WQht0SWUxswPjQ9PRWxcZYnp"))

# Simulated in-memory cart for demonstration purposes
user_carts = {
    "test_user": {"P4": 2}  # e.g., 2 Sneakers
}

# Dummy catalog for price lookup (prices in INR)
catalog = {
    "P4": {"name": "Sneakers", "price": 1800}
}

# Payment options (for simulation, we handle all the same way)
payment_options = ["Net Banking", "PayPal", "UPI", "Debit Card"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout')
def checkout():
    # In a real application, you'd determine the user and calculate total
    # Here, we'll simulate for test_user's cart
    username = "test_user"
    cart = user_carts.get(username, {})
    if not cart:
        return "Your cart is empty. Nothing to checkout.", 400

    total = sum(catalog[pid]["price"] * qty for pid, qty in cart.items())
    
    # Create a unique receipt id (for demo purposes)
    receipt_id = f"order_rcptid_{uuid.uuid4().hex[:6]}"
    
    # Create an order in Razorpay (amount in paise)
    order_data = {
        "amount": int(total * 100),  # convert to paise
        "currency": "INR",
        "receipt": receipt_id,
        "payment_capture": 1
    }
    order = client.order.create(data=order_data)
    
    # Clear the cart after order creation (optional, depends on your flow)
    user_carts[username] = {}

    # Render the checkout page with order details
    return render_template("checkout.html", order=order, total=total, key_id="rzp_test_yjboSPRAoVvP6f")

if __name__ == '__main__':
    app.run(debug=True)
