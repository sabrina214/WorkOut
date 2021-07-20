def get_element(row, col):
    '''
    Considering 1-indexed matrix.

    An approach would be to determine the max of row and col
    the motivation behind it is each layer of spiral has maximum
    element as square of that layer number and all the elements 
    in that layer would be those numbers contained between
    max number of previous layer exclusive and max number of present 
    layer inclusive.

    For example; (3, 2) means we need to look at layer 3
    max value at this layer would be 3*3 = 9
    max value of previous layer = 2*2 = 4
    values in layer 3 = {5,6,7,8,9}

    Now only thing left is to figure out the value of element
    relative to our max element. This is possible because the elements
    in a layer is ordered in some way according to whether the layer number
    is odd or even.

    for odd numbered layers, max values lies in (1, layer_no)
    for even numbered layers, max values lies in (layer_no, 1)

    for odd numbered layer:
        desired_value_at_row_col = (layer_no)**2 - (row - 1) + (col - layer_no)
    for even numbered layer:
        desired_value_at_row_col = (layer_no)**2 - (row - layer_no) + (col - 1)
    '''
    
    layer = max(x, y)
    max_element = layer * layer
    
    return max_element - (row - 1) + (col - layer) if layer & 1 else max_element + (row - layer) - (col - 1)

    # if layer & 1:
    #     return max_element - (row - 1) + (col - layer)
    # else:
    #     return max_element + (row - layer) - (col - 1)

for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]

    print(get_element(x, y))
    print()

    n = max(x, y)
    for x in range(1, n+1):
        for y in range(1, n+1):
            print(get_element(x, y), end="\t")
        print()

