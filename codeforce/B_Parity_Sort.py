t = int(input(''))
while(t):
    n=int(input(''))
    m=list(map(int,input('').split(' ')))
    k = sorted(m)
    bool = True
    for i in range(n) :
        if (m[i] % 2 == 0 and k[i] %2 ==  1 ) or (m[i] % 2 == 1 and k[i] % 2 == 0):
            bool = False
            break

    if bool :
        print('YES')
    else :
        print('NO')
    t -=1
                    
