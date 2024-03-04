n,k = map(int,input('').split(' '))
a = list(map(int,input('').split(' ')))
b = list(map(int,input('').split(' ')))
profit = []
loss_b = []
p_loss = []
for i in range(n) :
    if a[i] - b[i] < 0 :
        profit.append(a[i])
    else :
        loss_b.append(b[i])
if k > len(profit) :
    m = k - len(profit)
    for i in range(n) :
        p_loss.append(a[i] - b[i])
    p_loss.sort()
    for i in range(m) :
        if k<=len(profit):
            break;
        for j in range(n):
            if k <= len(profit):
                break;
            elif (a[j] - b[j] == p_loss[i]):
                profit.append(a[j])
                loss_b.remove(b[j])
total = sum(profit) + sum(loss_b)
print(total)