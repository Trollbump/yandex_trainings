#!/usr/bin/python3

from math import ceil

def to_sec(a):
    return a[0]*60*60 + a[1]*60 + a[2]

def from_sec(a):
    res = []
    res.append(str(a//(60*60)))
    a -= int(res[0])*60*60
    res.append(str(a//(60)))
    a -= int(res[1])*60
    res.append(str(a))
    if (int(res[0]) >= 24):
        res[0] = str(int(res[0]) - 24)
    for i in range(3):
        if len(res[i]) < 2:
            res[i] = '0' + res[i]
    return ':'.join(res)
    

a = to_sec(list(map(int, input().split(':'))))
b = to_sec(list(map(int, input().split(':'))))
c = to_sec(list(map(int, input().split(':'))))

if a > c:
    c += 24*60*60

delay = ceil((c-a) / 2.0)
res = from_sec(b + delay)

print(res)

