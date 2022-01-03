# https://www.geeksforgeeks.org/find-significant-set-bit-number/

# TC: O(1)
def findMSB(n):
    # Write your code here.
    if n==0:
        return 0
    # To find the position of the most significant set bit
    k=int(math.log(n,2))
    
    # To return the value of the number with set bit at k-th position
    return 1<<k

# Brute Force
def setBitNumber(n):
	if (n == 0):
		return 0

	msb = 0

    # keep dividing n/2 until it becomes 1 i.e., only MSB bit remains 
    # and maintain the count of number of times division is done
	while (n != 1):
		n = int(n / 2)
		msb += 1
    # return the MSB in terms of it decimal value
	return 1<<msb