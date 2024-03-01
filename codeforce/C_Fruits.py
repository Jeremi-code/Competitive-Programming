n,m = map(int,input('').split(' '))
p = list(map(int,input('').split(' ')))
p.sort()
s_dict = {}
maxima = 0
minima = 0
k = m
while k :
    s = input('')
    if(s not in s_dict):
        s_dict[s] = 0
        
    s_dict[s] += 1
    k-=1
s_list = sorted(list(s_dict.values()),reverse=True)
for i in range(len(s_list)):
    if s_list[i] > m :
        minima += m * p[i]
        maxima += m * p[-i -1]
        break
    else :
        minima += s_list[i] * p[i]
        maxima += s_list[i] * p[-i -1]
        m -=s_list[i] 
print(minima,maxima)