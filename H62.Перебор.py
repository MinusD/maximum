maxi = 0
mini = 100000
for i in range(84533, 97432):
    if i%3 == 0 and i % 7 == 0 and i%9 != 0 and i %13 !=0 and i%10 == 3:
        maxi = max(maxi, i)
        mini = min(mini, i)
print(maxi-mini)
