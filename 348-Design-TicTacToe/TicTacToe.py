class TicTacToe:
  def __init__(self, n: int):
    """
    Initialize your data structure here.
    """
    self.rows = [0] * n
    self.cols = [0] * n
    self.d1 = 0              
    self.d2 = 0        
    self.n = n

  def move(self, row: int, col: int, player: int) -> int:
    """
    Player {player} makes a move at ({row}, {col}).
    @param row The row of the board.
    @param col The column of the board.
    @param player The player, can be either 1 or 2.
    @return The current winning condition, can be either:
            0: No one wins.
            1: Player 1 wins.
            2: Player 2 wins.
    """
    inc = 1 if player == 1 else -1
        
    self.rows[row] += inc
    self.cols[col] += inc
    if row == col:
      self.d2 += inc
    if row + col == self.n - 1:
      self.d1 += inc
    if self.n in [abs(self.rows[row]), abs(self.cols[col]), abs(self.d1), abs(self.d2)]:
      return player
    return 0