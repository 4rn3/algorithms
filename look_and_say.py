# start = 1
#1 -> 11, 1 x 1
#11 -> 21, 2 x 1
#21 -> 1211, 1 x 2 + 1x1
def next_number(s):
    res = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        res.append(str(count) + s[i])
        i += 1
    return ''.join(res)

s = '1'
n = 4 #number of times

for i in range(4-1):
    s = next_number(s)
    print(s)
