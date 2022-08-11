user_input = input("select oneo of them: *, /, +, -     ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if user_input == "+":
    print( num1 + num2 )
elif user_input == "-":
    print(num1 - num2)
elif user_input == "/":
    print(num1 / num2)
elif user_input == "*":
    print(num1 * num2)
else:
    print("invaild operator")
