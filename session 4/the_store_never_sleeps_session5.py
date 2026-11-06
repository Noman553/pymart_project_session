# PyMart - Store Never Sleeps
# session 5 : Hello , FrenchMart
# Author : <Noman Mehmood>

import math

# ----- Session 4 Constants -----
MART_NAME = "French Mart"
MART_ADDRESS = "Malakwal Jinnah road"
MART_PHONE = "03486120924"
GST_RATE = 0.18
MAX_QTY_PER_ITEM = 100

# --- Session 5 Constants ---
CASHIER_PIN = "1234"
MAX_PIN_ATTEMPTS = 3

# --- Global Trackers ---
receipt_counter = 0


# --- Session 4 Calculation Helpers ---
def subtotal(items_unite_price, items_quantity):
    return items_unite_price * items_quantity


def gst(subtotal_amount, rate=GST_RATE):
    return subtotal_amount * rate


def calculating_total(amount, calculate_gst):
    return math.ceil(amount + calculate_gst)


def receipt_no_counter():
    global receipt_counter
    receipt_counter = receipt_counter + 1
    return receipt_counter


def verify_items(item_unit_price, item_quantity):
    # Validates single item bounds during the loop
    return item_unit_price > 0 and 1 <= item_quantity <= MAX_QTY_PER_ITEM


def bulk_discount_percent(total_discount):
    if total_discount >= 10000:
        return 10
    if total_discount >= 5000:
        return 5
    if total_discount >= 2000:
        return 2
    if total_discount >= 1000:
        return 1
    else:
        return 0


def membership_discount(tier):
    match tier.lower():
        case "g":
            return 5
        case "s":
            return 2
        case _:
            return 0


def tier_name(tier):
    match tier.lower():
        case "g":
            return "Gold"
        case "s":
            return "Silver"
        case _:
            return "Regular"


# --- Session 4 Currency Breakout ---
def denomination_of_currency(change):
    print("Change: Rs", change)
    # Fixed the previous sequence typo from your code (10000 -> 1000)
    denominations = [5000, 1000, 500, 100, 50, 10, 5, 2, 1]
    remaining_change = change
    for denomination in denominations:
        count = remaining_change // denomination
        if count > 0:
            if denomination >= 10:
                print(f" Rs {denomination} x {count}")
            else:
                print(f" Coins Rs {denomination} x {count}")
            remaining_change %= denomination


# --- Session 4 Receipt Body Formatting ---
def print_receipt(
    customer,
    item_count,
    subtotal_price,
    discount_percent,
    discount_price,
    gst_price,
    total,
    tier,
    cashier,
):
    receipt_no = receipt_no_counter()
    print()
    print_line("-", 42)
    print(f"Receipt No : {receipt_no} | Cashier: {cashier}")
    print(f"Customer   :- {customer}")
    print(f"Items      :- {item_count}")
    print(f"Subtotal   :- Rs {subtotal_price:.1f}")
    if discount_percent > 0:
        print(f"Discount   :- - Rs {discount_price:.1f} ( {discount_percent} % )")
    print(f"gst_price  :- Rs {gst_price:.1f}")
    print(f"total      :- Rs {total}")
    print_line("-", 42)


# --- Step 1: Draw lines with a for loop ---
def print_line(char, length):
    """Draw a line using a for loop and range()."""
    for i in range(length):
        print(char, end="")
    print()


def show_banner():
    print_line("=", 42)
    print(f"{MART_NAME:^42}")
    print_line("=", 42)


# --- Step 2: Cashier login with three attempts (while-else) ---
def login():
    """Allow 3 PIN attempts.

    while-else runs 'else' if no break happened.
    """
    attempts = 0
    while attempts < MAX_PIN_ATTEMPTS:
        pin = input("Enter cashier PIN: ")
        if pin == CASHIER_PIN:
            print("Login successful.")
            break
        attempts = attempts + 1
        print("Wrong PIN.", MAX_PIN_ATTEMPTS - attempts, "attempt(s) left.")
    else:
        print("Too many wrong attempts. System locked.")
        return False
    return True


# --- Step 4: Keep asking until the cash is enough ---
def collect_cash(total):
    """Keep asking until the customer gives enough cash."""
    while True:
        cash = int(input("Cash received (Rs): "))
        if cash >= total:
            return cash
        print("Not enough! Short by Rs", total - cash, "- try again.")


