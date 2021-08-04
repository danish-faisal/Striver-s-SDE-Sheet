# https://leetcode.com/problems/permutation-sequence/

# Brute Force Approach -> Generate all permutations, have them stored in a data structure, sort the data structure and return (k-1)th element

# Optimal Approach
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        numbers=[]  # to store all 0-n numbers, will be used to generate the req.permutation
        # calculate (n-1)th factorial
        for i in range(1,n):
            fact=fact*i
            numbers.append(i)
        numbers.append(n)
        # resuktant string
        ans=""
        # as we'll have 0 based index permutations
        k=k-1

        while True:
            # for n we'll have n! permutations -> each digit having (n-1) combinations
            # First position of the kth sequence will be occupied by the number present at index = k / (n-1)! -> so get that number at number[k/fact]
            ans+=str(numbers[k//fact])
            # pop off that number from the numbers list to reduce the size(n) -> as the next in sequence will be made of another numbers
            numbers.pop(k//fact)
            # base codn
            if len(numbers)==0:
                break
            # update k -> as next first digit in the sequence will be again at k/(n-1)! index
            k=k%fact
            # update factorial with the new size(n)
            fact=fact//len(numbers)
        
        return ans