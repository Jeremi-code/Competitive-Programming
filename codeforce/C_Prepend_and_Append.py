t = int(input(''))
while t : 
    n = int(input(''))
    s = input('')
    s_copy = s
    count = 0
    for i in range(n//2) : 
        if s_copy[i] == s_copy[-i -1] :
            break
        else : 
            s = s_copy[i+1:-i-1]
    count = len(s)
    print(count)
    t-=1