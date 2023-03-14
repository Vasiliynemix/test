n = int(input())
total = 0
while n != 0:
    total += n % 10
    n //= 10
    if n <= 0 and total > 9:
        n = total
        total = 0
        while n != 0:
            total += n % 10
            n //= 10
        else:
            if total > 9:
                n = total
                total = 0
print(total)
