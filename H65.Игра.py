def ng():
   t = list(input("New ").split())
   global a, b, h
   #a = int(t[0])
   a = 12
   b = int(t[0])
   h = 1
   change_msg()

def change_msg():
    global h, msg
    if h%2 == 0:
        msg = 'V: '
    else:
        msg = 'P: '
    

def next():
    print(a, b, "|", [[a+1, b], [a*2,b], [a, b+1], [a, b*2]])
    change_msg()
    if a + b >= 74:
        print('End Game', ('P' if h%2 == 0 else 'V'))
        ng()


msg = 'print 0 to start\n'
while True:
    v = int(input(msg))
    if v == 0:
        ng()
    elif v == 1:
        a += 1
    elif v == 2:
        a *= 2
    elif v == 3:
        b +=1
    elif v ==4:
        b*= 2
    next()
    h+=1
