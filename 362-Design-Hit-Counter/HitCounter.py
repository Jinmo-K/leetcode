class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Circular array holding elements of [timestamp, count] 
        self.arr = [[] for _ in range(300)]
        # Index of the oldest timestamp
        self.oldest = 0
        # Current position in the array
        self.curr = 0
        # Number of counts within the last 5 minutes
        self.count = 0
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.removeOld(timestamp)
        # For counting multiple hits with same timestamp
        if self.arr[self.curr] and self.arr[self.curr][0] == timestamp:
            self.arr[self.curr][1] += 1
        else:
            # New timestamp - increment the position in the array, if needed
            # before counting a hit
            if self.arr[self.curr]:
                self.curr += 1 % 300
            self.arr[self.curr] = [timestamp, 1]
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.removeOld(timestamp)
        return self.count
        
    def removeOld(self, timestamp):
        # Starting from oldest timestamp, iterate through, erasing
        # ones that are older than 5 minutes and removing their count
        # from the total 
        while self.arr[self.oldest] and self.arr[self.oldest][0] <= timestamp - 300:
            self.count -= self.arr[self.oldest][1]
            self.arr[self.oldest] = []
            # oldest cannot go past curr
            if self.oldest != self.curr:
                self.oldest += 1

