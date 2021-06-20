n = 43046955
ans = ''
while n!=0:
    ans += str(n%3)
    n//=3
print(ans[::-1])
