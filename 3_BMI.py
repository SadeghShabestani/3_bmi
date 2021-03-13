import termcolor2

weight = float(input("Enter Weight: "))
height = float(input("Enter Height: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(termcolor2.colored(f"Condition: {bmi} Underweight", color="blue"))
elif 18.5 <= bmi <= 24.9:
    print(termcolor2.colored(f"Condition: {bmi} Normal", color="green"))
elif 25 <= bmi <= 29.9:
    print(termcolor2.colored(f"Condition: {bmi} Overweight", color="yellow"))
elif 30 <= bmi <= 34.9:
    print(termcolor2.colored(f"Condition: {bmi} Obese", color="orange"))
elif 35 >= bmi:
    print(termcolor2.colored(f"Condition: {bmi} Extremely Obese", color="red"))
