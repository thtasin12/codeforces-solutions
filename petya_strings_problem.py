s1 = input().strip().lower()
s2 = input().strip().lower()

if s1 > s2:
    print(1)
elif s2 > s1:
    print(-1)
else:
    print(0)