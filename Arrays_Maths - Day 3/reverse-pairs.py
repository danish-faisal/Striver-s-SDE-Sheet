# https://leetcode.com/problems/reverse-pairs/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # static count to count no. of reverse pairs found
        cnt = 0

        # left and right will be sorted
        def merge(left, right):
            nonlocal cnt
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    i += 1
                # a pair is found such tha nums[i]>2*nums[j] and i<j
                else:
                    # as the array is sorted, so on finding one such element ->
                    # move the 'j' pointer as we need not compare it with rest of the elements in 'left' array
                    # so increment the count by number of remaning element in left array which we need not compare with the element 'j' was pointing to
                    cnt += len(left)-i
                    j += 1

            # returning merged sorted array combining left ad right
            return sorted(left+right)


        def mergeSort(A):
            if len(A) <= 1:
                return A
            # inplace division of array and callinf mergesort on each division
            # then merge will be called on each set of arrays (will be sorted as they reach on higher levels)
            return merge(mergeSort(A[:(len(A) + 1) // 2]), mergeSort(A[(len(A) + 1) // 2:]))

        mergeSort(nums)
        return cnt