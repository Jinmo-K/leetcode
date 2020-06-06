class Solution {
  public int numberOfArithmeticSlices(int[] A) {
    int num_slices = 0;
    int add = 0;
    
    for (int i = 2; i < A.length; i++) {
      if (A[i] - A[i-1] == A[i-1] - A[i-2]) {
        add++;
        num_slices += add;
      }
      else {
        add = 0;
      }
    }
    
    return num_slices;
  }
}