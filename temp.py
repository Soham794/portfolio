grid = [[]]

from collections import defaultdict

dict = defaultdict(list)

for row in grid:
    for col in row:
        dict[grid[row][col]].append([row, col])


