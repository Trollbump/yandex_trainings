#!/usr/bin/python3

n = int(input())
a = [int(input()) for i in range(n)]

cnt = min(a)*(n-1)
m = min(a)
for i in range(n):
    a[i] -= m

while (a.count(0) < n-1):  # идем по отрезкам между нулями, минусуем минимум по отрезку, и тд
    i = 0
    while ((i < len(a)-1) and (a[i] == 0)):  # идем до ближайшего НЕ 0
        i += 1
    start = i              # запоминаем отрезок
    while ((i < len(a)) and (a[i] != 0)):     # идём до конца отрезка
        i += 1
    # полученный отрезок - a[start:i+1]
    if (i-1 == start):
        a[start] = 0
    else:
        i -= 1
        m = min(a[start:i+1])
        cnt += (m * (i-start))  # добавляем к счетчику красивости макс строчку из отрезка (кроме ласт)
        for j in range(start, i+1):
            a[j] -= m

print(cnt)

