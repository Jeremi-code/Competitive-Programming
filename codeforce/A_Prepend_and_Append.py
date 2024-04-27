n = int(input())
while n :
    m = int(input())
    s = list(input())
    output = s;
    first = 0
    last = m-1
    while first < last:
        if s[first] == s[last]:
            break
        output = s[first+1:last]
        first += 1
        last -= 1
    print(len(output))
    n -= 1
    