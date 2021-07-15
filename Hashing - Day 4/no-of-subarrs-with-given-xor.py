# https://www.geeksforgeeks.org/count-number-subarrays-given-xor/

def subarrayXor(arr,givenXor):
    n=len(arr)
    xor=0
    count=0
    freq={}

    for i in range(n):
        # compute prefix xor
        xor=xor^arr[i]
        """If givenXor^xor of Arr[i] XOR exists in map, then there is another previous prefix with 
        same XOR, i.e., there is a subarray ending at i with XOR equal to m. We add count of
        all such subarrays to result."""
        if xor^givenXor in freq:
            count+=freq[xor^givenXor]
        # If xor of Arr[i] is equal to m, increment ans by 1
        if xor==givenXor:
            count+=1
        # Increment count of elements having XOR-sum, freq[xor] in map by 1
        if xor in freq:
            freq[xor]+=1
        else:
            freq[xor]=1
    
    return count

# Driver Code
arr = [4, 2, 2, 6, 4]
m = 6
 
print("Number of subarrays having given XOR is",
                        subarrayXor(arr, m))