s = 'ДЕКОР'
s = list(s)
co = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                print(co, a+b+c+d)
                co+=1
