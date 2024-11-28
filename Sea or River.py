print("Shoopkeeper - How can I help you? ")

print("Customer - I am going fishing, so I want to buy a fishing hook. ")

point_estination = input("Shopkeeper - Tell me, where are you going for fishing (river or sea)? ")

with_friends = input("Shopkeeper - Are you going along with your friends (yes/no)? ")

how_far = input("Shopkeeper - Is this area far away from the city (yes/no)? ")

wants_to_buy = input("Do you want to buy a fishing hook? ")

print("Shoopkeeper - Okay, so you want a fishing hook. ")

hook_type = input("Shoopkeeper - Which type of hook do you want? Enter the type: ")

print(f"Customer - Do you have a {hook_type} type of hook? ")

while True:
    stock_check = input("Customer - Is the hook available \nShoopkeeper: (yes/no)? ")
    for stock_check in [stock_check.lower()]:
        if stock_check == "yes":
            for stock_check in range(1):
                hook_quantity = int(input("Shoopkeeper - Tell me how many hooks do you want to buy? "))
                print(f"Shoopkeeper - Here is your {hook_quantity} {hook_type} hooks. ")
                break   # exit inner loop
            break       # exit outer loop
        else:
            print("Shoopkeeper - Sorry, the hooks aren't available. ")
            break       # exit unavailable loop
    break               # exit from the entire loop

rod = input("Shopkeeper - Do you need a fishing stick/rod as well (yes/no)? ")

rod = input("Do you want to buy a fishing rod? (yes/no): ")

if rod.lower() == "yes":
    rod_buy = input("Shopkeeper - Tell me, do you want to buy a fishing rod? (yes/no): ")
    if rod_buy.lower() == "yes":
        quantity = int(input("Shopkeeper - How many fishing rods do you want to buy? "))
        rod_type = input("Shopkeeper - Which type of fishing rod do you want (metal, bronze, plastic, aluminum)? ")

        color_rod = input("Do you want a colored rod? (yes/no): ")
        if color_rod.lower() == "yes":
            rod_color = input("Which color do you want? ")
            print(f"Shopkeeper - Here is your {rod_color} {rod_type} rod. Quantity: {quantity}. ")
        else:
            print(f"Shopkeeper - Here is your standard {rod_type} rod. Quantity: {quantity}. ")
    else:
        print("Shopkeeper - Okay, let me know if you change your mind. \n")
else:
    print("Customer - I will use my friend's fishing rod. ")
    print("Shopkeeper - If your friend doesn’t bring the rod, what would you use? \n")
    print("Customer - Okay, tell me which type of rod you have. ")
    print("Shopkeeper - I have rods in metal, bronze, plastic, and aluminum. ")

    rod_type = input("Which type of rod do you want to buy (metal, bronze, plastic, aluminum): ")
    color_rod = input("Do you want a colored rod? (yes/no): ")
    if color_rod.lower() == "yes":
        rod_color = input("Which color do you want? ")
        print(f"Shopkeeper - Here is your {rod_color} {rod_type} rod. ")
    else:
        print(f"Shopkeeper - Here is your {rod_type} rod. ")

wants_to_buy_boat = input("Shopkeeper - Do you also want to buy a boat (yes/no)? ")

if wants_to_buy_boat.lower() == "yes":
    boat_size = input("Which size of boat do you want (small/medium/large)? ")
    if boat_size.lower() == "small":
        boat_color = input("Which color do you want for the small boat? ")
        print(f"Shopkeeper - Your {boat_color} small boat is ready. ")
    elif boat_size.lower() == "medium":
        boat_color = input("Which color do you want for the medium boat? ")
        print(f"Shopkeeper - Your {boat_color} medium boat is ready. ")
    elif boat_size.lower() == "large":
        boat_color = input("Which color do you want for the large boat? ")
        print(f"Shopkeeper - Your {boat_color} large boat is ready. ")
else:
    print("Okay, fine. ")

# Bank account
print("Shopkeeper - You are going out of the city, so you need much cash for it. Do you have enough cash for spending there? \n")

is_atm_available = input("Is there any ATM machine there (yes/no)? ")

if is_atm_available.lower() == "yes":
    account_available = input("Do you have any bank account? (yes/no) ")
    if account_available.lower() == "no":
        open_bank_account = input("Shopkeeper - Do you want to open a bank account? (yes/no) ")
        if open_bank_account.lower() == "yes":
            print("Shopkeeper - Okay, let's proceed with opening your bank account. ")
            full_name = input("Tell me your full name: ")
            your_number = input("Tell me your number: ")
            your_number = input("Is your number registered on your name (yes/no): ")
            if your_number.lower() == "no":
                print("Okay, I converted it to your number. ")
            elif your_number.lower() == "yes":
                print("It's perfect. ")
            your_nic = input("Tell me your NIC number: ")
            guardian_nic = input("Tell me your guardian's NIC number: \n")
            age = input("Tell me your age: \n\n")
            print("__________YOUR ACCOUNT IS SUCCESSFULLY OPENED__________ \n")
            print("Your IBAN number is: DE44 1234 1234 1234 1234 00 \n")
            print("Your account number is: 123456789012 \n")
        else:
            print("Shopkeeper - Okay, let's move on. ")
    else:
        print("Shopkeeper - You already have a bank account. ")
else:
    print("Shopkeeper - There is no ATM machine available. ")

print("Shoopkeeper - So now it's time for billing. ")

# Total (metal, bronze, plastic, aluminum)
# Prices for hooks, rods, and boats
hook_price = 100
metal_rod_price = 1000
bronze_rod_price = 100
plastic_rod_price = 700
aluminum_rod_price = 850
small_boat_price = 10000
medium_boat_price = 15000
large_boat_price = 20000
total_bill = 0

# Hook purchase input
hook_quantity = int(input("How many hooks did you buy? "))
hook_total_cost = hook_price * hook_quantity
total_bill += hook_total_cost

# Rod purchase input
rod_buy = input("Did you buy a rod? (yes/no): ").lower()

# Initialize rod_total_cost as 0
rod_total_cost = 0

if rod_buy == "yes":
    rod_type = input("Which type of rod did you buy (metal, bronze, plastic, aluminum)? ").lower()
    rod_quantity = int(input("How many rods did you buy? "))
    
    if rod_type == "metal":
        rod_total_cost = metal_rod_price * rod_quantity
    elif rod_type == "bronze":
        rod_total_cost = bronze_rod_price * rod_quantity
    elif rod_type == "plastic":
        rod_total_cost = plastic_rod_price * rod_quantity
    elif rod_type == "aluminum":
        rod_total_cost = aluminum_rod_price * rod_quantity
    else:
        print("Invalid rod type entered. Please enter a valid rod type (metal, bronze, plastic, or aluminum).")
    
    total_bill += rod_total_cost

# Boat purchase input
boat_quantity = int(input("How many boats did you buy? "))
boat_size = input("Which size of boat did you buy (small/medium/large)? ").lower()

if boat_size == "small":
    total_bill += small_boat_price * boat_quantity
elif boat_size == "medium":
    total_bill += medium_boat_price * boat_quantity
elif boat_size == "large":
    total_bill += large_boat_price * boat_quantity
else:
    print("Invalid boat size entered. Please enter small, medium, or large.")

# Final bill output
print(f"Your total bill is: ${total_bill}.")
print("Shopkeeper - Thank you for your purchase! Have a great day and enjoy your fishing trip!")
