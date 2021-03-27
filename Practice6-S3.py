
num = int(input())
a = 0
x = num

while True:
    x //= 10 
    a += 1
    if x == 0: 
        break

x = num 
d = 1
s = 0

while True:
    b = x % (10 ** d)
    c = (b - b % (10 ** (d-1))) / (10 ** (d-1))
    s = s + c ** a
    d += 1
    print(c)
    if b == x:
        break

if s == num:
    print('Yes')
else:
    print('No')
