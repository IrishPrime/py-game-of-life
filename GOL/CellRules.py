transforms = [(-1,-1), (0,-1), (1,-1),
              (-1,0),          (1,0),
              (-1,1),  (0,1),  (1,1)]

def next_state(board, pos):
  row, col = pos
  cell_alive = board[row][col]

  neighbors = [transform(pos, t) for t in transforms]
  state = [board[n[0]][n[1]] for n in neighbors if in_board(board, n)]
  living_neighbors = state.count(True)

  return living_neighbors == 3 or (cell_alive and living_neighbors == 2)

def transform(pos, transform):
  return (pos[0] + transform[0], pos[1] + transform[1])

def in_board(board, pos):
  return pos[0] < len(board) and pos[1] < len(board[pos[0]]) and \
         pos[0] >= 0 and pos[1] >= 0

