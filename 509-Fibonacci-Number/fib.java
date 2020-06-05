class Solution {
  public int fib(int N) {
    int f1 = 1;
    int f2 = 0;

    for (int i = 0; i < N; i++) {
      int prev = f1;
      f1 = f1 + f2;
      f2 = prev;
    }
    return f2;
  }
}