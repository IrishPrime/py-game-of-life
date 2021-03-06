import unittest
from game_of_life import GameOfLife
from GOL import CellRules

class TestGameOfLife(unittest.TestCase):
  def setUp(self):
    pass

  def test_live_cell_with_lt_2_neighbors_dies(self):
    board = [[False, True, False]]
    result = CellRules.next_state(board, (0, 1))
    self.assertFalse(result)

  def test_live_cell_with_2_neighbors_lives(self):
    board = [[True, True, True]]
    result = CellRules.next_state(board, (0, 1))
    self.assertTrue(result)

  def test_live_cell_with_2_neighbors_lives_2(self):
    board = [[False, False, True],
             [True,  True,  True]]
    result = CellRules.next_state(board, (1, 1))
    self.assertTrue(result)

  def test_live_cell_with_3_neighbors_lives(self):
    board = [[False, True, False],
             [True,  True, True]]
    result = CellRules.next_state(board, (1, 1))
    self.assertTrue(result)

  def test_live_cell_with_gt_3_neighbors_dies(self):
    board = [[True,  True, False],
             [True,  True, True]]
    result = CellRules.next_state(board, (1, 1))
    self.assertFalse(result)

  def test_dead_cell_with_2_neighbors_stays_dead(self):
    board = [[True,  True, False],
             [True, False, True]]
    result = CellRules.next_state(board, (0, 2))
    self.assertFalse(result)

  def test_dead_cell_with_3_neighbors_lives(self):
    board = [[True,  True, False],
             [True,  True, True]]
    result = CellRules.next_state(board, (0, 2))
    self.assertTrue(result)

  def test_can_build_game_of_life_with_initial_state(self):
    game = GameOfLife(10, 10)
    game.set_living_cells([(3,3)])
    self.assertTrue(game.cell_alive((3,3)))

  def test_that_board_advances_to_next_state(self):
    game =GameOfLife(10, 10)
    game.set_living_cells([(3,3)])
    game.advance()
    self.assertFalse(game.cell_alive((3,3)))

if __name__ == '__main__':
  unittest.main()
