n = int(input(""))
while n :
    c = int(input(""))
    r1 = list(input(''))
    r2 = list(input(''))
    for i in range(c):
        if r1[i] == "B":
            r1[i] = "G"
        if r2[i] == "B":
            r2[i] = "G"
    if r1 == r2 :
        print('YES')
    else :
        print('NO')
    n-=1