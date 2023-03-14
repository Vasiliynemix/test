a = int(input())
b = int(input())
counter = 0
for i in range(a, b + 1):
    if i == 2:
        print(i)
    for j in range(1, i + 1, 2):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)
    counter = 0

