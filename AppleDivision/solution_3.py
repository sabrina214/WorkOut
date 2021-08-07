from sys import stdin, stdout


def min_diff(a):
    total_sum = sum(a)
    best = 1e9
    for i in range(1<<n):
        sum_a = 0
        for j in range(n):
            if i & (1<<j):
                sum_a += a[j]
        best = min(best, abs(total_sum - 2 * sum_a))
    return best


if __name__ == '__main__':
    n = int(stdin.readline())
    a = [int(i) for i in stdin.readline().split()]
    stdout.write(str(int(min_diff(a))))
