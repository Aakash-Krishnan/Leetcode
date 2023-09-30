class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        
        arr = []
        arr.append(intervals[0])
        for i in range(1, len(intervals)):
            if not(arr[-1][1] < intervals[i][0] or intervals[i][1] < arr[-1][0]):
                arr[-1][0] = min(arr[-1][0], intervals[i][0])
                arr[-1][1] = max(arr[-1][1], intervals[i][1])
            else:
                arr.append(intervals[i])
        
        return arr