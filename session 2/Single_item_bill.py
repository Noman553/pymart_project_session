# ===========================================================================
# PyMart - Grocery Store Management and Billing System
# season 2 : Hello , FrenchMart
# Author : <Noman Mehmood>


# -------------- let's add the constants first for our mart so they will remain same --------------------------
STORE_NAME = "FrenchMart"
STORE_ADDRESS = "District Mandi Bahaudin Tehseel Malakwal jinnah road"
GST_RATE = 0.18

# --------------------- let's try Multiple assigment : means you can add two variable or more in one line --------------------------------
counter_no , version = 1 , "0.2"
# --------------- Store Banner ------------------------
print("======================================================")
print("-------------------------- French Mart----------------")
print("   District Mandi Bahaudin Tehseel Malakwal jinnah road    ")
print(" ======================================================")
print("Counter No:" , counter_no , "| version : " , version)

# -------------------------- now the next part is to add the sale details like casher name and customer name --------------------------------
cashier = input("Cashier Name : ")
customer_name = input("Customer Name :")
item_name = input("Item Name : ")
unit_price = float(input("Unit Price :"))
items_quantity =    int(input("Items Quantity :"))

# ---------------------------- next step is to calculate the bill ------------------------------------
subtotal = unit_price * items_quantity
gst_total = subtotal * GST_RATE
total = subtotal + gst_total
total_rounded = round(total)
print("subtotal:" , subtotal)
print("The gst is 0.18% :" , gst_total)
print("total payable " , total_rounded)

# ----------------------------- now Let's work on cash receiving the cash and change -------------------
cash_received = int(input("cash Received (RS) :"))
change = cash_received - total_rounded
print("Change to return :" , change)

# ------------------------- now break the change into notes -----------------------------------
notes = {5000 , 1000 , 500 , 100 , 50 , 10 }
for note in notes:
    count = change // note
    remaining_change = change % note
    print(f"Rs{note} note:{count}")

