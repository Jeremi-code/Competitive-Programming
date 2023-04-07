class Solution: 
    def select(self, arr, i):
        # code here 
        minIndex = i
        for i in range(i+1,len(arr)):
            if arr[i] < arr[minIndex]:
                minIndex = i
        return minIndex
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minIndex = self.select(arr,i)
            arr[minIndex],arr[i] = arr[i],arr[minIndex]
    
        return arr