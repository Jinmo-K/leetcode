class Solution {
  public int heightChecker(int[] heights) {
    int[] counts = new int[101];
    int ptr = 0;
    int num_moves = 0;
    
    for (int height : heights) {
      counts[height]++;
    }
    
    for (int height = 0; height < counts.length; height++) {
      for (int i = 0; i < counts[height]; i++) {
        if (height != heights[ptr]) {
          num_moves++;
        }
        ptr++;
      }
    }
    
    return num_moves;
  }
}