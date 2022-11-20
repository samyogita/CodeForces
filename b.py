t = int(input())
for _ in range(t):  
    m, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    t = sum(arr)
    total = s + t
    mx = max(arr)
    while mx * (mx + 1) / 2 < total:
        mx += 1
    if mx * (mx + 1) / 2 == total:
        print('YES')
    else:
        print('NO')
    
