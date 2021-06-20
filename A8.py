n = int(input())
c = 0
while n != 0:
    if n % 4 == 0 and n % 5 != 0:
        c += 1
    n -= 1
print(c)
