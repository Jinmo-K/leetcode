class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Check for duplicates
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        
        lengths = set()
        points = [p1] + [p2] + [p3] + [p4]
        
        for p in range(3):
            for q in range(p + 1, 4):
                lengths.add(self.calculateDistance(points[p], points[q]))
        return len(lengths) == 2
        
    
    def calculateDistance(self, point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5