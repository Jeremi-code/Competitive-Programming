def main():
    n = int(input())
    left = []
    right = []
    for _ in range(n):
        l, r = map(int, input().split())
        left.append(l)
        right.append(r)
    
    r0 = r1 = l0 = l1 = 0
    for i in range(n):
        if right[i] == 1:
            r1 += 1
        else:
            r0 += 1
    
    red = min(r1, r0)
    
    for i in range(n):
        if left[i] == 1:
            l1 += 1
        else:
            l0 += 1
    
    red += min(l1, l0)
    print(red)

if __name__ == "__main__":
    main()
