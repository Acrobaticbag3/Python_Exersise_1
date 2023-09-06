# assignment 8
def check_Amount(change):
    int_bill_value = {1000, 500, 200, 100, 50, 20}  # array of ints 

    # for every element in arr 
    for element in int_bill_value:              
        if change % int_bill_value[element]:    # if change and element are devisable
            change - element                    #
            print(change, element)


price = int(input("Price: "))
payment = int(input("Payment: "))

change = payment - price
check_Amount(change)