unit = int(input("enter units:"))

if unit <= 100:

    print("you need to pay 5rs per unit")
    bill=unit *5
    print("your bill is",bill)

elif unit <200:

    print("you need to pay 7 rs per unit")
    bill = unit*7
    print("your bill is",bill)

elif unit >200:

    print("you need to pay 10 rs per unit")
    bill=unit*10
    print("your bill is",bill)

print("code ended")