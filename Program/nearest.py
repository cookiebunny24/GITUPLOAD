
def nearest_smaller_to_left(arr):
    result = []
    for i in range(0, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                result.insert(i,arr[j])
                break
        else:
            result.insert(i,-1)

    return result

arr = [5,3,1,9,7,3,4,1]
print(nearest_smaller_to_left(arr))