for i in range(1, 6):
    row = list(map(int, input().split()))
    for j in range(1, 6):
        if row[j-1] == 1:
            r = i
            c = j

moves = abs(r-3) + abs(c-3)
print(moves)