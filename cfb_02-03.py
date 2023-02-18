n = int(input())
for _ in range(n):
    l = int(input())
    c = input()
    ans = False
    start = [0, 0]
    for i in range(l):
        if c[i] == 'U':
            start[1] += 1
        elif c[i] == 'D':
            start[1] -= 1
        elif c[i] == 'R':
            start[0] += 1
        elif c[i] == 'L':
            start[0] -= 1
        if start == [1, 1]:
            ans = True
    
    print('YES' if ans else 'NO')
    

