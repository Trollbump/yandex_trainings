#!/usr/bin/python3

def binsearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return l

n = int(input())
a = sorted(list(set(map(int, input().split()))))

k = int(input())
p = list(map(int, input().split()))
for elem in p:
    print(binsearch(arr=a, x=elem))

