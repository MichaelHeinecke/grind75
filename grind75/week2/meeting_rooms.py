from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        """
        @param intervals: an array of meeting time intervals
        @return: if a person could attend all meetings
        """
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False

        return True
