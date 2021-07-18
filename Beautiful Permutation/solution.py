n = int(input() or 1000000)

from time import time
begin=time()
if n == 2 or n == 3:
    print('NO SOLUTION')
else:
    print(*range(2, n+1, 2), *range(1, n+1, 2))

print(time() - begin)