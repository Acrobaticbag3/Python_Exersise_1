# assignemnt 4
# Store all info and convert variables to usable info
s = int(input("Initial savings: "))
p = int(input("Interest rate (in percentages): "))
y = int(input("Number of years: "))

#Math
p = p / 100 + 1

for year in range(y):
  s = s * p

s = round(s)
print("The value of your savings after", y, "years is:", s)