# https://www.geeksforgeeks.org/print-sums-subsets-given-set/

def subsetSums(arr,l,r,res,ans=0):
    # ptr crossed the valid indexes
    # print current subset's sum
    if l>r:
        res.append(ans)
        return
    
    # Subset including arr[l]
    subsetSums(arr,l+1,r,res,ans+arr[l])

    # Subset excluding arr[l]
    subsetSums(arr,l+1,r,res,ans)

# Driver code
arr = [5, 2, 1]
res=[]
n = len(arr)
subsetSums(arr, 0, n - 1,res)
res.sort()
print(" ".join(str(val) for val in res))