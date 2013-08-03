#!python

# Rules
# 1) Any live cell with < 2 dies
# 2) Any live cell with 2-3 live neighbors lives
# 3) Any live cell with > 3 dies
# 4) Any dead cell with 3 becomes alive

# 2D Array of bool
# Iterate over board, determine next generation
# Determine whether cells are alive or dead

class CellRules:
  transforms = [(-1,-1), (0,-1), (1,-1),
                (-1,0),          (1,0),
                (-1,1),  (0,1),  (1,1)]

  def next_state(board, pos):
    cell_alive = board[pos[0]][pos[1]]

    neighbors = [CellRules.transform(pos, t) for t in CellRules.transforms]
    state = [board[n[0]][n[1]] for n in neighbors if CellRules.in_board(board, n)]
    living_neighbors = state.count(True)

    return living_neighbors == 3 or (cell_alive and living_neighbors == 2)

  def transform(pos, transform):
    return (pos[0] + transform[0], pos[1] + transform[1])

  def in_board(board, pos):
    return pos[0] < len(board) and pos[1] < len(board[pos[0]]) and \
           pos[0] >= 0 and pos[1] >= 0


def main():
  pass

if __name__ == '__main__':
  main()
