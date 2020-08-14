class KthLargest {
  int K;
  PriorityQueue<Integer> pq = new PriorityQueue<>();

  public KthLargest(int k, int[] nums) {
      K = k;
      for (int num : nums) {
          add(num);
      }
  }
  
  public int add(int val) {
      pq.add(val);
      if (pq.size() > K) {
          pq.poll();
      }
      return pq.peek();
  }
}