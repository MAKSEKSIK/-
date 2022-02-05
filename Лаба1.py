a = input()
b = input()
c = input()
d = input()
maxs = -1000000
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if (a > maxs and a % 2 == 0):
    maxs = a
if (b > maxs and b % 2 == 0):
    maxs = b
if (c > maxs and c % 2 == 0):
    maxs = c
if (d > maxs and d % 2 == 0):
    maxs = d
print(maxs)