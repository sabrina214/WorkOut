def is_twin(s):
    return not s & 1


def deliver_twins(n, s):
    s //= 2
    a, b = [], []
    while n > 0:
        if n <= s:
            a.append(n)
            s -= n
        else:
            b.append(n)
        n -= 1
    return a, b

n = int(input())
s = sum(range(1, n+1))
maximum_effort = is_twin(s)

if maximum_effort:
    print('YES')
    chinki, minki = deliver_twins(n, s)

    print(len(chinki))
    print(*chinki)
    print(len(minki))
    print(*minki)
else:
    print('NO')