# --- Step 3: Many items per customer (sentinel loop) ---
def process_sale(cashier):
    """Add many items until the cashier types 'done'.

    Returns the bill total.
    """
    customer = input("Enter the customer name :- ")
    tier = input("Membership Gold, Silver, Enter = None :- ")

    subtotal_val = 0
    item_count = 0

    print("Enter items. Type done as the product name to finish.")
    while True:
        item_name = input(" Product name: ")
        if item_name.lower() == "done":
            break

        unit_price = float(input(" Unit price :- "))
        quantity = int(input(" Enter the items quantity :- "))

        # Integration of verify_items with the 'continue' keyword to skip items
        if not verify_items(unit_price, quantity):
            print(
                f" invalid price or quantity (allowed 1 - {MAX_QTY_PER_ITEM}) - item skipped."
            )
            continue  # Skips this item and returns to the top of the loop

        line_total = subtotal(unit_price, quantity)
        subtotal_val = subtotal_val + line_total
        item_count = item_count + quantity

        print(
            f" Added: {item_name} {quantity} x {unit_price} = {line_total} | Running subtotal: {subtotal_val}"
        )

    if item_count == 0:
        print("No items entered. Sale cancelled.")
        return 0

    # Calculate global totals using your Session 4 discount & tax logic
    total_discount_percent = bulk_discount_percent(
        subtotal_val
    ) + membership_discount(tier)
    discount_value = subtotal_val * total_discount_percent / 100
    after_discount_value = subtotal_val - discount_value
    gst_value = gst(after_discount_value)
    total_payable = calculating_total(after_discount_value, gst_value)

    # Display receipt structure
    print_receipt(
        customer,
        item_count,
        subtotal_val,
        total_discount_percent,
        discount_value,
        gst_value,
        total_payable,
        tier,
        cashier,
    )

    # Indefinite payment collection loop
    cash_received = collect_cash(total_payable)
    due_cash = cash_received - total_payable

    if due_cash > 0:
        denomination_of_currency(due_cash)

    print("payment received Thank you !")
    return total_payable


# --- Step 6: A price table with nested loops ---
def show_price_table():
    """Nested loops: a quick quantity x price reference table."""
    print("Qty", end="\t")
    for price in range(100, 600, 100):
        print("Rs", price, end="\t")
    print()

    for qty in range(1, 6):
        print(qty, end="\t")
        for price in range(100, 600, 100):
            print(qty * price, end="\t")
        print()


def store_info():
    print_line("-", 30)
    print("---Store information---")
    print(f"Mart Name    :- {MART_NAME}")
    print(f"Mart Address :- {MART_ADDRESS}")
    print(f"Mart Phone   :- {MART_PHONE}")
    print(f"GST Rate     :- {GST_RATE * 100:.0f}%")
    print_line("-", 30)


# --- Step 5: The main menu loop and day totals ---
def main():
    show_banner()
    if not login():
        return

    cashier = input("Enter the cashier name :- ")
    sales_count = 0
    day_revenue = 0

    while True:
        print()
        print("===== MAIN MENU =====")
        print("1. New Sale")
        print("2. Day summary")
        print("3. Price table")
        print("4. Store information")
        print("5. Close the till (exit)")

        choice = input("Choose an option :- ")
        match choice:
            case "1":
                total = process_sale(cashier)
                if total > 0:
                    sales_count = sales_count + 1
                    day_revenue = day_revenue + total
            case "2":
                # Guard statement to prevent ZeroDivisionError
                print_line("-", 30)
                if sales_count > 0:
                    avg_bill = day_revenue / sales_count
                    print(f"Sales today : {sales_count}")
                    print(f"Revenue     : Rs {day_revenue}")
                    print(f"Average bill: Rs {avg_bill:.1f}")
                else:
                    print("Sales today : 0")
                    print("Revenue     : Rs 0")
                    print("Average bill: Rs 0.0")
                print_line("-", 30)
            case "3":
                show_price_table()
            case "4":
                store_info()
            case "5":
                print(
                    f"Till closed. Sales: {sales_count} | Revenue: Rs {day_revenue}"
                )
                print(f"Good Bye, {cashier}")
                break
            case _:
                print("Invalid option, try again.")


if __name__ == "__main__":
    main()
