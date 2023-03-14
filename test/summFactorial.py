n = int(input())
faq_sum = 1
total = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        faq_sum *= j
    total += faq_sum
    faq_sum = 1
print(total)