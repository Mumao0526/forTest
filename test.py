from collections import deque


a = [[0, 0], [0, 0]]

n = len(a)
b = [[0] * n for i in range(5)]

b[3][1] = 2
print(b)

print()

numS = [1, 0, 0]
k = 0
num = 0
for i in range(len(numS) - 1, -1, -1):
    num = num + int(numS[i]) * (10**i)
    k += 1
    print(num, (10**i))
print()

print(len(""))


haha = [2]
print(haha[-1])


sss = list("RRDDRRDRDR")
print(sss[2:])

[["1","1","1"],
 ["0","1","0"],
 ["1","1","1"]]