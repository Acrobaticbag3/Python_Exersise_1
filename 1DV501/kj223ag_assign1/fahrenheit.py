# assignemnt 3

userInput = input("Provide a temperature in Fahrenheit: ")      # Takes user input
celsius  = float(userInput)                                     # Converts userInput to float
celsius = celsius - 32 
celsius = celsius * 5/9

print("Corresponding temperature in Celsius is: ", celsius)