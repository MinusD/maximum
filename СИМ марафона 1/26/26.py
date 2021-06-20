from math import *
with open('26.txt', 'r') as f:
    n = int(f.readline())
    items = []
    res = 0
    max_sell = 0
    for i in range(n):
        tmp = int(f.readline())
        if tmp > 150:
            items.append(tmp)
        else:
            res+=tmp
    #items = sorted(items, key=int)
    for i in range(1, len(items)+1):
        if i%2 != 0:
            maxi = max(items)
            res += maxi
            items.remove(maxi)
        else:
            mini = min(items)
            res += mini*0.8
            items.remove(mini)
            max_sell = max(max_sell, mini)
    print(floor(res), max_sell)
