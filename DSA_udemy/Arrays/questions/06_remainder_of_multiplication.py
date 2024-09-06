def remainderOfArrayMultiplication(arr, n):
    a = 1
    for i in range(len(arr)):
        a = a * arr[i]
    print(a)
    print(a%n)
    
        


arr1 = [100, 10, 5, 25, 35, 14]
n1=11
remainderOfArrayMultiplication(arr1,n1)