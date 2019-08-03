from itertools import permutations
n, m = map(int, input().split())
x = list(map(int, input().split()))
for i in permutations(x, 2):
    if sum(i) == m:
        print('yes')
        break
else:
    print('no')
