class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0
        counts = {}
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                counts[s] = counts.get(s, 0) + 1
                counts[g] = counts.get(g, 0) - 1
                
                if counts[s] <= 0: 
                    cows += 1
                if counts[g] >= 0:
                    cows += 1
    
        return f'{bulls}A{cows}B'
            
            