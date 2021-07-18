n = int(input())

while True:
    print(n, end=' ')
    if n == 1: break
    n = n * 3 + 1 if n & 1 else n >> 1
