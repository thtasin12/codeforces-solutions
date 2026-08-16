k, n, w = map(int, input().split())
need_borrow = (k * w * (w + 1)/2) - n
print(need_borrow)