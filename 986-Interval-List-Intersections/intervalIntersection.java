class Solution {
  public int[][] intervalIntersection(int[][] A, int[][] B) {
      int A_ptr = 0;
      int B_ptr = 0;
      List<int[]> intersection = new ArrayList<>();
      
      while (A_ptr < A.length && B_ptr < B.length) {
          int A_start = A[A_ptr][0];
          int A_end = A[A_ptr][1];
          int B_start = B[B_ptr][0];
          int B_end = B[B_ptr][1];
          
          int start = Math.max(A_start, B_start);
          int end = Math.min(A_end, B_end);
          
          if (start <= end) {
              intersection.add(new int[]{start, end});
          }
          
          if (A_end > B_end) {
              B_ptr++;
          } else {
              A_ptr++;
          }
      } 
      
      return intersection.toArray(new int[intersection.size()][2]);
  }
}
