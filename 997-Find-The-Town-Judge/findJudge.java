class Solution {
  public int findJudge(int N, int[][] trust) {
      int[] scores = new int[N+1];
      
      for (int[] relation : trust) {
          scores[relation[0]]--;
          scores[relation[1]]++;
      }
      
      for (int i = 1; i < N + 1; i++) {
          if (scores[i] == N - 1) return i;
      }
      
      return -1;
  }
}