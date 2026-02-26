#Simple Calculator

num1 = float(input("enter first number:"))

op= input(" Enter operator (+, -, *, /):")




num2 = float(input("enter second number:"))

if op == "+":
    print("Result=", num1 + num2)

elif op =="-":
    print("result", num1 - num2)

elif op == "*":
    print("result", num1 * num2)

elif op == "/":
    print("result", num1 / num2)

else:
    print("invalid")
