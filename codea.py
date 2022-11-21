t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(arr[1])