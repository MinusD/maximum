st = list('АКРУ')
counter = 1
for a in st:
    for b in st:
        for c in st:
            for d in st:
                for e in st:
                    for f in st:
                        if counter == 215:
                            print(counter, a+b+c+d+e+f)
                        counter+= 1
