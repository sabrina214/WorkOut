def trailing_zeros(n):
    # count the number of times you are able to factor out 10
    # Thus, the it is necessary to only figure out the number of 5's in n!.

    # Now one more thing to observe is that numbers will not have just single number 
    # of 5 as factor, else solution would be as simple as obtaining the quotient of (n / 5).
    # Specifically, for each multiple of 5**i; i > 0; the number will have i number of 5's
    # For eg; 5**2 = 25             5**3 = 125
    # 25 * 2: two 5's               125 * 2: three 5's
    # 25 * 3: two 5's               125 * 3: three 5's
    # thus we need to accumulate these quotients as well for all powers of 5 less than n

    powered_up_5 = 5

    zeros = 0
    while powered_up_5 <= n:
        zeros += (n // powered_up_5)
        powered_up_5 *= 5
    return zeros

print(trailing_zeros( int(input())))