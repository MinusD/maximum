n = int(input())
k = 0
while n > 1:
    if n%6==0:
        k+=1
        n//=6
    else:
        k = "Не является степенью"
        break
print(k)
