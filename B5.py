s = 'ЕЗЛМЯ'
s = list(s)
print(s)
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    if(a+b+c+d+e == "ЗЕМЛЯ"):
                        print(k)
                    k += 1
