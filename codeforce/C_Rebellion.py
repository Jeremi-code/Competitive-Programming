# t = int(input(''))
# while t :
#     n = int(input(''))
#     m = list(map(int,input('').split(' ')))
#     k=m[:]
#     count = 0
#     for i in range(n//2):
#         if k == sorted(k):
#             break
#         for j in range(n-1,n//2 -1,-1):
#             if m[i] == 1 and m[j] == 0:
#                 m[j] +=m[i]
#                 count +=1
#                 k.remove(k[i])
    
#     print(count)
#     t -=1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ct = 0
    i = 0
    j = n - 1
    while i < j:
        if a[i] == 1 and a[j] == 0:
            ct += 1
        elif a[i] == 1 and a[j] == 1:
            i -= 1
        elif a[i] == 0 and a[j] == 0:
            j += 1
        i += 1
        j -= 1
    print(ct)

def main():
    TC = int(input())
    for _ in range(TC):
        solve()

if __name__ == "__main__":
    main()


