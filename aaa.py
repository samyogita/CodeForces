t = int(input())
for _ in range(t):
    def solve():
        num = int(input())
        arr = list(map(int, input().split()))
        string = list(input())
        dict = {}
        for i in range(len(arr)):
            if arr[i] in dict and dict[arr[i]] != string[i]:
                print('NO')
                return
            else:
                dict[arr[i]] = string[i]
        print('YES')
    
    solve()

        
        
    
    

    


