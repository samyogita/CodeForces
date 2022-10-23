t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    for i in range(2, len(arr)):
        if arr[0] + arr[1] == arr[i]:
            print('YES')
        else:
            print('NO')

