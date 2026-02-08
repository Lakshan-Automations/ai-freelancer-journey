number = int(input("enter the number"))
if number > 0:
    print("positive")

age = int(input("enter your age"))
if age > 18:
    print("adult")
else:
    print("mionr")

temp = int(input("temperature?"))
if temp > 30:
    print("hot")
elif temp > 20:
    print("warm")
else:
    print("cold")

password = input("enter your password")
if password == "secret123":
    print("access granted")
else:
    print("access denided")

number_to_check = int(input("enter a number to check its even or odd"))
if number_to_check % 2 == 0 and number_to_check != 0:
    print("even")
else:
    print("odd")



