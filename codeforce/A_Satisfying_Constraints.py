def Satisfying_Constraints():
    t = int(input())
    for _ in range(t):
        n = int(input())
        _min = 0
        _max = 10**9
        ne = []
        sub = 0
        for _ in range(n):
            a, x = map(int, input().split())

            if a == 1:
                if x > _min:
                    _min = x
            elif a == 2:
                if x < _max:
                    _max = x
            else:
                ne.append(x)

        for num in ne:
            if num >= _min and num <= _max:
                sub += 1

        print(max(_max - _min + 1 - sub, 0))
Satisfying_Constraints()