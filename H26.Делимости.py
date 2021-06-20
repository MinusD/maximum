sum = 0
co = 0
for i in range(55261, 61513):
    if i%3 == 0 and i%5 == 0:
        if i%2!=0 and i%11!=0 and i%17!=0:
            co+=1
            sum+=i
print(sum/co, co)
