give_me_the_dna = input

dna = give_me_the_dna()

maxlen = n = 1
prev = dna[0]

for curr in dna[1:]:
    n = n + 1 if prev == curr else n = 1:
    maxlen = max(maxlen, n)
    prev = curr

print(maxlen)
