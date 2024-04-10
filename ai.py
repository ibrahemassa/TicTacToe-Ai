AI = 'O'
HUMAN = 'X'

def win(grid, player):
    if player not in ('X', 'O'):
        return False
    #Check for columns
    for i in range(3):
        if grid[i] == player and grid[i+3] == player and grid[i+6] == player:
            return True
    
    #Check for rows
    for i in range(3):
        cur_row = i * 3
        if grid[cur_row] == player and grid[cur_row+1] == player and grid[cur_row+2] == player:
            return True
    
    #Check for diagonals
    if grid[0] == player and grid[4] == player and grid[8] == player or \
    grid[2] == player and grid[4] == player and grid[6] == player:
        return True
    

def minmax(grid, player, index=0):
    #Get all empty cells in the grid
    empty_indices = [i for i in range(9) if isinstance(grid[i], int)]

    #Check if we reached a winning state and returning respective score
    if win(grid, HUMAN):
        return [index, -1]
    elif win(grid, AI):
        return [index, 1]
    elif not empty_indices:
        return [index, 0]
    
    #Check for all avilable moves and thier respective score
    avilable_moves = []
    for i in empty_indices:
        grid[i] = player
        
        if player == AI:
            cur = minmax(grid, HUMAN, i)
        else:
            cur = minmax(grid, AI, i)
        grid[i] = cur[0]

        avilable_moves.append(cur)

        #Determining the best move
        best_move = avilable_moves[0] or [0, 0]
        if player == AI:
            for move in avilable_moves:
                if best_move[1] < move[1]:
                    best_move = move[:]
        else:
            for move in avilable_moves:
                if best_move[1] > move[1]:
                    best_move = move[:]
        return best_move
