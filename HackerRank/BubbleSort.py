def countSwaps(a):
    count=0
    temp=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                count+=1
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


    
