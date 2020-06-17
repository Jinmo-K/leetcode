class Solution:
  def dailyTemperatures:
      stack = []
          ans = [0]*len(T)
          
          for i, temp in enumerate(T):
              while stack and temp > T[stack[-1]]:
                  pos = stack.pop()
                  ans[pos] = i - pos
              stack.append(i)
          
          return ans