# this is shopping cart code
# dict for storing the stock
mensSection = {"Shirt" : 200  , "Hoodie" : 1102}
womenSection = {"saree" : 2000 , "dress" : 1000}
childSection = {"shirt":500}
Basket = {}


# Functions.......
def sel_first():
  print("-------Welcome to SourceKode Mall---------")
  print("-------WElcome to Seller Portal---------")
  print("\n\n\n")
  b=int(input(print("enter 1 for login & enter 2 for sign up")))
  if b==1:
     sel_login()
  else:
     sel_signup()


def sel_login(seller_name,seller_password):
  print("Welcome to SourceKode Mall")
  print("\n\n")
  print("-------------LOGIN------------")
  print("\n\n")
  s_name = input("Seller name : ")
  s_pass = input("Password : ")
  if s_name==seller_name and s_pass==seller_password :
     sel_greet(seller_name)
  else:
    sel_signup()


def sel_signup():  
  print("Welcome to SourceKode Mall")
  print("\n\n")
  print("-------------SIGN UP------------")
  print("\n\n")
  print("Seller details:-")
  seller_name = input("Please enter your name : ")
  seller_phno = int(input("Please enter 10 digit mob. no : "))
  seller_address = input("Please enter your address : ")
  seller_pincode = input("Please enter your pincode : ")
  seller_email = input("Please enter your email id : ")
  seller_password = input(("Please enter password : "))
  print("\n\n")
  print("Login for listing your product")
  sel_login(seller_name,seller_password)


def sel_greet(name):
    print("enter 1->men's section 2->women's section 3->child section ")
    choice = int(input("enter your choice"))
    if choice==1:
      men_update()
    elif choice==2:
      women_update()
    elif choice==3:
      child_update()
    else:
      print("incorrect choice")


def men_update():
  print("--------Update Men's Section----------")
  print("\n\n")
  print("Add new items:")
  print("\n\n")
  item_name = input("enter new item name")
  item_price = int(input("enter item price"))

  mensSection[item_name] = item_price

  item_to_delete = input("enter item name to delete")
  mensSection.pop(item_to_delete)

  print("---------------Updated Men's Section---------------")   
  print(mensSection) 


def women_update():
  print("--------Update Women's Section----------")
  print("\n\n")
  print("Add new items:")
  print("\n\n")
  item_name = input("enter new item name")
  item_price = int(input("enter item price"))

  womenSection[item_name] = item_price

  item_to_delete = input("enter item name to delete")
  womenSectionSection.pop(item_to_delete)
  print("---------------Updated Women's Section---------------")   
  print(womenSection) 

def child_update():
  print("--------Update Kids Section----------")
  print("\n\n")
  print("Add new items:")
  print("\n\n")
  item_name = input("enter new item name")
  item_price = int(input("enter item price"))

  childSection[item_name] = item_price

  item_to_delete = input("enter item name to delete")
  childSection.pop(item_to_delete)
  print("---------------Updated Kids Section---------------")   
  print(childSection) 


def cus_first():
  print("-------Welcome to SourceKode Mall---------")
  print("-------WElcome to Customer Portal---------")
  print("\n")
  b=int(input(print("enter 1 for login & enter 2 for sign up")))
  if b==1:
     login()
  else:
     signup()


def login():
  print("Welcome to SourceKode Mall")
  print("\n\n")
  print("-------------LOGIN------------")
  print("\n\n")
  c_name = input("Customer name : ")
  c_pass = input("Password : ")
  if c_name==name and c_pass==password :
     firstpg(name)
  else:
    signup()


def signup():  
  print("Welcome to SourceKode Mall")
  print("\n\n")
  print("-------------SIGN UP------------")
  print("\n\n")
  print("Customer details:-")
  name = input("Please enter your name : ")
  customer_phno = int(input("Please enter 10 digit mob. no : "))
  customer_address = input("Please enter your address : ")
  customer_pincode = input("Please enter your pincode : ")
  customer_email = input("Please enter your email id : ")
  password = input("Please enter password : ")
  print("\n\n")
  print("Login for Shopping")
  login()


def women(Basket,name):
  for i in womenSection:
    print(f"Item : {i} , Price: {womenSection[i]}")

  new_item = input("enter item name to buy :")
  Basket[new_item] = womenSection[new_item]
  print("\n\n")
  ch = int(input("enter 0 to move to main menu or 1 to continue Women Shopping"))
  if ch==0:
    greet(name)
  else:
    women(Basket,name)


def child(Basket,name):
  for i in childSection:
    print(f"Item : {i} , Price: {childSection[i]}")

  new_item = input("enter item name to buy :")
  Basket[new_item] = childSection[new_item]
  print("\n\n")
  ch = int(input("enter 0 to move to main menu or 1 to continue Child Shopping"))
  if ch==0:
    greet(name)
  else:
    child(Basket,name)


def men(Basket,name):
  for i in mensSection:
    print(f"Item : {i} , Price: {mensSection[i]}")

  new_item = input("enter item name to buy :")
  Basket[new_item] = mensSection[new_item]
  print("\n\n")
  ch = int(input("enter 0 to move to main menu or 1 to continue Men Shopping"))
  if ch==0:
    greet(name)
  else:
    men(Basket,name)

def cart( Basket,name):
    print("\n\n............Cart........\n\n")

    for i in Basket:
       print(f"item Name : {i}  ,  Price :  {Basket[i]}")

    print("\n\n")

    C = int(input("enter 1 for checkout and 0 for main menu"))
    if C==1:
      checkout(Basket,name)
    else:
      greet(name)

def checkout(Basket,name):
    print("\n\n\n ........... Checkout...............\n\n")

    total_amount = 0
    for i in Basket:
      print(f"Item bought : {i}  Price : {Basket[i]}")
      total_amount = total_amount + Basket[i]
    print("\n\n\n\n")


    print(f"Total Payable Amount  = {total_amount} \n\n\n")

    print(f"Thankyou {name} for Shopping with Us!!")

def exit(name):
  print("\n\n Exit.....Thankyou for visiting \n\n")
  print(f"See yaa {name}")


def greet(name):
    print("enter 1->men 2->women 3->child 4->checkout 5-> cart 6->exit")
    choice = int(input("enter your choice"))

    if choice==1:
      men(Basket,name)
    elif choice==2:
      women(Basket,name)
    elif choice==3:
      child(Basket,name)
    elif choice==4:
      checkout(Basket,name)
    elif choice==5:
      cart(Basket,name)
    elif choice==6:
      exit(name)
    else:
      print("incorrect choice")


def firstpg(name):
 print("Welcome to SourceKode shopping Mall")
 print("\n\n")
 print(f"Welcome {name}")
 print("\n\n")
 greet(name)

# This is the beginning of the project
print("Welcome to SourceKode Mall")
print("\n")
name=input("Enter name :\n")
password=input("Enter password to be generated :\n")
b=int(input(print("enter 1 for customer portal & enter 2 for seller portal")))
if b==1:
  cus_first()
else:
  sel_first()










