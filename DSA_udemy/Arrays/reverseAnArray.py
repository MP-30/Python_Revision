def reverse (nums):
    start_index = 0
    end_index = len(nums) -1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index -1

if __name__ == '__main__':
    arr = [12,45,15,75,48,47,45,85,47]

    a = reverse(arr)
    print(arr)
    print(a)