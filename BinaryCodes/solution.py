def show(binary):
    for i in binary:
        print(i, end='')
    print()


def add(arr, i):
    if arr[i]:
        arr[i] = 0
        add(arr, i - 1)
    else:
        arr[i] = 1
        return 0

def binary_codes(n):
    binary = [0] * n

    for i in range(1 << n):
        show(binary)
        add(binary, n-1)
        
n = int(input())
binary_codes(n)
