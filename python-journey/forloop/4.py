lst = [10, 20, 30, 40, 50]

n = len(lst)
for i in range(n // 2):
    lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

print("Reversed list:", lst)