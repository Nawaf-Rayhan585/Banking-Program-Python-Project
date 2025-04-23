import datetime

card_num = input('please add your card number to make an account: ')
name = input('please add your name: ')
age = input('please add your age: ')
createdAt = datetime.datetime.now()

balance = 0
int(balance)

def action_msg():
    print("press 1: deposit")
    print("=====================")
    print("press 2: withdraw")
    print("=====================")
    print("press 3: show balance")
    print("=====================")
    print("press 4: account details")
    print("=====================")
    print("type currency: check currency")
    print("=====================")
    print("press q: quit")
    print("=====================")

def check_card_number():

    check_card_num = input("please verify by giving card number: ")
    if check_card_num == card_num:
        print('verification success!')
        print("")
    else:
        print('sorry try again next time:')
        print("")
        check_card_number()



def deposit():
    global balance
    check_card_number()
    new_balance = input("please put the amount you want to deposit $: ")
    balance = balance + int(new_balance)
    print("you have $", balance)
    print("")


def withdraw():
    global balance
    check_card_number()
    withdraw_amount = input("please put the amount you want to withdraw $: ")
    if int(withdraw_amount) <= balance:
        balance = balance - int(withdraw_amount)
        print("you have withdrawn $", withdraw_amount)
        print("your new balance is $", balance)
        print("")
    else:
        print("not enough balance!")
        print("")


def acc_details():
    check_card_number()
    print("Name:", name)
    print("=====================")
    print("Age:", age)
    print("=====================")
    print("card number:", card_num)
    print("=====================")
    print("account created on:", createdAt)
    print("=====================")

def currency():
    print("Currency Conversion (from USD)")
    print("Available currencies: bdt, aud, inr, eur")
    print("Type 'back' to return to the main menu.\n")

    # Set up exchange rates (can be updated)
    exchange_rates = {
        "bdt": 120,
        "aud": 1.52,
        "inr": 83,
        "eur": 0.91
    }

    while True:
        curr_name = input("Enter currency code (bdt/aud/inr/eur) or 'back': ").lower()
        if curr_name == "back":
            break
        elif curr_name in exchange_rates:
            amount_usd = input("Enter amount in USD: ")
            try:
                usd_val = float(amount_usd)
                converted = usd_val * exchange_rates[curr_name]
                print(f"{usd_val} USD is approximately {converted:.2f} {curr_name.upper()}")
                print(f"Your current balance in {curr_name.upper()}: {balance * exchange_rates[curr_name]:.2f}\n")
            except ValueError:
                print("Please enter a valid number for amount.\n")
        else:
            print("Invalid currency code. Try again.\n")




def main():

    action_msg()
    input(f"Good Morning, {name} , what do you want to do today? please press ENTER to proceed")
    action = input("1: deposit, 2: withdraw, 3: show balance, 4:account details, Q: quit, enter action: ")
    if action == "1":
        deposit()
        action = input("1: deposit, 2: withdraw, 3: show balance, 4:account details, Q: quit, enter action: ")

    if action == "2":
        withdraw()
        action = input("1: deposit, 2: withdraw, 3: show balance, 4:account details, Q: quit, enter action: ")

    if action == "3":
        print(f"your current balance is:", balance)
        action = input("1: deposit, 2: withdraw, 3: show balance, 4:account details, Q: quit, enter action: ")

    if action == "4":
        acc_details()
        action = input("1: deposit, 2: withdraw, 3: show balance, 4:account details, Q: quit, enter action: ")

    if action == "currency":
        currency()
        action = input("1: deposit, 2: withdraw, 3: show balance, 4:account details, Q: quit, enter action: ")


    if action == "q":
        print("thanks for using our service")
        exit()


main()
