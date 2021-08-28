# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # decalre a stack
        stack=[]
        # build a dictionary/hashmap of matching opening:closing brackets
        dic={'(':')','{':'}','[':']'}
        # for each bracket in string
        for c in s:
            # push it in the stack if ti's an opening bracket
            if c in dic:
                stack.append(c)
            else:    # if it's a closing bracket
                # Check if the curr-closing-bracket matches the top-opening bracket in the stack -> Return False if its not
                # Also Return False if the stack is empty -> as this means a closing bracket before an opening bracket
                if len(stack)==0 or dic[stack.pop()]!=c:
                    return False
        # check if the stack is empty -> Valid-Parentheses if empty
        return len(stack)==0