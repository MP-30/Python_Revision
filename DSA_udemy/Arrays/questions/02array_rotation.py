
def array_roation(arr):
    length = len(arr)

    if length == 0:
        return arr
    else:
        arr1 = [0] * length
        for i in range(len(arr)):
            arr1[i] = arr[-(i+1)]
        return (arr1)
            
    
arry = [71,45,78,4,7,15,74,85,26,9]
print(array_roation(arry))