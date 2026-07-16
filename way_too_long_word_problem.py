a = input()
b = len(a)
c = " "

if b > 10:
    c = a[0] + str(b - 2) + a[-1]
    print(c)
else:
    print(a)