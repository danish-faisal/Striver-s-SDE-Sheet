# https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/
# https://www.codingninjas.com/codestudio/problem-details/calculate-square-of-a-number_1112623

# Approach 3: TC: O(log n)
'''
If n is even, it can be written as
  n = 2*x 
  n^2 = (2*x)^2 = 4*(x^2)
If n is odd, it can be written as 
  n = 2*x + 1
  n^2 = (2*x + 1)^2 = 4*(x^2) + 4*x + 1
'''
def square(n):
    if n==0:
        return 0
    if n<0:
        n=abs(n)
    x=n>>1

    # check if 'n' is odd -> as LSB will be 1 only for Odds, n&1 will be 1 only for Odds
    if n&1:
        return (square(x)<<2) + (x<<2) +1
    else:
        return (square(x)<<2)    # (x<<2) => x*4


# Approach 2: The idea is to basically write a perfect square in terms of a series
#  and it turns out to be the sum of the first ‘N’ odd numbers.                     ; TC: O(log n)
def square(n):
    if n==0:
        return 0
    if n<0:
        n=abs(n)
    
    # start of odd-no.
    o=1
    res=0
    for i in range(n):
        res+=o
        # incr 'o' by 2 each time to get the next odd-no
        o+=2
    
    return res

# Approach 1: Add the number 'n', n times to get its square; TC: O(n)
def square(n):
    if n==0:
        return 0
    if n<0:
        n=abs(n)
    
    res=n
    for i in range(n):
        res+=n
    
    return res