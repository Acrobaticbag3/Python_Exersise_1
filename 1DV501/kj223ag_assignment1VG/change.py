# assignment 8
# Function
def check_Amount(change):
    int_Bill_Value = {1000, 500, 200, 100, 50, 20}  # Bill values 
    int_Coin_Value = {10, 5, 2, 1}                  # Coin values

    # loop through our bill array and see what values we get
    for element in int_Bill_Value:
        try:
            if change >= element:   # check that change is bigger than or == element value 
                change -= element
                print(element, "bills:", 1)
        except:
            print("There was an exception!")
    
    # loop through our coin array and see what values we get
    while change != 0:             # Lloop through as long as change != 0 
        for idex in int_Coin_Value:     
            try:
                if change >= idex:  # check that change is bigger than or == elemental value 
                    change -= idex
                    print(idex, "Coins:")
            except:
                print("There was an exception!")


# Main program
price = int(input("Price: "))
payment = int(input("Payment: "))

change = payment - price
check_Amount(change)