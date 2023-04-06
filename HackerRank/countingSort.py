def countingSort(arr):
    list=[]
    for i in range(100):
        if i in arr:
            list.append(arr.count(i))
        else:
            list.append(0)
    return list

print(countingSort([1,1,3,2,1]))