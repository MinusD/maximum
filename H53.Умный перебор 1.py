n = int(input())
mt = 0
m2t = 0
mnt = 0
mn2t = 0
for i in range(n):
    num = int(input())
    if num%2 == 0:
        if mt < num:
            m2t = max(mt, m2t)
            mt = num
        elif mt == num:
            mt2 = num
        else:
            m2t = max(m2t, num)
    else:
        if mnt < num:
            mn2t = max(mnt, mn2t)
            mnt = num
        elif mnt == num:
            mtn2 = num
        else:
            mn2t = max(mn2t, num)
print(max(mt*m2t, mt*mnt))
