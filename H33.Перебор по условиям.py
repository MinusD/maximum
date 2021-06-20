maxi = 1016
n = 0
for i in range(1016, 7938):
    if i%3 == 0:
        if i%7!= 0 and i%17!= 0 and i%19 != 0 and i%27 != 0:
            if i > maxi:
                maxi = i
            n += 1
print(n, maxi)
                
            
