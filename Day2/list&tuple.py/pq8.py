numbers = [10, 20, 30, 40]

print("Original List:", numbers)

pos = int(input("Enter position to insert: "))
value = int(input("Enter value to insert: "))

numbers.insert(pos, value)

print("Updated List:", numbers)