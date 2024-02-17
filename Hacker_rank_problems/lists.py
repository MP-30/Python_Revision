if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        camnd = input().split()
        if camnd[0] == "insert":
            list.insert(int(camnd[1]), int(camnd[2]))
        elif camnd[0] == "append":
            list.append(int(camnd[1]))
        elif camnd[0] == "print":
            print(list)
        elif camnd[0] == "remove":
            list.remove(int(camnd[1]))
        elif camnd[0] == "sort":
            list.sort()
        elif camnd[0] == "pop":
            list.pop()
        elif camnd[0] == "reverse":
            list.reverse()
        