class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        index = 0
        while zeros > 0 or ones > 0 or twos > 0:
            if zeros > 0:
                nums[index] = 0
                index += 1
                zeros -= 1
                continue
            elif ones > 0:
                nums[index] = 1
                index += 1
                ones -= 1
                continue
            else:
                nums[index] = 2
                index += 1
                twos -= 1