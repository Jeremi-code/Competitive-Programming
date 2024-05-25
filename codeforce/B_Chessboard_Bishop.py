def max_bishop_sum(test_cases):
    results = []

    for case in test_cases:
        n, m, board = case
        TLBR = {}  
        TRBL = {}  

        for i in range(n):
            for j in range(m):
                if (i - j) not in TLBR:
                    TLBR[i - j] = 0
                if (i + j) not in TRBL:
                    TRBL[i + j] = 0
                TLBR[i - j] += board[i][j]
                TRBL[i + j] += board[i][j]

        max_sum = 0

        for i in range(n):
            for j in range(m):
                current_sum = TLBR[i - j] + TRBL[i + j] - board[i][j]
                if current_sum > max_sum:
                    max_sum = current_sum

        results.append(max_sum)
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, board))

results = max_bishop_sum(test_cases)

for result in results:
    print(result)
