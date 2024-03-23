def main():
    k = int(input())
    a = list(map(int, input().split()))
    total = sum(a)

    if total < k:
        print(-1)
    else:
        a.sort(reverse=True)
        summation = 0
        month = 0
        while summation < k:
            summation += a[month]
            month += 1
        print(month)

if __name__ == "__main__":
    main()
