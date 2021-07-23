# https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

def findMin(V):
    coins = [1,2,5,10,20,50,100,500,1000]
    n=len(coins)

    res=[]
    for i in range(n-1,-1,-1):
        while V>=coins[i]:
            V-=coins[i]
            res.append(coins[i])
    
    print(res)

# Driver Code
if __name__ == '__main__':
    n = 93
    print("Following is minimal number",
          "of change for", n, ": ", end = "")
    findMin(n)