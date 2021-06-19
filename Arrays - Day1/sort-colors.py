# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        # count the no. of 0s 1s and 2s
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        index = 0
        while zeros > 0 or ones > 0 or twos > 0:
            # start placing 0s from 0 index to the no. of 0s present
            if zeros > 0:
                nums[index] = 0
                index += 1
                zeros -= 1
                continue
            # after 0s are placed, start placing 1s untile they're exhausted
            elif ones > 0:
                nums[index] = 1
                index += 1
                ones -= 1
                continue
            # start with 2s after 1s
            else:
                nums[index] = 2
                index += 1
                twos -= 1