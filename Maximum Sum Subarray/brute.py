def brute(a):
    # considering subarray sizes one at a time
    n = len(a)
    max_so_far = a[0] - 1
    p, q = 0, 0

    for sub_size in range(1, n+1):
        for i in range((n-sub_size)+1):
            subarr_sum = sum(a[i: sub_size + i])
            if subarr_sum > max_so_far:
                p, q = i, sub_size + i
                max_so_far = subarr_sum
    return max_so_far, a[p:q]
