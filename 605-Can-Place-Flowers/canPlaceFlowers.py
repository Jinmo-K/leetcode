class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and prev == 0 and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                n -= 1
                prev = 1
                if n == 0: return True
            else:
                prev = flowerbed[i]
        
        return n <= 0