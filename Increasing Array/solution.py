n = int(input())

arrey_bhai = [int(i) for i in input().split()]

no_of_moves = 0

for i in range(n-1):
    if arrey_bhai[i] > arrey_bhai[i+1]:
        no_of_moves += arrey_bhai[i] - arrey_bhai[i+1]

print(no_of_moves)