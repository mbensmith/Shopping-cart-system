# Shopping Cart System
# Author: Edmund Gah
# Date: August 14, 2025
# Description: A command-line shopping cart application in Ghana Cedis with discounts and invoice generation.

# ANSI escape codes for colored output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Product catalog in Ghana Cedis
catalog = {
    "Apple": 3.50,
    "Banana": 2.00,
    "Orange": 4.00,
    "Milk": 18.00,
    "Bread": 10.00,
    "Cheese": 25.00,
    "Eggs": 18.00,
    "Yogurt": 12.00,
    "Cereal": 40.00,
    "Juice": 22.00,
    "Rice (5kg)": 65.00,
    "Sugar (1kg)": 12.00,
    "Tomato Paste": 5.00,
    "Chicken (1kg)": 48.00,
    "Beef (1kg)": 55.00,
    "Fish (1kg)": 35.00,
    "Cooking Oil (1L)": 28.00,
    "Salt (1kg)": 5.00,
    "Spaghetti": 14.00
}

# Discount rules (Buy N get 1 free)
discounts = {
    "Apple": 3,
    "Banana": 4
}

# Shopping cart
cart = {}

def display_catalog():
    """Display the product catalog in a formatted table."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}📦 Product Catalog (GHS):{Colors.END}")
    print(f"{Colors.BLUE}{'Product':<20}{'Price (₵)':<10}{Colors.END}")
    print("-" * 35)
    for product, price in sorted(catalog.items()):
        print(f"{product:<20}₵{price:.2f}")
    print("-" * 35)

def view_cart():
    """Display the current cart contents."""
    if not cart:
        print(f"\n{Colors.WARNING}🛒 Your cart is empty.{Colors.END}")
        return
    print(f"\n{Colors.HEADER}{Colors.BOLD}🛒 Current Cart:{Colors.END}")
    print(f"{Colors.BLUE}{'Product':<20}{'Quantity':<10}{'Subtotal (₵)':<15}{Colors.END}")
    print("-" * 45)
    for product, qty in sorted(cart.items()):
        subtotal = qty * catalog[product]
        print(f"{product:<20}{qty:<10}₵{subtotal:.2f}")
    print("-" * 45)

def add_to_cart():
    """Add products to the cart."""
    display_catalog()
    while True:
        product = input(f"\nEnter product name to add (or 'done' to finish): ").title()
        if product == 'Done':
            break
        if product in catalog:
            try:
                qty = int(input(f"Enter quantity for {product}: "))
                if qty > 0:
                    cart[product] = cart.get(product, 0) + qty
                    print(f"{Colors.GREEN}✅ Added {qty} {product}(s) to cart.{Colors.END}")
                else:
                    print(f"{Colors.FAIL}❌ Quantity must be positive.{Colors.END}")
            except ValueError:
                print(f"{Colors.FAIL}❌ Please enter a valid number.{Colors.END}")
        else:
            print(f"{Colors.FAIL}❌ Product not found in catalog.{Colors.END}")

def update_cart():
    """Update quantities or remove items."""
    view_cart()
    if not cart:
        return
    product = input("\nEnter product name to update/remove (or 'skip' to cancel): ").title()
    if product == 'Skip' or product not in cart:
        return
    action = input("Update quantity (u), remove (r), or cancel (c)? ").lower()
    if action == 'u':
        try:
            new_qty = int(input(f"Enter new quantity for {product} (0 to remove): "))
            if new_qty >= 0:
                if new_qty == 0:
                    del cart[product]
                    print(f"{Colors.GREEN}✅ Removed {product} from cart.{Colors.END}")
                else:
                    cart[product] = new_qty
                    print(f"{Colors.GREEN}✅ Updated {product} quantity to {new_qty}.{Colors.END}")
            else:
                print(f"{Colors.FAIL}❌ Quantity cannot be negative.{Colors.END}")
        except ValueError:
            print(f"{Colors.FAIL}❌ Please enter a valid number.{Colors.END}")
    elif action == 'r':
        del cart[product]
        print(f"{Colors.GREEN}✅ Removed {product} from cart.{Colors.END}")

def calculate_total():
    """Calculate total cost with discounts."""
    total = 0.0
    for product, qty in cart.items():
        price = catalog[product]
        if product in discounts:
            buy_n = discounts[product]
            free_items = qty // (buy_n + 1)
            paid_items = qty - free_items
            subtotal = paid_items * price
        else:
            subtotal = qty * price
        total += subtotal
    return total

def print_invoice():
    """Print invoice with discounts."""
    if not cart:
        print(f"\n{Colors.WARNING}🛒 Cart is empty. No invoice to print.{Colors.END}")
        return
    total = calculate_total()
    print(f"\n{Colors.HEADER}{Colors.BOLD}{Colors.UNDERLINE}🧾 FINAL INVOICE (GHS){Colors.END}")
    print(f"{Colors.BLUE}{'Product':<20}{'Qty':<5}{'Price (₵)':<12}{'Subtotal (₵)':<15}{Colors.END}")
    print("-" * 55)
    for product, qty in sorted(cart.items()):
        price = catalog[product]
        if product in discounts:
            buy_n = discounts[product]
            free_items = qty // (buy_n + 1)
            subtotal = (qty - free_items) * price
            discount_note = f" (Buy {buy_n} Get 1 Free: {free_items} free)"
        else:
            subtotal = qty * price
            discount_note = ""
        print(f"{product:<20}{qty:<5}₵{price:<10.2f}₵{subtotal:.2f}{discount_note}")
    print("-" * 55)
    print(f"{Colors.BOLD}TOTAL: ₵{total:.2f}{Colors.END}")
    print(f"{Colors.HEADER}💙 Thank you for shopping with us! 💙{Colors.END}")

def main():
    """Run the shopping cart system."""
    print(f"{Colors.HEADER}{Colors.BOLD}🌟 Welcome to the Shopping Cart System (GHS)! 🌟{Colors.END}")
    print("Browse products, add to cart, and checkout when ready.\n")

    while True:
        print(f"\n{Colors.BLUE}📌 Menu Options:{Colors.END}")
        print("1) Display Catalog")
        print("2) Add to Cart")
        print("3) View Cart")
        print("4) Update/Remove from Cart")
        print("5) Print Invoice & Checkout")
        print("6) Exit")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            display_catalog()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            update_cart()
        elif choice == '5':
            print_invoice()
            confirm = input("\nProceed to checkout and exit? (y/n): ").lower()
            if confirm == 'y':
                break
        elif choice == '6':
            print(f"{Colors.GREEN}👋 Exiting the system. Goodbye!{Colors.END}")
            break
        else:
            print(f"{Colors.FAIL}❌ Invalid option. Please choose 1-6.{Colors.END}")

if __name__ == "__main__":
    main()
