s = list("ДЕКОР")
print(s)
co = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                if a == "К":
                    print(co, a+b+c+d)
                co+=1
