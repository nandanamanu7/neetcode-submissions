class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        start = intervals[0][0]
        stop = intervals[0][1]

        for i in range(1, len(intervals)):
            newStart = intervals[i][0]
            newStop = intervals[i][1]
            if (stop >= newStart):
                stop = max(stop,newStop)
            else:
                merged.append([start, stop])
                start = newStart
                stop = newStop
            
        if intervals:
            merged.append([start,stop])
            
        return merged
            
        

        