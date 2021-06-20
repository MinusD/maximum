from random import *
n = int(input('Количество чисел: '))
answer = 0
a = [randint(1, 1000) for i in range(n)]
for i in range(n-4):
    for j in range(i+4, n):
        answer = (max(answer, a[i] * a[j]) if (a[i] * a[j])%2 == 0 else answer)
print(answer)
