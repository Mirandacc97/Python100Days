print("Welcome to the Tip Calculator.")
bill = float (input("What was the total bill? $"))
tip_percentage = int (input("What percentage tip would you like to give? 10, 12, or 15? "))
split_people = int (input("How many people to split the bill? "))

tip =  bill * (tip_percentage / 100)
total_bill = bill + tip
amount_per_person = total_bill / split_people

print("Each person should pay: ${:.2f}".format(amount_per_person))