def solve(s):
    ans = 0
    count_a = 0

    if s.startswith('aaa') or s.endswith('aaa'):
        return -1
    
    if s == '':
        return 2

    n = len(s)
    if n == 1:
        if s == 'a':
            return 1
        else:
            return 4
    
    for c in s:
        if c == 'a':
            count_a += 1
        else:
            if count_a == 0:
                ans += 2
            elif count_a == 1:
                count_a += 1
                ans += 1
            elif count_a == 2:
                count_a = 0
            else:
                return -1
    
    if s[-1] != 'a':
        ans += 2
    elif s[-2] != 'a':
        ans += 1
    
    return ans

bogus = input()
print(solve(bogus))
