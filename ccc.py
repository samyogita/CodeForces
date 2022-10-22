import bisect
t = int(input())
for _ in range(t):
    strlen, char = list(map(str, input().split()))
    strlen = int(strlen)
    s = list(input())
    string = s + s
    charpos = []
    g = []
    res = 0
    for i in range(strlen):
        if s[i] == char:
            charpos.append(i)
    for i in range(len(string)):
        if string[i] == 'g':
            g.append(i)
   
    for ele in charpos:
        val = bisect.bisect_left(g, ele)
        res = max(res, g[val] - ele)
    print(res)


    
    

