"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = sorted(intervals,key=lambda x : x.start)
        n = len(intervals)
        for i in range(1,n):
            if arr[i].start<arr[i-1].end:
                return False
        return True