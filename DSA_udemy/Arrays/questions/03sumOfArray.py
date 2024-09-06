# print sum of array


def sumOfArray(arr):
    length = len(arr)
    sumOfArrayElements = 0
    for i in range(length):
        sumOfArrayElements = sumOfArrayElements + arr[i]
    return sumOfArrayElements


arr1 = [5,4,7,8,9,6,5,4,2,5,8]
print(sumOfArray(arr1))