#!/usr/bin/python3

with open("input.txt", 'r') as infile:
    # count all chars
    m = {}
    for line in infile:
        s = list(line.replace(' ', '').replace('\n', ''))
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
    
    # start histogram
    s = ''.join(sorted(m))
    length = max(m.values())

    for i in range(length):
        tmp = ''
        for c in s:
            if (length-i) == m[c]:
                m[c] -= 1
                tmp += '#'
            else:
                tmp += ' '
        print(tmp)

    print(s)

