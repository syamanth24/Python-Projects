#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Total_bill = 150

#Total_tip = Total_bill/12

#Total_cost = Total_bill + Total_tip

#bill_person = Total_cost/5

#print(round(bill_person, 2))

bill = input("what was the total bill: ")

tip = input("What percetage tip would you like to give? 10, 12, or 15: ")

people = input("How many people to split the bill? ")

tip_total = float(bill)/int(tip)

tip_person = float(tip_total)/float(people)

person_bill = (float(bill)/float(people)) + float(tip_person)

actual = round(person_bill, 2)

print(f"Each person should pay {actual} dollars.")
