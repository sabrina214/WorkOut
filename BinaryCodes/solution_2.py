'''
Came up with this solution while solving gray codes. Thus a larger part of it 
is inspired from the code of gray-code solution. Might want to check out that
before this, if: this one's not intuitive else: pass
'''


def get_bit(line, bit_pos, state, powers):
    k = powers[bit_pos - 1]

    if line % (k // 2) == 0:
        bit = 1 - state[bit_pos - 1]
        state[bit_pos - 1] = bit
        return str(bit)
    else:
        return str(state[bit_pos-1])


def binary_codes(n):
    from random import randrange

    lines = 1 << n
    state = [randrange(2) for _ in range(n)]
    powers = [1 << i for i in range(1, n + 1)]

    for line in range(lines):
        binary_code = ''
        for bit_pos in range(n, 0, -1):
            binary_code += get_bit(line, bit_pos, state, powers)
        print(binary_code)


n = int(input())
binary_codes(n)