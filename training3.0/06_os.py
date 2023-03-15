#!/usr/bin/python3

# пересекаются ли операционки
def is_cross(a1, b1, a2, b2):
    return ((a1 <= b2) and (a2 <= b1))

m = int(input())
n = int(input())

arr = []  # хранение всех осей, ось: (ai, bi, is_working)
cnt = 0   # счетчик рабочих осей для ответа

for i in range(n):
    a, b = list(map(int, input().split()))

    # обходим все существующие оси
    for j in range(len(arr)):
        # если текущая работает и пересекается с новой - удаляем текущую
        if ((arr[j][2]) and (is_cross(a, b, arr[j][0], arr[j][1]))):
            arr[j] = (arr[j][0], arr[j][1], False)
            cnt -= 1

    # добавляем новую ось
    arr.append((a, b, True))
    cnt += 1

print(cnt)

