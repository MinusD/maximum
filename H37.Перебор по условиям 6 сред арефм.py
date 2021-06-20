m = 0
mi = 100000
n = 0
for i in range(1869, 6598):
    if i%3 == 0 and i%7 == 0 and i%10 == 5:
        if i%4!= 0 and i%6!= 0:
            nu = list(str(bin(i))[2:])
            nc = 0
            for j in nu:
                nc+=int(j)
            if(nc %2 == 0):  
                n += 1
                m = i
                if i < mi:
                    mi = i
            
print(m - mi, mi + m)

                
            

