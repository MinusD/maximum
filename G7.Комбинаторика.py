st = list('ЛАВР')
counter = 0
for a in st:
    for b in st:
        for c in st:
            for d in st:
                for e in st:
                    for f in st:
                        for g in st:
                            co = 0
                            co += 1 if a == 'А' else 0
                            co += 1 if b == 'А' else 0
                            co += 1 if c == 'А' else 0
                            co += 1 if d == 'А' else 0
                            co += 1 if e == 'А' else 0
                            co += 1 if f == 'А' else 0
                            co += 1 if g == 'А' else 0
                            if co == 2:
                               counter+=1
print(counter)
