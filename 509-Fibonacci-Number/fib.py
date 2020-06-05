class Solution:
  def fib(self, N):
    f1, f2 = 1, 0
    for _ in range(N):
      f1, f2 = f1 + f2, f1
    return f2