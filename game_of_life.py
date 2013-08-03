#!python

# Rules
# 1) Any live cell with < 2 dies
# 2) Any live cell with 2-3 live neighbors lives
# 3) Any live cell with > 3 dies
# 4) Any dead cell with 3 becomes alive

# 2D Array of bool
# Iterate over board, determine next generation
# Determine whether cells are alive or dead

from GOL.Helpers import index
from GOL.CellRules import next_state

#def index(l):
#  return zip(l, range(len(l)))
    

class GameOfLife:
  def __init__(self, rows, cols):
    self.board = [[False for c in range(cols)] for r in range(rows)]

  def set_living_cells(self, cells):
    for row, col in cells:
      self.board[row][col] = True

  def cell_alive(self, position):
    row, col = position
    return self.board[row][col]

  def advance(self):
    self.board = [[next_state(self.board, (ri,ci))
      for _, ci in index(row)]
      for row, ri in index(self.board)]

def main():
  pass

if __name__ == '__main__':
  main()
