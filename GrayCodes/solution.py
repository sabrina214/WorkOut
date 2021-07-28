def toggle_or_not(line, bit_pos, state, powers):
    k = powers[bit_pos-1]

    if line % (k // 2) == 0:
        bit = 1 - (state[bit_pos - 1])
        state[bit_pos - 1] = bit
        if line % k == 0:
            state[bit_pos - 1] = 1 - bit
            bit = 1 - bit
        return str(bit)
    else:
        return str(state[bit_pos-1])

def gray_codes(n):
    lines = 1 << n
    state = [0] * n

    powers = [2**i for i in range(1, n + 1)] 

    for line in range(lines):
        gray_code = ''
        for bit_pos in range(n, 0, -1):
            gray_code += toggle_or_not(line, bit_pos, state, powers)
        print(gray_code)

n = int(input())
gray_codes(n)