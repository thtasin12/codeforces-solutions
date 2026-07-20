n = int(input())

count = 0

for i in range(n):

    line = input().split()

    Petya = int(line[0])
    Vasya = int(line[1])
    Tonya = int(line[2])

    if Petya + Vasya + Tonya >= 2:
        count += 1

print(count)