#!/usr/bin/python3

from math import floor 

def place_to_coords(a):
    return [floor(a/2)+a%2, 2-a%2]

n = int(input())
k = int(input())
p_row = int(input())
p_deskplace = int(input())

p_place = (p_row-1)*2 + p_deskplace
p_var = p_place % k
if p_var == 0:
    p_var += 1
flag = True

if ((p_place + k <= n) and (p_place - k >= 1)):
    if (place_to_coords(p_place+k)[0] - p_row <= p_row - place_to_coords(p_place-k)[0]):
        w_place = p_place + k
    else:
        w_place = p_place - k
elif (p_place + k <= n):
    w_place = p_place + k
elif (p_place - k >= 1):
    w_place = p_place - k
else:
    flag = False

if flag:
    print(*place_to_coords(w_place))
else:
    print(-1)

