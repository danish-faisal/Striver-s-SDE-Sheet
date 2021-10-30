# https://leetcode.com/problems/implement-strstr/
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

class Solution:
    def strStr(self, txt: str, pat: str) -> int:
        M = len(pat)
        N = len(txt)
        
        if pat=="":     # edge-case: when the pattern to find is empty-string
            return 0

        # create lps[] that will hold the longest prefix suffix  values for pattern
        lps = [0 for i in range(M)]
        j = 0 # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(pat, M, lps)

        i = 0 # index for txt[]
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                # "Found pattern at index " + str(i-j)
                return i-j          # print instead of returning -> in case of searching all possible occurences
                j = lps[j-1]        # to continue after printing

            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters, they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1

    def computeLPSArray(self, pat, M, lps):
        len = 0 # length of the previous longest prefix suffix

        # lps[0] is always 0
        i = 1

        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i]==pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                # This is tricky. Consider the example. AAACAAAA and i = 7.
                # The idea is similar to search step.
                if len != 0:
                    len = lps[len-1]
                    # Also, note that we do not increment i here
                
                else:
                    lps[i] = 0
                    i += 1