for i in range(130149, 130212):
    co = 0
    j = i//2
    pr = 1
    dividers = ""
    while co <= 4 and j > 1:
        if i%j == 0:
            co += 1
            pr*=j            
            dividers = str(j) + " " + dividers
        j -= 1
    if co == 4:
        print(dividers,'pr =', pr)
        
