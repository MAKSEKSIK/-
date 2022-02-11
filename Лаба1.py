a = int(input())
b = int(input())
c = int(input())
d = int(input())
maxs = -1000000
if (a > maxs and a % 2 == 0):
    maxs = a
if (b > maxs and b % 2 == 0):
    maxs = b
if (c > maxs and c % 2 == 0):
    maxs = c
if (d > maxs and d % 2 == 0):
    maxs = d
print(maxs)
