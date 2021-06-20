from collections import * 
with open('24.txt', 'r') as f:
    st = f.readline()
    a = list(st)
    arr = []
    for i in range(1, len(a)):
        if a[i] == 'Z':
            arr.append(a[i-1])
    print(Counter(arr))
