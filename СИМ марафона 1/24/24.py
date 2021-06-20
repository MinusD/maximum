with open('24.txt', "r") as f:
    maxi = 0
    for i in f:
        if i.count('F') + i.count('Z') < i.count('A'):
            maxi = max(maxi, len(i))
    print(maxi-1)
