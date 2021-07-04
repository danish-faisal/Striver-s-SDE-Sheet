# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pts - left & right
        left = right = 0
        obj = {}
        # to store max len of such string
        cnt = 0
        while right<len(s):
            # skip to character next to 'right', when a repeated character is seen
            if s[right] in obj and left<=obj[s[right]]:
                left = obj[s[right]] + 1
            
            # calc length between left-right for len of str with no-pepeated chars
            if right - left + 1 > cnt:
                cnt = right - left + 1
            
            # add the seen characters to Hashmap
            obj[s[right]]=right
            right += 1

        return cnt