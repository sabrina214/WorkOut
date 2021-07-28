def get_bit(line, bit_pos, state, powers):
    k = powers[bit_pos-1]

    # toggling b/w 1 and 0
    if line % (k // 2) == 0:
        bit = 1 - (state[bit_pos - 1])
        state[bit_pos - 1] = bit
        # checking if pattern should reverse, in that case we again toggle the bit value
        if line % k == 0:
            state[bit_pos - 1] = 1 - bit
            bit = 1 - bit
        return str(bit)
    # if bit value does not change use bit value of previous gray-code
    else:
        return str(state[bit_pos-1])


def gray_codes(n):
    from random import randrange

    lines = 1 << n

    # state will hold the previous gray-code(stored in reverse order,
    # because that was a bit intuitive while accessing it).
    # We can start with any valid n-bit gray code.    
    state = [randrange(2) for _ in range(n)]

    # powers is used as a lookup for powers of 2
    powers = [1 << i for i in range(1, n + 1)]

    for line in range(lines):
        gray_code = ''
        for bit_pos in range(n, 0, -1):
            gray_code += get_bit(line, bit_pos, state, powers)
        print(gray_code)


n = int(input())
gray_codes(n)
