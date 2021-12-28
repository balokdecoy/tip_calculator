print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 12, 15, or 20? ")
people = int(input("how many people to split the bill? "))

tip_num = (int(tip) / 100) + 1

result = "{:.2f}".format((bill / people) * tip_num)

print(f"Each person should pay: ${result}.")