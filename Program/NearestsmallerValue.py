
def NearestSmallerValues(arr):
    result=[]
    for i in range(0, len(arr)):
        for j in range(i-1, 0, -1):
            if arr[i] > arr[j]:
                result.insert(i, arr[j])
                break
        else:
            result.insert(i, -1)

    return result

# keep this function call here
vals=[5,3,1,9,7,3,4,1]
print(NearestSmallerValues(vals))
