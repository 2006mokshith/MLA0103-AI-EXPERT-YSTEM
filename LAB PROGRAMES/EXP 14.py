age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Diet: Protein and calorie-rich foods")
elif bmi < 25:
    print("Diet: Balanced healthy foods")
else:
    print("Diet: Balanced portions and more vegetables")
