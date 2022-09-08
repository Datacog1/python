# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
str_number = str(two_digit_number)
first_digit = int(str_number[0])
second_digit = int(str_number[1])
print(f"Digit one: {first_digit}")
print(f"Digit two: {second_digit}")
print(f"The sum of {first_digit} and {second_digit} is {first_digit+second_digit}")