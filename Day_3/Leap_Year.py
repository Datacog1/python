# 🚨 Don't change the code below 👇
from email.headerregistry import UniqueAddressHeader


year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not leep year")