n = int(input())
s = input()

a = 0
d = 0

for char in s:
    if char == "A":
        a += 1
    elif char == "D":
        d += 1

if a > d:
    print("Anton")
elif a < d:
    print("Danik")
elif a == d:
    print("Friendship")