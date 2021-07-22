# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    res=plat=1
    i=1
    j=0

    while i<n and j<n:
        if arr[i]<=dep[j]:
            plat+=1
            i+=1
        elif arr[i]>dep[j]:
            plat-=1
            j+=1
        
        if plat>res:
            res=plat
    
    return res

# Driver code
 
 
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
 
print("Minimum Number of Platforms Required = ",
      findPlatform(arr, dep, n))