def StockPicker(arr):
    temp=0
    maxcost=0
    mini=arr[0]
    for i in range(0,len(arr)):
        mini= min(mini,arr[i])
        temp=arr[i]-mini
        maxcost=max(maxcost,temp)
    return maxcost

# keep this function call here
input1=[10,12,4,5,9]
print(StockPicker(input1))