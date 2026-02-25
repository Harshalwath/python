#WAp to find the greatest of 3 number  entered by the user.

a = int(input("enter first number:"))

b = int(input("enter second number:"))

c = int(input("enter third number:"))

if (a>b & a>c):

    print(" first numberis a largest")

elif(b>c):

    print("second number is largest")

else:
    print("third number is largest")