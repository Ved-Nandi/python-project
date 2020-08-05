l = ['a', 'a', 'a']
step = 3
while 1:
    if l[len(l) - 1] == 'z':
        break

    if '{' in str(l):

        for i in range(len(l), 0, -1):
            if l[i - 2] == '{':
                l[i - 1] = chr(ord(l[i - 1]) + 1)
                
                if l[i - 1] == '{':
                    l[i] = chr(ord(l[i]) + 1)
                    l[i-1]='a'
                
                if step == i-1 :
                    step += 1
                for ii in range(i-1):
                    l[ii] = 'a'

                        
    print(l[:step])
    l[0] = chr(ord(l[0]) + 1)
    