n = 780501
flag = 0
f = []
while flag <=10:
    maxi = 0
    mini = n+1
    for i in range(3, n//2+1, 2):
        if n%i == 0:
            maxi = max(i, maxi)
            mini = min(i, mini)
    if (maxi-mini)%7 == 0 and maxi-mini!=0:
        f.append([n, maxi-mini])
        print(n, maxi-mini, "|", maxi, mini)
        flag+=1
    n+=1
print(f)
