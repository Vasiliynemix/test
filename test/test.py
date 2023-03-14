count = 0
counter = 0
x = 150
print("Существует ли a^5 + b^5 + c^5 + d^5 = e^5, если a, b, c, d, e <= x")
print("Ищем ответ...")
for a in range(1, x + 1):
    for b in range(a, x + 1):
        for c in range(b, x + 1):
            for d in range(c, x + 1):
                for e in range(max(a, b, c, d) + 1, x + 1):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print("Ура!!! существует")
                        print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
                        print(f"Было проверено где-то {int(a / x * 100)}% всех комбинаций")
                        print("Поздравляем, мы только что опровергли Великую теорему Ферма")
                        count = 1
                        break
                if count:
                    break
            if count:
                break
        if count:
            break
    if a == 5:
        print("Не сдаваться!!! еще чуть-чуть=)")
    if a % 2 == 0:
        counter += 1
        print(f"Еще немного <3... проверено где-то {counter * 10}% всех комбинаций")
    if count:
        break
else:
    print("программа завершилась")
