def palindrome_reorder(s):
    count = [0] * 26

    n = 0
    for c in s:
        count[ord(c) - 65] += 1
        n += 1
    
    palindrome = ''
    middle_str = ''
    flag = False

    for i in range(26):
        if count[i] & 1:
            if not flag:
                flag = True
                if n & 1:
                    if count[1] == 1:    
                        middle_str = chr(i+65)
                    else:
                        middle_str += chr(i+65) * count[i]
                else:
                    return 'NO SOLUTION'
            else:
                return 'NO SOLUTION'   
        else:
            palindrome += chr(i+65) * (count[i] // 2)

    if middle_str:
        palindrome += middle_str + palindrome[::-1]
    else:
        palindrome += palindrome[::-1]

    return palindrome

s = input()
print(palindrome_reorder(s))
