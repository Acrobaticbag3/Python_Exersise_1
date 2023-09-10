# assignment 8 vg task
def check_Amount(change):
    int_Bill_Value = [1000, 500, 200, 100, 50, 20]  # List of bill values
    int_Coin_Value = [10, 5, 2, 1]                  # List of coin values

    change = round(change)  # round off the change to the nearest krona
    
    print(f"Change: {change} kr")

    for bill in int_Bill_Value:
        bill_count = change // bill # calculate how many times the current bill value can be used to make up the remaining change.
        if bill_count > 0:
            print(f"{bill}kr bills: {bill_count}")
            change -= bill_count * bill # keep track of the remaining change that is to be processed.

    for coin in int_Coin_Value:
        coin_count = change // coin # calculate how many times the current coin value can be used to make up the remaining change.
        if coin_count > 0:
            if coin >= 10:
                print(f"{coin}kr coins: {coin_count}")
            else:
                print(f"{coin}kr coins: {coin_count}")
            change -= coin_count * coin # keep track of the remaining change that is to be processed.

# get price and payment from user
price = float(input("Price: "))
payment = float(input("Payment: "))

change = payment - price

if payment < price:
    print(f"Payment of: {payment} is less than the price of: {price} \n you can't pay with that!")
elif price < 0 or payment < 0:
    print("The cost can't be negative!")
else:
    check_Amount(change)