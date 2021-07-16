def kadane(a):
    # a button up cockroach
    max_sum = a[0]
    max_so_far = a[0]
    p, q, p_temp, q_temp = 0,0,0,0

    for i in range(1, len(a)):
        temp = max_so_far + a[i]
        if a[i] > temp:
            max_so_far = a[i]
            p_temp = i
            q_temp = i + 1
        else:
            max_so_far = temp
            q_temp = i + 1
        
        if max_sum < max_so_far:
            max_sum = max_so_far
            p, q = p_temp, q_temp

    return max_sum, a[p:q]
