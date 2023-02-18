t = int(input())
for _ in range(t):
    length = int(input())
    val = input()
    l = 0
    r = length - 1
    while l < r:
        if (val[l] == '0' and val[r] == '1') or (val[l] == '1' and val[r] == '0'):
            l += 1
            r -= 1
        else:
            break
    print(r-l+1)
