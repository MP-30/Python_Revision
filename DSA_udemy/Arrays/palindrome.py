
def reverse(strr):
    start_point = 0
    end_point = len(strr) -1
    print(end_point)
    print(strr[1])
    while end_point > start_point:
        strr[start_point], strr[end_point] = strr[end_point], strr[start_point]
        start_point =+ start_point +1
        end_point =+ end_point -1

if __name__ == '__main__':
    str1 = 'radar'
    str2 = 'aditya'
    str3 = 'madam'
    a = reverse(str1)
    print(reverse(str1))
    print(a)
