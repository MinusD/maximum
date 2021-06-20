st = list('АИОУЭ')
counter = 1
for a in st:
    for b in st:
        for c in st:
            for d in st:
                if a+b+c+d == 'ИААЭ':
                    print(counter, a+b+c+d)
                counter+= 1
