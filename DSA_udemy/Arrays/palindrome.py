
def reverse(strr):
    s = strr[::-1]
    if s == strr:
        return True
    else:
        return False
if __name__ == '__main__':
    str1 = 'radar'
    str2 = 'aditya'
    str3 = 'madam'
    a = reverse(str1)
    print(reverse(str3))
    
