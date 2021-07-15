# https://leetcode.com/problems/subarray-sum-equals-k/

# have to return total no. of occurences of sub-arrays that sums up to k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # resultant variable
        cnt = 0
        # sum variable
        tsum = 0
        # hashmap - to store the no. of occurences of a sub-array sum and no.d in the array
        obj = {}
        # if array contains 0 or a sequence like -4,4 or 1,2,1,-4 occurs that results in 0
        obj[0]=1
        for i in nums:
            tsum += i
            # a sub-array found -> add to the count
            if tsum-k in obj:
                # https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book
                # https://leetcode.com/problems/subarray-sum-equals-k/discuss/535507/Explanation-to-why-map.get(sum-k)-is-done-than-count%2B%2B
                cnt+=obj[tsum-k]
            # add the sum to the map
            obj[tsum]=1 + (obj[tsum] if tsum in obj else 0)
        return cnt