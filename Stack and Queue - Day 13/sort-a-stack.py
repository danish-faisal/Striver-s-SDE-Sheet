# https://www.geeksforgeeks.org/sort-a-stack-using-recursion/
'''
Time Complexity: O(N^2)
In the worst case for every sorted(), sortedInsert() is called for ‘N’ times recursively for putting element to the right place
Auxiliary Space: O(N), Use of stack data structure for storing values
'''
# Approach 2: Using Recursion
def sortedInsert(s,element):
    # Base case: Either stack is empty or newly inserted
    # item is greater than top (greater than all existing), so push at its correct place
    if len(s)==0 or element<s[-1]:
        s.append(element)
    else:
        # Remove the top item and recur with the remaing elements in the stack and curr-temp
        temp=s.pop()
        sortedInsert(s,element)
        # Remove the top item and recur
        s.append(temp)
    
def sorted(s):
    # if stack is not empty
    if len(s)>0:
        # pop the top-ele
        temp=s.pop()
        # sort remaining stack recursively
        sorted(s)
        # Push the top item back in sorted stack
        sortedInsert(s,temp)


# https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/

# Approach 1: Using another temp-stack, TC:O(N^2), SC:O(N)
def sorted(inputs):
    # res-arr
    tmps=[]
    # until all elements in input-arr are checked
    while len(inputs)>0:
        # current top-ele in the input-arr
        tmp=inputs.pop()
        # until tmp-arr has elements, compare tmp with top-ele in tmp-arr
        while len(tmps)>0 and tmps[-1]>tmp:
            # push back elements greater than tmp, from tmp-arr to inp-arr
            inputs.append(tmps[-1])
            # pop those elements from the tmp-arr
            tmps.pop()
        # push tmp element at its correct place
        tmps.append(tmp)
    # tmp-arr will have the sorted list
    return tmps