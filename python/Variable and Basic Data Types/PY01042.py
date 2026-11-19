if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        arr = input()
        check = True
        for x in arr:
            if x not in ['0', '1', '2']:
                print("NO")
                check = False
                break
        if check:
            print("YES")
