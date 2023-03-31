#!/usr/bin/python3

from string import ascii_lowercase as alph

s = input()
m = {}
n = len(s)

for i in range(n):
    if s[i] not in m.keys():
        m[s[i]] = 0
    
    m[s[i]] += (i+1) * (n-i)

for char in alph:
    if char in m.keys():
        print(f'{char}: {m[char]}')

