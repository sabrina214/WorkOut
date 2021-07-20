def clash_of_knights(n):
    '''
    for each n x n board there can be at most five 
    different positions with distinct attack radius: 2, 3, 4, 6, 8
    
    Number of clashes with second knight if first knight is placed at:
    Clash Position                      Number of clash positions
    -------------------------------------------------------------
    1. corner                                       2
    
    2. adjacent to corner and edge                  3 
    
    3. adjacent to corner diagonally,               4
    and also edge positions not 
    adjacent to corners

    4. consider the inner board of                  6
    (n-2) x (n-2). Positions that
    would lie in the border of this
    board except the corners.

    5. consider the inner board of                  8
    (n-4) x (n-4). All the positions
    covered by this area. 
    '''
    for k in range(1, n+1):
        # knights are not romantic enough to squeeze in a single place
        if k == 1:
            print(0)
        elif k == 2:
            # world of peace
            # (4 x 3) / 2
            print(6)
        elif k == 3:
            # (8 x 7) / 2
            print(28)
        
        # for rest all cases,i.e k > 3, number of attack positions associated
        # with corner and adjacent positions would not vary with increasing 
        # board size, i.e if a board is never going to have more than four corners,
        # and also each corner will never have more than two adjacent positions
        # and u get the gist
        else:
            total_pos = k**2

            twos = (4 * (total_pos - 3)) // 2
            threes = (8 * (total_pos - 4)) // 2
            fours = (((4 + (k - 4) * 4)) * (total_pos - 5)) // 2
            sixes = (((k - 4) * 4) * (total_pos - 7)) // 2
            eights = (((k - 4) ** 2) * (total_pos - 9)) // 2
            safe_possible_pos = twos + threes + fours + sixes+ eights
            
            print(safe_possible_pos)


n = int(input())
clash_of_knights(n)
