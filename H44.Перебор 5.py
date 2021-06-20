n = 0
m = 100000
su = 0
for i in range(1535, 8644):
    s = i//10
    if i%2==0 and i%11!=0 and s%10>=5:
        n+=1
        su += i
        mi = i
        m = min(m, i)
print(n, su/n)
