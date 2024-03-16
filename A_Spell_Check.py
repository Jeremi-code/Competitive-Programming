n = int(input(''))
while n :
    m = int(input(''))
    t = "Tumri"
    s = list(input(""))
    count = 0
    for i in range(m):
        if s[i] in t :
            count +=1
        else :
            break
    if count == 5 :
        print('YES')
    else :
        print('NO')
    n-=1
            

