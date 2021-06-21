# https://leetcode.com/problems/find-the-duplicate-number/submissions/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) time & O(1) space | Slow pointer-Fast pointer tech | Hare & Tortoise tech
        slow = nums[0]
        fast = nums[0]
        
        # find the point where the slow pointer and the fast pointer meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # initializing slow ptr to start & fast is at the point it stopped from the above step
        #  the point where the slow and fast ptr meet again is the duplicate point/element
        slow = nums[0]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return fast
    

        # O(n) time & O(n) space
        # obj = {}
        # for num in nums:
        #     if num in obj:
        #         return num
        #     obj[num] = 1
        # return -1