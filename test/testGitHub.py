n = int(input())
a = 1
y = 0
for i in range(n):
    b = a
    a = b + y
    y = b
    print(b, end=" ")
