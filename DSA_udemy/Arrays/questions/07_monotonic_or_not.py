def monotonic_check(arr):
    length = len(arr)
    if length > 1:
        for i in range(length):
            if i == 0 or i == len(arr):
                return ("check later")
            else:
                arr[i] > arr[i+1]


arr1 = [4,8,9,12,58,69]
arr2 = [89,78,58,35,15,2]
arr3 = [4,7,5,1,2,6,8,5,3]
print(monotonic_check())