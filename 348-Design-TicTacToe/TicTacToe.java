class TicTacToe {
  private int[] cols;
  private int[] rows;
  private int d1;
  private int d2;
  private int size;

  /** Initialize your data structure here. */
  public TicTacToe(int n) {
      size = n;
      cols = new int[n];
      rows = new int[n];
  }
  
  /** Player {player} makes a move at ({row}, {col}).
      @param row The row of the board.
      @param col The column of the board.
      @param player The player, can be either 1 or 2.
      @return The current winning condition, can be either:
              0: No one wins.
              1: Player 1 wins.
              2: Player 2 wins. */
  public int move(int row, int col, int player) {
      int inc = (player == 1) ? 1 : -1;
      rows[row] += inc;
      cols[col] += inc;
      if (row + col == size - 1) {
          d1 += inc;
      }
      if (row == col) {
          d2 += inc;
      }
      if (Math.abs(rows[row]) == size || 
          Math.abs(cols[col]) == size || 
          Math.abs(d1) == size || 
          Math.abs(d2) == size) 
      {
          return player;
      }
      return 0;
  }
}