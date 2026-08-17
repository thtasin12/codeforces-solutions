n = int(input())
current = 0
maximum = 0

for _ in range(n):
    a, b = map(int, input().split())

    current = current - a + b
    maximum = max(current, maximum)

print(maximum)