
def check(char):
    cnt = 0
    for i in char:
        cnt += (i>0)
    return cnt

t = int(input())
for _ in range(t):
    length = int(input())
    c = input()
    rmp = [0] * 26
    lmp = [0] * 26
    for i in c:
        pos = ord(i) - ord('a')
        rmp[pos] += 1
    l, r = 0, check(rmp)
    best = l + r
    for x in range(length):
        cpos = ord(c[x]) - ord('a')
        lmp[cpos] += 1
        rmp[cpos] -= 1
        best = max(best, check(lmp) + check(rmp))

    print(best)


