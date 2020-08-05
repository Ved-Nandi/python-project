l = ['a', 'a', 'a', 'a', 'a','a']
step = 3
while 1:
    print(*l[:step])
    
    if l[5] == 'z':
        break
    if l[4] == 'z':
        l[5] = chr(ord(l[5]) + 1)
        l[4] = 'a'
        l[3] = 'a'
        l[2] = 'a'
        l[1] = 'a'
        l[0] = 'a'
        
        if step == 5:
            step +=1
    
    if l[3] == 'z':
        l[4] = chr(ord(l[4]) + 1)
        l[3] = 'a'
        l[2] = 'a'
        l[1] = 'a'
        l[0] = 'a'
        if step == 4:
            step +=1
        

    if l[2] == 'z':
        l[3] = chr(ord(l[3]) + 1)
        l[2] = 'a'
        l[1] = 'a'
        l[0] = 'a'
        if step == 3:
            step +=1

    if l[1] == 'z':
        l[2] = chr(ord(l[2]) + 1)
        l[1] = 'a'
        l[0] = 'a'


    if l[0] == 'z':
        l[1] = chr(ord(l[1]) + 1)
        l[0] = 'a'

    l[0] = chr(ord(l[0]) + 1)