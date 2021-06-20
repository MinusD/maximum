with open('26.txt', 'r') as f:
    n = int(f.readline())
    a = []
    summ = 0
    m = []
    mm = []
    max_sale = 0
    for i in range(n):
        a.append(int(f.readline()))
    for i in range(n):
        if a[i] <=200:
            m.append(a[i])
        else:
            mm.append(a[i])
    for i in range(1, len(mm)+1):
        if i %2 !=0:
            summ += max(mm)
            mm.remove(max(mm))
        else:
            summ += min(mm) * 0.65
            max_sale = max(max_sale, min(mm))
            mm.remove(min(mm))
    print(sum(m) + summ, max_sale)
