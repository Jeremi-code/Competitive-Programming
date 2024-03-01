n,m = map(int,input('').split(' '))
a = list(map(int,input('').split(' ')))
a.sort()
max_earned = 0
for i in range(m):
    if(a[i]>0):
        break
    max_earned += a[i]
print(abs(max_earned))