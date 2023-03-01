print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip_amount = int(input("What percent would you like to tip? "))
no_people = int(input("How many people are splitting the bill? "))
tip_as_percent = tip_amount / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
amount_pp = total_bill / no_people
final_amount = "{:.2f}".format(amount_pp)

print(f"Each person should pay: £{final_amount}")