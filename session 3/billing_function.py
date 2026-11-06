# ===========================================================================
# PyMart - Grocery Store Management and Billing System
# season 3 : Hello , FrenchMart
# Author : <Noman Mehmood>

# import Single_item_bill
import math

# ----------- store constants -----------
STORE_NAME = "FrenchMart"
STORE_ADDRESS = "District Mandi Bahaudin Tehseel Malakwal jinnah road"
GST_RATE = 0.18
PROMO_PERCENT = 2
receipt_counter = 0


# ---------- now let's see about the lambda a tiny one line function --------------
apply_discount = lambda amount , percent : amount - amount * percent / 100



print("=========================================================")
print("======================== French Mart ===================")
print("======================= Best Grocery Store ======================")
print(" Address : District Mandi Bahaudin Tehseel Malakwal jinnah road ")
print("Phone : 03485533445")
print("hours : 9:00 am - 11:00pm (7days)")
print("----------------------------------------------------")
print("system : Mart Billing version v0.1 (Season 3)")
print("system : Mart Billing version v0.1 (Season 3)")

#---------------------------------- now let's create the calculation function -------------------------------
print("=============== calculate the subtotal ========================")
def calculate_subtotal(unit_price , quantity):
    print("========== for calculating the subtotal =============")
    return unit_price * quantity


print(calculate_subtotal(200 , 3))





