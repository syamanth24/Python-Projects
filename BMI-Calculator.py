height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

cal = weight/(height * height)

bmi = (round(cal))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 25 >= bmi > 18.5:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif  30 >= bmi > 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")  
elif 35 >= bmi < 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")