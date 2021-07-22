# https://www.geeksforgeeks.org/job-sequencing-problem/

def JobSequencing(arr,n):
    # sort the array in descending order of profit of each job
    arr.sort(key=lambda x: x[2], reverse=True)
    # to store max of all deadlines -> to schedule the jobs within
    maxDeadline = -1
    # itearte over each job, to compare deadlines and get the max
    for i in range(n):
        if arr[i][1]>maxDeadline:
            maxDeadline=arr[i][1]
    # to store max-jobs that can be done and max-profit that can be achieved
    maxJobs = maxProfit = 0
    # to store the sequence of jobs performed and 
    # check if another job can be performed within its deadline
    jobsPerformed=[-1]*(maxDeadline+1) #'+1' as (0-1=-1) in python will refer to last-index of a list, So use 1-(maxDeadLine+1) indexes 
    
    # iterate over sorted arr
    for i in range(n):
        # Find a free slot for this job -> within its deadline
        # (Note that we start from the last possible slot)
        for j in range(arr[i][1],0,-1):
            if jobsPerformed[j]==-1:
                # store the job-id for sequence
                jobsPerformed[j]=arr[i][0]
                maxJobs+=1
                maxProfit+=arr[i][2]
                break
    
    print(jobsPerformed)
    print(maxJobs)
    print(maxProfit)

arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

# Function Call
JobSequencing(arr, 5)
