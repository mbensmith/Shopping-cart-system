# Shopping Cart System
# Author: Edmund Gah
# Date: August 14, 2025
# Description: Colorful, category-based, user-friendly Ghana Cedis shopping cart system with discounts and invoice generation.

# ANSI escape codes for colored output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Product catalog in Ghana Cedis (Grouped by category)
catalog = {
    # Fruits
    "Apple": 3.50, "Banana": 2.00, "Orange": 4.00, "Mango": 5.00,
    "Watermelon": 15.00, "Pineapple": 10.00, "Grapes": 18.00,

    # Drinks
    "Juice": 22.00, "Soda": 8.00, "Mineral Water": 5.00,
    "Energy Drink": 12.00, "Tea Pack": 14.00, "Coffee Pack": 20.00,

    # Dairy & Breakfast
    "Milk": 18.00, "Yogurt": 12.00, "Cheese": 25.00, "Cereal": 40.00,
    "Bread": 10.00, "Butter": 16.00, "Eggs": 18.00,

    # Meats & Seafood
    "Chicken (1kg)": 48.00, "Beef (1kg)": 55.00, "Fish (1kg)": 35.00,
    "Sausages": 28.00, "Goat Meat (1kg)": 60.00, "Tuna Can": 14.00,

    # Staples & Cooking
    "Rice (5kg)": 65.00, "Sugar (1kg)": 12.00, "Tomato Paste": 5.00,
    "Cooking Oil (1L)": 28.00, "Salt (1kg)": 5.00, "Spaghetti": 14.00,
    "Beans (1kg)": 18.00, "Corn Flour (1kg)": 9.00, "Palm Oil (1L)": 24.00,

    # Household
    "Soap": 6.00, "Toothpaste": 8.00, "Detergent": 20.00,
    "Tissue Roll": 3.50, "Shampoo": 18.00, "Body Lotion": 25.00
}

# Discount rules (Buy N get 1 free)
discounts = {
    "Apple": 3,
    "Banana": 4,
    "Milk": 2,
    "Soap": 5
}

# Shopping cart
cart = {}

def display_features():
    """Show system features attractively."""
    print(f"{Colors.CYAN}{Colors.BOLD}✨ Shopping Cart System - Features ✨{Colors.END}")
    features = [
        "📦 Over 30 Ghana-market relevant products in categories",
        "🛒 Add, update, and remove items easily",
        "💰 Buy-N-Get-1-Free discounts on selected products",
        "📃 Detailed invoice with applied discounts",
        "🎨 Color-coded, user-friendly terminal interface",
        "✅ Input validation to prevent wrong entries"
    ]
    for feat in features:
        print(f"{Colors.GREEN}{feat}{Colors.END}")
    print()

def display_catalog():
    """Display catalog in categories with colors."""
    categories = {
        "🍎 Fruits": ["Apple", "Banana", "Orange", "Mango", "Watermelon", "Pineapple", "Grapes"],
        "🥤 Drinks": ["Juice", "Soda", "Mineral Water", "Energy Drink", "Tea Pack", "Coffee Pack"],
        "🥛 Dairy & Breakfast": ["Milk", "Yogurt", "Cheese", "Cereal", "Bread", "Butter", "Eggs"],
        "🍖 Meats & Seafood": ["Chicken (1kg)", "Beef (1kg)", "Fish (1kg)", "Sausages", "Goat Meat (1kg)", "Tuna Can"],
        "🍚 Staples & Cooking": ["Rice (5kg)", "Sugar (1kg)", "Tomato Paste", "Cooking Oil (1L)",
                                 "Salt (1kg)", "Spaghetti", "Beans (1kg)", "Corn Flour (1kg)", "Palm Oil (1L)"],
        "🏠 Household": ["Soap", "Toothpaste", "Detergent", "Tissue Roll", "Shampoo", "Body Lotion"]
    }

    print(f"\n{Colors.HEADER}{Colors.BOLD}📦 Product Catalog (GHS):{Colors.END}")
    for category, items in categories.items():
        print(f"\n{Colors.CYAN}{Colors.BOLD}{category}{Colors.END}")
        print(f"{Colors.BLUE}{'Product':<30}{'Price (₵)':<10}{Colors.END}")
        print("-" * 40)
        for product in items:
            price = catalog[product]
            print(f"{product:<30}₵{price:.2f}")

def find_product_name(user_input):
    """Case-insensitive search for product name."""
    for product in catalog.keys():
        if product.lower() == user_input.lower():
            return product
    return None

def view_cart():
    """View current cart."""
    if not cart:
        print(f"\n{Colors.WARNING}🛒 Your cart is empty.{Colors.END}")
        return
    print(f"\n{Colors.HEADER}{Colors.BOLD}🛒 Current Cart:{Colors.END}")
    print(f"{Colors.BLUE}{'Product':<30}{'Quantity':<10}{'Subtotal (₵)':<15}{Colors.END}")
    print("-" * 55)
    for product, qty in sorted(cart.items()):
        subtotal = qty * catalog[product]
        print(f"{product:<30}{qty:<10}₵{subtotal:.2f}")
    print("-" * 55)

def add_to_cart():
    """Add items to cart."""
    display_catalog()
    while True:
        user_input = input(f"\nEnter product name to add (or 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break
        product = find_product_name(user_input)
        if product:
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
    """Update cart items."""
    view_cart()
    if not cart:
        return
    user_input = input("\nEnter product name to update/remove (or 'skip' to cancel): ").strip()
    product = find_product_name(user_input)
    if user_input.lower() == 'skip' or not product or product not in cart:
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
    """Calculate total with discounts."""
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
    """Print detailed invoice."""
    if not cart:
        print(f"\n{Colors.WARNING}🛒 Cart is empty. No invoice to print.{Colors.END}")
        return
    total = calculate_total()
    print(f"\n{Colors.HEADER}{Colors.BOLD}{Colors.UNDERLINE}🧾 FINAL INVOICE (GHS){Colors.END}")
    print(f"{Colors.BLUE}{'Product':<30}{'Qty':<5}{'Price (₵)':<12}{'Subtotal (₵)':<15}{Colors.END}")
    print("-" * 65)
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
        print(f"{product:<30}{qty:<5}₵{price:<10.2f}₵{subtotal:.2f}{discount_note}")
    print("-" * 65)
    print(f"{Colors.BOLD}TOTAL: ₵{total:.2f}{Colors.END}")
    print(f"{Colors.HEADER}💙 Thank you for shopping with us! 💙{Colors.END}")

def main():
    """Main program."""
    print(f"{Colors.HEADER}{Colors.BOLD}🌟 Welcome to the Ghana Shopping Cart System! 🌟{Colors.END}")
    display_features()

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
