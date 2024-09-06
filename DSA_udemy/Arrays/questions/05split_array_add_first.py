def split_array(arr, d):
    new_array = arr[d:] + arr[:d]
    return (new_array)

arr1 = [8,765,46,7,534,65,75,57,12,3]
d1 = 3
print(split_array(arr1,d1))