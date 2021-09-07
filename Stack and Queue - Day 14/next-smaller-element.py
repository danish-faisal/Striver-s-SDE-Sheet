# https://www.geeksforgeeks.org/next-smaller-element/

# TC: O(N), SC: O(1)
def find_next_smaller_elements(xs):
    # Initialize output array to all -1s.
    ys=[-1 for x in xs]
    # Create an empty stack, of indexes of items we have visited in the input-array
    stack=[]
    # Iterate over each element in the input array
    for i,x in enumerate(xs):
        # Check if stack has elements & the element at curr-index < element at prev-index (top-of-stack) 
        while len(stack)>0 and x<xs[stack[-1]]:
            # if yes, the curr-ele is the NSE for the prev-ele
            ys[stack.pop()]=x
            # pop the prev-index off the stack, next even earlier indexes are checked as they'll be at the top of the stack
            # Keep popping from the stack while the popped element is greater than curr-ele
            # curr-ele becomes the NSE for all such popped elements 
        # append the curr-index to the stack as checked
        stack.append(i)
    return ys


'''
Brute Force Approach: TC:O(N^2), SC: O(1)
Use two loops:
The outer loop picks all the elements one by one.
The inner loop looks for the first smaller element for the element picked by outer loop.
If a smaller element is found then that element is printed as next, otherwise, -1 is printed.
'''