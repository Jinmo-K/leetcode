class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        scores = [0] * (N + 1)
        
        for truster, trustee in trust:
            scores[truster] -= 1
            scores[trustee] += 1
            
        for i in range(1, N + 1):
            if scores[i] == N - 1: return i
        
        return -1