def is_reverse(s):
    return s == s[::-1]

t = int(input().strip())
for _ in range(t):
    n, s = input().split()
    n = int(n)
    s = list(s)
    flag, r, loop = 1, len(s) - 1, 0
    while loop < r:
        if flag == 0 and s[loop] == s[r]:
            break
        if s[loop] != s[r]:
            if s[r] == '1':
                s[r] = '0'
            else:
                s[r] = '1'
            r -= 1
            loop += 1
            flag = 0
        elif s[loop] == s[r]:
            loop += 1
            r -= 1

    if is_reverse(s):
        print("YES")
    else:
        print("NO")
