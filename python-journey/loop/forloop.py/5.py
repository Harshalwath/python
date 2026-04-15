num = int(input("Enter a number: "))
count = 0


num = abs(num)


for digit in str(num):
    count += 1

print("Number of digits:", count)