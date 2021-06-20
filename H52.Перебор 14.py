from random import *
from time import *
timer = time()
n = int(input('Количество чисел: '))
answer = 0
t14 = 0
a = [randint(1, 1000) for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        answer += (1 if a[i]%14 == 0 or a[j]%14 == 0 or (a[i]%2 == 0 and a[j]%7 == 0) or (a[j]%2 == 0 and a[i]%7 == 0) else 0)
print(answer)
print("Выполнено за:", time() - timer)
