for i in range(10, 19):
    co = 0
    pr = 1
    j = i//2
    dividers = ""
    while co <= 4 and j > 1:
        if i%j == 0:
            co += 1
            pr*=j
            dividers = dividers + " " +  str(j) 
        j -= 1
    if co == 4:
        print(dividers[::-1], 'pr =', pr)
        
