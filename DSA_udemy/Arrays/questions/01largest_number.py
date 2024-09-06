# find the maximum value in array

'''
Time complexity: O(N)
Auxiliary space: O(1)

two other way using sort() and max method

'''
def largest(arr, n):
    max = arr[0]
    
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

n1 = 7
arr1 = [45,75,84,14,78,53,65]
print(largest(arr1,n1))
