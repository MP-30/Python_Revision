# array roation by d element


def check_rotation_by_d_element(arr, d):
    length_of_original_array = len(arr)
    if d == 0:  
        return arr
    elif d == length_of_original_array:
        return arr
    elif d < 0:
        d = -d * len(arr)
        arr1 = (arr[d:]) + (arr[:d])
        return arr1
    elif d >= length_of_original_array:
        return ('Enter correct value of d')
    else:
        arr1 = (arr[d:]) + (arr[:d])
        return arr1


arr0 = [4,5,7,8,1,2,5,9,6,3,8,5,9]
d_element = 8
print(check_rotation_by_d_element(arr=arr0, d=d_element))

def
revisit again