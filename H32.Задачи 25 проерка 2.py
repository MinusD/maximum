for i in range(12, 19):
    co = 0
    j = i//2
    pr = 1
    dividers = ""
    while co <= 4 and j > 1:
        if i%j == 0:
            co += 1
            pr*=j            
            dividers = dividers + " " + str(j) 
        j -= 1
    if co == 4:
        print(dividers[::-1],'pr =', pr)
        
