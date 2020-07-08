class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:    
        min_diff = float('inf')
        # Convert each timepoint to minutes and sort them
        minutes = sorted(map(self.calculateMinutes, timePoints))
        # In order to calculate difference between first and last
        # values, add minutes[0] + 24 hr to the end of array
        minutes.append(minutes[0] + 24*60)
        # Iterate through, calculating differences and maintaining the min
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        return min_diff
        
    def calculateMinutes(self, time):
        hr, mins = time.split(':')
        return int(hr)*60 + int(mins)