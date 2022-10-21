t = int(input())
for _ in range(t):
    arrlen, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    evenCnt = 0
    oddCnt = 0
    for i in arr:
        if i % 2 == 0:
            evenCnt += 1
        else:
            oddCnt+= 1
    total = sum(arr)
    for i in range(q):
        q, val = list(map(int, input().split()))
        if q == 0:
            total += evenCnt * val
            if val % 2 != 0:
                oddCnt += evenCnt
                evenCnt = 0
            print(total)
        else:
            total += oddCnt * val
            if val % 2 != 0:
                evenCnt += oddCnt
                oddCnt= 0
            print(total)
        
        



   
   
    
    