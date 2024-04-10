from ai import win
grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_grid(grid):
    print('-------------')
    for i in range(0, 9, 3):
        print('| ', end='')
        for j in range(3):
            if isinstance(grid[i+j], int):
                cur = '_'
            else:
                cur = grid[i+j]
            print(cur, end=' | ')
        print('\n-------------')


