# https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1
# https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/

# Optimal Solution: TC: O(N), SC: O(N)
'''
Step 1: Find indexes of next smaller and previous smaller for every element.
Next smaller is the nearest smallest element on right side of arr[i].
Similarly, a previous smaller element is the nearest smallest element on the left side of arr[i]. 
If there is no smaller element on the right side, then the next smaller is n.
If there is no smaller on the left side, then the previous smaller is -1.

Step 2: Once we have indexes of next and previous smaller, we know that arr[i] is a minimum of a window of length “right[i] – left[i] – 1”.
Create an auxiliary array ans[n+1] to store the result. Values in ans[] can be filled by iterating through right[] and left[]

Step 3: Some entries in ans[] are 0 and yet to be filled.
Below are few important observations to fill remaining entries 
a) Result for length i, i.e. ans[i] would always be greater or same as result for length i+1, i.e., ans[i+1]. 
b) If ans[i] is not filled it means there is no direct element which is minimum of length i 
and therefore either the element of length ans[i+1], or ans[i+2], and so on is same as ans[i] 
'''
def printMaxOfMin(arr, n):
     
    s = [] # Used to find previous and next smaller
 
    # Arrays to store previous and next smaller. Initialize elements of left[] and right[]
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
 
    # Fill elements of left[] using logic discussed on
    # https:#www.geeksforgeeks.org/next-greater-element
    for i in range(n):
        while (len(s) != 0 and
               arr[s[-1]] >= arr[i]):
            s.pop()
 
        if (len(s) != 0):
            left[i] = s[-1]
 
        s.append(i)
 
    # Empty the stack as stack is going to be used for right[]
    while (len(s) != 0):
        s.pop()
 
    # Fill elements of right[] using same logic
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()
 
        if(len(s) != 0):
            right[i] = s[-1]
 
        s.append(i)
 
    # Create and initialize answer array
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = 0
 
    # Fill answer array by comparing minimums of all. Lengths computed using left[] and right[]
    for i in range(n):
        # Length of the interval
        Len = right[i] - left[i] - 1
 
        # arr[i] is a possible answer for this
        # Length 'Len' interval, check if arr[i] is more than max for 'Len'
        ans[Len] = max(ans[Len], arr[i])
 
    # Some entries in ans[] may not be filled yet.
    # Fill them by taking values from right side of ans[]
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
 
    # Print the result
    for i in range(1, n + 1):
        print(ans[i], end = " ")
 
# Driver Code
if __name__ == '__main__':
    arr = [10, 20, 30, 50, 10, 70, 30]
    n = len(arr)
    printMaxOfMin(arr, n)

'''
Brute Force Solution: TC: O(N^3), SC: O(1)
A simple brute force approach to solve this problem can be to generate all the windows possible of a particular length say ‘L’ 
and find the minimum element in all such windows. Then find the maximum of all such elements and store it.
'''
# A naive method to find maximum of minimum of all windows of different sizes
INT_MIN = -2147483648
def printMaxOfMin(arr, n):
    # Consider all windows of different sizes starting from size 1
    for k in range(1, n + 1):
         
        # Initialize max of min for current window size k
        maxOfMin = INT_MIN
 
        # Traverse through all windows of current size k
        for i in range(n - k + 1):
             
            # Find minimum of current window
            min = arr[i]
            for j in range(k):
                if (arr[i + j] < min):
                    min = arr[i + j]
 
            # Update maxOfMin if required
            if (min > maxOfMin):
                maxOfMin = min
                 
        # Print max of min for current window size
        print(maxOfMin, end = " ")
 
# Driver Code
arr = [10, 20, 30, 50, 10, 70, 30]
n = len(arr)
printMaxOfMin(arr, n)