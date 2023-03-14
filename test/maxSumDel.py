a = int(input())
b = int(input())
total = 0
largest = 0
res = a - 1
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= largest and i >= res:
        largest = total
        res = i
    total = 0
print(res, largest, sep=" ")
