"""
for / while
0 10
1 9
2 8
3 7
5 5
6 4
7 3
8 2
"""
for regressivo in range(10, 1, -1):
    print(regressivo)

for progressivo, regressivo in enumerate(range(10, 1, -1)):
    print(progressivo, regressivo)
