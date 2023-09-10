# assignment 14 vg task
monthly_Income = float(input("Please provide monthly income: "))    # get monthly income

# defien our tax values
tax = 0.3
additional_tax1 = 0.05
additional_tax2 = 0.1

# define our thresholds
threshold1 = 38000
threshold2 = 50000

# calcualate apropriate income after tax
if monthly_Income < 0:
    print("Monthly income can't be negative!")
else:
    if monthly_Income < threshold1:
        monthly_Income = monthly_Income * tax   # 30% tax
    elif threshold1 < monthly_Income < threshold2:
        monthly_Income = monthly_Income * (tax + additional_tax1)   # 35% tax
    elif monthly_Income > threshold2:
        monthly_Income = monthly_Income * (tax + additional_tax2)   # 40% tax

    print(f"You income tax is: {int(monthly_Income)} sek.")