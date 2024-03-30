s =input().strip()
t = input().strip()
l1 = len(s)
l2 = len(t)
length = l1 + l2
c = 0
if s[l1-1] != t[l2-1] :
    print(length)
else :
    while l2 and l1 >= 0:
        l1 -=1
        l2 -=1
        if s[l1] == t[l2] :
            c+=1
        else :
            break
    print(length - (2*c))


