height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(float(weight)/(float(height)*float(height)))

print(bmi)

print("Your BMI is " + str(bmi) + ".")