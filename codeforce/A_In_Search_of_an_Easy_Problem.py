n = int(input(''))
m = list(map(int,input('').split(' ')))
is_easy = True
for i in range(n):
    if m[i] == 1 :
        is_easy=False
        break

if is_easy :
    print('EASY')
else :
    print('HARD')