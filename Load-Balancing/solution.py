def solve(arr):
    w1 = 0
    w2 = 0
    w3 = 0

    total_time = sum(arr)

    # each worker can at most be tasked with tasks totalling "thresh"
    thresh = total_time // 3

    i = 0
    j = len(arr) - 1
    temp = 0

    while True:
        temp = arr[i] + w1
        if temp >= thresh:
            break
        w1 = temp
        i += 1

    while True:
        temp = arr[j] + w3
        if temp >= thresh:
            break
        w3 = temp
        j -= 1

    w2 = sum(arr[i + 1 :j])

    return w1 == w2 and w2 == w3

arr = [int(i) for i in input().split()]
print(solve(arr))
