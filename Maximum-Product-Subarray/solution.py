def max_product_subarray(arr):
    max_prod = arr[0]
    max_so_far = arr[0]
    min_so_far = arr[0]

    for i in arr[1:]:
        if i < 0:
            min_so_far, max_so_far = max_so_far, min_so_far
        min_so_far = min(i, min_so_far * i)
        max_so_far = max(i, max_so_far * i)

        max_prod = max(max_prod, max_so_far)
    
    return max_prod

arr = [float(i) for i in input().split()]
print(max_product_subarray(arr))
