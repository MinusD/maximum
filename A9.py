n = int(input())
result = 1
for i in range(1, n+1):
    if i % 8 == 0 or i % 6 == 0:
        result *= i
if result == 1:
    print(0)
else:
    print(result)
