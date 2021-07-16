def find_missing(a, n):
    count = [0] * (n + 1)
    for i in a:
        count[i] += 1
    for i in range(1, n+1):
        if count[i] == 0:
            return i
