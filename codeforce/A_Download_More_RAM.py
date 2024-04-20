t = int(input())
while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = []
    for i in range(n):
        ab.append([a[i],b[i]])
    ab.sort(key=lambda x: x[0])
    for i in range(len(a)):
        if k < ab[i][0]:
            break
        k += ab[i][1]

    print(k)
    t -= 1
