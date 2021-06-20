st = list('ДЕКОР')
n = 1
for a  in st:
    for b in st:
        for c in st:
            for d in st:
                for e in st:
                    if a+b+c+d+e == "ДЕКОР":
                        print(n)
                    n+=1
