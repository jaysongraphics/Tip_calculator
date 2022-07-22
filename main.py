
print('Welcome to the tip calculator!')

bill = float(input("What was your total bill? \n"))

tip = int(input("How much would you like to give % ? [10, 12, or 15]? \n"))

people = int(input("How many people to split the bill? \n"))

tip_percentage = tip / 100
# print('tip percentage', tip_percentage)

total_tip = bill * tip_percentage
# print('total tip', total_tip)

total_bill = bill + total_tip
# print('total bill', total_bill)

bill_per_person = total_bill / people
# print('bill per person', bill_per_person)

total = round(bill_per_person, 2)
total = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${total}")