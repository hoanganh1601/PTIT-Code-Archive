if __name__ == '__main__':
    test = int(input())
    for _ in range(test):     
        num = input()
        if len(num) < 3:
            print("NO")
        else:
            inc = [1] * (19)
            dec = [1] * (19)
            
            for i in range(1, len(num)):
                if num[i - 1] < num[i]:
                    inc[i] = inc[i - 1] + 1
            
            for i in range(len(num) - 2, -1, -1):
                if num[i + 1] < num[i]:
                    dec[i] = dec[i + 1] + 1

            check = False
            for i in range(len(num)):
                # print(inc[i], dec[i])
                
                if inc[i] + dec[i] - 1 == len(num):
                    print("YES")
                    check = True
                    break
            if not check:
                print("NO")
                    
        