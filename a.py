t = int(input())
for T in range(1, t+1):
    string = ''
    f = -1
    s = input()
    for i in range(0, len(s)):
        string += 'Yes'
    f = string.find(s)
    if f == -1:
        print('NO')
    else:
        print('YES')
