class Solution {
  public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
      int[][] points = {p1, p2, p3, p4};
      Map<Integer, Integer> distances = new HashMap<>();
      
      for (int i = 0; i < 3; i++) {
          for (int j = i + 1; j < 4; j++) {
              int dist =  calculateDist(points[i], points[j]);
              if (dist == 0) return false;
              distances.put(dist, distances.getOrDefault(dist, 0));
          }
      }
      return distances.size() == 2;
  }
  
  public int calculateDist(int[] a, int[] b) {
      return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
  }
  
}