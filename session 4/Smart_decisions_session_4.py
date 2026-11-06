# PyMart - Smart Decisions
# session 4 : Hello , FrenchMart
# Author : <Noman Mehmood>

import math
# Mart Information
MART_NAME = "French Mart"
MART_ADDRESS = "Malakwal Jinnah road"
MART_PHONE = "03486120924"
GST_RATE = 0.18
MAX_QYT_PER_ITEM =  100
# Receipt counter
receipt_counter = 0 # it will help us to count how many receipt have been generated


# let's calculate the Subtotal
def subtotal (items_unite_price , items_quantity) :
    return items_unite_price * items_quantity

# calculating the gst
def gst(subtotal_amount , rate = GST_RATE) :
     return subtotal_amount * rate

def calculating_total(amount , calculate_gst):
    return math.ceil(amount+calculate_gst)

# creating the receipt counter
def receipt_no_counter():
   global receipt_counter
   receipt_counter = receipt_counter + 1
   return receipt_counter


#validate the items to see that the product quantity is valid or not
def verify_items(item_unit_price , item_quantity):
    return item_unit_price > 0 < item_quantity <= 100

# function that will be used for build discount means more purchase means more discount
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

# customer memberShip discount

def membership_discount(tier):
    # keep the tier in lower case so if the customer add the membership in uppercase our machine will still be able to understand
   lower_case_tier = tier.lower()
   match lower_case_tier:
       case "g" :
        return 5
       case "s":
           return 2
       case _:
           return 0
# function that will convert the tier into full name like if the customer enter the g it will return gold and if customer enter the s it will return silver
def tier_name(tier):
    match tier:
        case "g" :
            return "Gold"
        case "s" :
            return "Silver"
        case _:
            return "Regular"

# denomination of currency
def denomination_of_currency(change):
    # printing the change
    print("Change :" , change)
    denominations =  [5000, 1000, 500, 100, 50, 10, 5, 2, 1]
    remaining_change = change
    for denomination in denominations :
        count = remaining_change // denomination
        if count > 0:
            if denomination >= 10 :
                print(f"Rs {denomination} x {count}")
            else:
                print(f"Coins {denomination} x {count}")
        remaining_change %= denomination


# organizing thing in receipt function
def print_receipt(customer , items_name , unit_price , quantity , subtotal_price , discount_percent , discount_price , gst_price , total , tier , * , cashier = "counter 1") :
    receipt_no = receipt_no_counter()
    full_tier_title = tier_name(tier)
    print(f"------------------{MART_NAME}---------------------")
    print(f"------------------{MART_ADDRESS}------------------")
    print("Receipt No :- " , receipt_no)
    print("Customer Name :- " , customer)
    print("Cashier Name :-" , cashier)
    print("--------------------------------------------")
    print("items_name :- " , items_name)
    print("unit_price :- " , unit_price)
    print("quantity :- " , quantity)
    print("---------------------------------------------")
    print("subtotal_price :- " , subtotal_price)
    if discount_percent > 0:
        print(f"discount {discount_percent}% :- Rs {discount_price:.1f}")

    print(f"gst_price :-  , {gst_price :.1f}")
    print("total :- " , total)

def process_sale(cashier):
   customer = input("Enter the customer name :- ")
   tier = input("Membership Gold , Silver , Enter = None :- ")
   items_name = input("Enter the Items Name :- ")
   item_unit_price = float(input("Enter the per unit price :- "))
   item_quantity = int(input("Enter the items quantity :- "))

   if not verify_items(item_unit_price , item_quantity):
       print(f"invalid price or quantity (allowed 1 - {MAX_QYT_PER_ITEM})")
       print("Sale Cancelled")
       return
   subtotal_val = subtotal(item_unit_price , item_quantity)
   total_discount_percent = bulk_discount_percent(subtotal_val) + membership_discount(tier)
   discount_value = subtotal_val * total_discount_percent/100
   after_discount_value = subtotal_val - discount_value
   gst_value = gst(after_discount_value)
   total_payable = calculating_total(after_discount_value , gst_value)

   print_receipt(customer, items_name, item_unit_price, item_quantity, subtotal_val, total_discount_percent, discount_value, gst_value, total_payable, tier, cashier = cashier  )

   # let's handle the incoming payments
   cash_received = int(input("Enter the received cash (RS:) :-  "))
   if cash_received >= total_payable :
       due_cash = cash_received - total_payable
       if due_cash > 0:
           denomination_of_currency(due_cash)
       print("payment received Thank you !")
def store_info():
    print("--------------------Store information-------------------")
    print(f"Mart Name :- {MART_NAME} ")
    print(f"Mart Address :- {MART_ADDRESS} ")
    print(f"Mart Address :- {MART_PHONE} ")
    print(f"GST Rate :- {GST_RATE * 100}%")

def main() :
    print(f"---------------- Welcome to the {MART_NAME} ----------------")
    cashier = input("Enter the cashier name :- ")
    print("\n1. New Sale")
    print("2 store information")
    print("Exit")
    choice = input("Choose an option :-")
    match choice :
        case "1" :
             process_sale(cashier)
        case "2" :
            store_info()
        case "3" :
            print(f"Good Bye , {cashier}")
        case _ :
            print("invalid option")
    if __name__ == "__main__":
        main()
main()






