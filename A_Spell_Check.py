n = int(input(''))
while n :
    m = int(input(''))
    t = "Tumri"
    dict = {"T" : 0,"u" : 0, "m" : 0, "r" : 0,"i" : 0}
    count = 0
    s = input("").strip()
    for i in range(m):
        if s[i] in t and m == 5:
            dict[s[i]] +=1
            count += 1
        else :
            break
    all_one = all(value == 1 for value in dict.values())
    if count == 5 and all_one == True:
        print('YES')
    else :
        print('NO')

    n-=1
            

