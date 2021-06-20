import random
items = [random.randint(-1000, 1000) for i in range(30)]
maxi = -1
for i in items:
    if i%2 == 0 and i > maxi and i > 0:
        maxi = i
print(maxi)
