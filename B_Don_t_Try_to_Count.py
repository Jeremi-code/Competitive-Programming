def sub_string_check(a, b):
    operation = -1
    while len(a) <= 100:
        operation += 1
        for i in range(len(a)):
            if i + len(b) <= len(a): 
                match = True
                for j in range(len(b)):
                    if b[j] != a[i + j]:
                        match = False
                        break
                if match:
                    return operation 
        a += a
    return -1

def main():
    t = int(input())
    output = []

    for _ in range(t):
        n, m = map(int, input().split())
        x = input().strip()
        y = input().strip()

        output.append(sub_string_check(x, y))

    for val in output:
        print(val)

if __name__ == "__main__":
    main()
