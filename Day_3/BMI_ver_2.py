# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(float(weight)/(float(height)**2))
print(f"The BMI is {bmi}")
if bmi < 18.5:
    print("Your bmi is {bmi}, you are underweight")
elif bmi < 25:
     print("Your bmi is {bmi}, you have normal weight")
elif bmi < 30:
     print("Your bmi is {bmi}, you are overweight")
elif bmi < 35:
     print("Your bmi is {bmi}, you are obese")
else:
     print("Your bmi is {bmi}, you are clinically obese")