def permute(s, n):
    if len(s) == 1: return s
    all_permutations = []
    for i in range(n):
        c = s[i]
        # if similar characters are present then we need to consider only one
        # list.index() method returns the index of first element matched
        # so a repeating character encountered later can be distinguished by this hack
        # because it's index won't be returned, it would be the index of first such character
        # thus we simply skip such repeating characters from consideration;)
        if s.index(c) != i: continue
        for permuted in permute(s[:i] + s[i+1:], n - 1):
            all_permutations.append(c + permuted)
    return all_permutations

s = input()
n = len(s)

permutations = permute(s, n)
permutations.sort()

print(len(permutations))
for i in permutations:
    print(i)