def solve():
    st = list(map(int, input().split()))
    for _ in range(3):
        if len(set(st)) == 1:
            print("YES")
            return
        x = min(st)
        y = max(st)
        st.append(x)
        st.append(y - x)
        st.remove(y)
    if len(set(st)) == 1:
        print("YES")
    else:
        print("NO")

def main():
    TC = int(input())
    for _ in range(TC):
        solve()

if __name__ == "__main__":
    main()
