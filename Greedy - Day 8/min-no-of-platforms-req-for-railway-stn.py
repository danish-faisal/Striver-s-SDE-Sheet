# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

def findPlatform(arr, dep, n):
    # Sort arrival and departure arrays
    arr.sort()
    dep.sort()
    # plat -> indicates number of platforms needed at a time
    res=plat=1
    i=1
    j=0

    # iterate over sorted arrival and departure arrays parallelly
    while i<n and j<n:
        # if arrival time of a train < departure time of a train -> we will be needing another platform
        if arr[i]<=dep[j]:
            plat+=1
            i+=1
        # else decrment count of platforms needed
        elif arr[i]>dep[j]:
            plat-=1
            j+=1
        
        # res -> will finally have the maximum no. of platforms need at any moment
        if plat>res:
            res=plat
    
    return res

# Driver code
 
 
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
 
print("Minimum Number of Platforms Required = ",
      findPlatform(arr, dep, n))