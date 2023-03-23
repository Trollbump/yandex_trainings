#!/usr/bin/python3

k = int(input())
min_x, max_x, min_y, max_y = 10**9, -10**9, 10**9, -10**9

for i in range(k):
    x, y = list(map(int, input().split()))
    min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)

print(min_x, min_y, max_x, max_y)
