import math

# Mart Information
MART_NAME = "French Mart"
MART_ADDRESS = "Malakwal Jinnah road"
GST_RATE = 0.18
PROMO_PERCENT = 2 # It means a mart is offering 2 percent discount on all purchase

# Receipt counter
receipt_counter = 0 # it will help us to count how many receipt have been generated

# it time for applying discount
apply_discount  = lambda amount , percent : amount - (amount *percent/100)

# let's calculate the Subtotal
def subtotal (unite_price , quantity) :
    return unite_price * quantity

# calculating the gst
def gst(amount , rate = GST_RATE) :
     return amount * rate

def calculating_total(amount , calculate_gst):
    return math.ceil(amount+calculate_gst)

# creating the receipt counter
def receipt_no_counter():
   global receipt_counter
   receipt_counter = receipt_counter + 1
   return receipt_counter

# taking input from the user
customer_name = str(input("Customer Name :-"))
cashier_name = str(input("cashier Name :-"))
item_name = str(input("Enter the item name :- "))
per_piece_price = float(input("Enter the per item price :-"))
items_quantity = int(input("Enter the quantity of items :- "))
discount_on_per_discount = float(input("Enter the discount item :-"))

# calculation
discounted_price = apply_discount(subtotal(per_piece_price , items_quantity) , discount_on_per_discount )
gst_amount = gst(discounted_price)
final_price = calculating_total(discounted_price , gst_amount)


# organizing thing in receipt function
def print_receipt(customer , items_name , unit_price , quantity , subtotal_price , discount_price , gst_price , total , * , cashier = "counter 1") :
    receipt_no = receipt_no_counter()
    print(f"------------------{MART_NAME}---------------------")
    print(f"------------------{MART_ADDRESS}------------------")
    print("receipt no :-" , receipt_no)
    print("Customer :- " , customer)
    print("Cashier Name :-" , cashier)
    print("--------------------------------------------")
    print("items_name :- " , items_name)
    print("unit_price :- " , unit_price)
    print("quantity :- " , quantity)
    print("---------------------------------------------")
    print("subtotal_price :- " , subtotal_price)
    print("discount_price :- " , round(discount_price , 2))
    print("gst_price :- " , round(gst_price , 2))
    print("total :- " , total)

print_receipt(
    customer_name ,
    item_name ,
    per_piece_price,
    items_quantity,
    subtotal(per_piece_price , items_quantity),
    discounted_price,
    gst_amount,
    final_price,
    cashier=cashier_name,
)






