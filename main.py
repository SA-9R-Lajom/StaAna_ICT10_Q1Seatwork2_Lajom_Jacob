from js import document

restaurant_name = "Midnight Tokyo Brewery"
owner_name = "Jake Marshall"


year_since = 1989
tax_rate = 0.08
has_delivery = True
is_dine_in = True
is_takeaway = True


product_names = ["Spaghetti Bolognese", "California Maki Sushi", "Caesar Salad"]
beverages = ["Iced Tea", "Soda"]
business_hours = ("7:00 AM", "12:00 PM")

menu = {
    "Spaghetti Bolognese": 5.99,
    "Caesar Salad": 3.50,
    "California Maki Sushi": 2.50,
    "Iced Tea": 1.55,
    "Soda": 3.29,
}

common_allergens = {"gluten", "dairy", "nuts"}

def set_text(element_id, text):
    el = document.getElementById(element_id)
    if el is not None:
        el.textContent = text


set_text("owner", f"Owner: {owner_name}")
set_text("since", f"Since {year_since}")

set_text("prod1", product_names[0])
set_text("price1", f"${menu['Spaghetti Bolognese']:.2f}")
set_text("prod2", product_names[1])
set_text("price2", f"${menu['California Maki Sushi']:.2f}")
set_text("prod3", product_names[2])
set_text("price3", f"${menu['Caesar Salad']:.2f}")
set_text("prod4", beverages[0])
set_text("price4", f"${menu['Iced Tea']:.2f}")
set_text("prod5", beverages[1])
set_text("price5", f"${menu['Soda']:.2f}")

set_text("openingHours", f"Open: {business_hours[0]} - {business_hours[1]}")

order_options = []
if is_dine_in: order_options.append("Dine-in")
if is_takeaway: order_options.append("Takeout")
if has_delivery: order_options.append("Delivery")
set_text("orderType", " / ".join(order_options) if order_options else "No order options")