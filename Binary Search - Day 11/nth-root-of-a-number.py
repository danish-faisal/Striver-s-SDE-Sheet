# https://www.geeksforgeeks.org/n-th-root-number/

# helper-func to multiply the passed no. 'a', 'n' times
def multiply(a,n):
    r=1
    for i in range(1,n+1):
        r*=a
    return r

# Approach: The Solution exists in range [1..m], apply binary search until the range-of-numbers is reduced to 10^-6 
def getNthRoot(n,m):
    # lowest point of range
    low=1
    # highest point of range
    high=m
    # mindiff to obtain to get the solution's range
    mindiff=1e-6

    # until the range [low,high] is not reduced to 10^-6
    while high-low>mindiff:
        # calc-mid
        mid=(low+high)/2
        # check if n times of mid < m
        if multiply(mid,n)<m:
            # cut the left-half of curr-range
            low=mid
        else:
            # cut the right-half of curr-range
            high=mid
    
    print(low," ",high)

    print(m**(1/n))

if __name__ == "__main__":
    # read n -> the no. to get root upto
    n=int(input())
    # read m -> the no. whose root is to be calculated
    m=int(input())
    # call the soln-function
    getNthRoot(n,m)