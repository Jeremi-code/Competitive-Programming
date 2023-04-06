def insertionSort1(n, arr):
    temp=arr[-1]
    for i in range (n-2,-1,-1):
        if temp<arr[i] and i>=0:
            arr[i+1]=arr[i]
            print(*arr)
        elif temp>arr[i]:
            arr[i+1]=temp  
            break
        if i==0:
            arr[i]=temp
            print(*arr)
    print(*arr) 



