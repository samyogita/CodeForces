t = int(input())
for _ in range(t): 
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    flag = 1
    for j in range(len(arr)-1):
        if arr[j] == arr[j+1]: 
            print('NO')
            flag = 0
            break
    if flag == 1:
        print('YES')

        
            
