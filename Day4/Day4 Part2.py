
with open('rawDataDayFour.txt', 'r') as file:
    raw_data = file.read()

lines = raw_data.strip().split('\n')
grid = [list(line.strip()) for line in lines]

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    diagonals = [
        (-1, -1),  # Up-left to down-right
        (-1, 1)    # Up-right to down-left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':  
                is_xmas = True
                for dir in diagonals:
                    seq = ''
                    for k in [-1, 0, 1]:
                        x = r + k * dir[0]
                        y = c + k * dir[1]
                        if not is_valid(x, y):
                            is_xmas = False
                            break
                        seq += grid[x][y]
                    if seq not in ['MAS', 'SAM']:
                        is_xmas = False
                        break
                if is_xmas:
                    count += 1

    return count

result = count_xmas(grid)
print(result)
