# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals/pairs in ascending order of 1st element of the pair
        intervals.sort(key = lambda x: x[0])
        # initialize result with 1st pair
        result = [intervals[0]]
        # start iterating from 1st index
        for interval in intervals[1:]:
            # check if the 2nd element of current last pair in result-array is >= 1st element of the current pair in intervals-array iteration
            if result[-1][1] >= interval[0]:
                # if yes replace the 2nd element in current last pair of result-array with 1st element of curr-pair in iteration
                result[-1][1]=max(interval[1],result[-1][1])
            # if no just append the current-pair to result-array as a new pair
            else:
                result.append(interval)
        return result