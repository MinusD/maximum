a = []
for i in range(413124, 519916):
    if i %13 == 0 and i%9 == 7:
        a.append(i)
print(len(a), sum(a), a)
