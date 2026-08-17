# n, k = map(str, input().split())
# k = int(k)
# for i in range(k):
#     if n[-1] == "0":n = str(int(n) // 10)
#     else:n = str(int(n) - 1)

# print(n)


n, k = map(int, input().split())
for _ in range(k):
    if n % 10 == 0: n //= 10
    else: n -= 1

print(n)