import os
import ai
import game
grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game.print_grid(grid)

while not ai.win(grid, 'X') and not ai.win(grid, 'O'):
    row = int(input("Enter row number: "))
    column = int(input("Enter row number: "))
    index = (row-1) * 3 + (column-1)
    
    if index > len(grid) - 1:
        print('Out of index!')
        print('You lost your turn')
    else:
        if isinstance(grid[(row-1) * 3 + (column-1)], int):
            grid[(row-1) * 3 + (column-1)] = 'X'
        else:
            print('AlREADY TAKEN!!!!')
            print('You lost your turn')

    ai_move = ai.minmax(grid, ai.AI)
    grid[ai_move[0]] = 'O'
    os.system('cls')
    game.print_grid(grid)

if ai.win(grid, 'X'):
    print('You Won!!')
elif ai.win(grid, 'O'):
    print('You lost')
else:
    print('Tie')

