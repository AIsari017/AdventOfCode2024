with open('Day4/rawDataDayFour.txt', 'r') as file:
    raw_data = file.read()

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "MAS"
    target_len = len(target)
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1), # down-left
        (0, -1), # left
        (-1, 0), # up
        (-1, -1),# up-left
        (-1, 1)  # up-right
    ]
    
    count = 0
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == target[0]:  
                for dr, dc in directions:
                    x, y = r, c
                    match = True
                    for k in range(target_len):
                        if not is_valid(x, y) or grid[x][y] != target[k]:
                            match = False
                            break
                        x += dr
                        y += dc
                    if match:
                        count += 1
    
    return count

lines = raw_data.strip().split('\n')
grid = [list(line.strip()) for line in lines]

result = count_xmas(grid)
print(result) 


