# https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/

def maxMeeting(l, n):
    # Sorting of meeting according to their finish time.
    l.sort(key = lambda x: x[1])
    
    # Initialising an arraylist for storing answer
    res=[l[0][2]]
    # time_limit to check whether new meeting can be conducted or not.
    endmax=l[0][1]
    # Check for all meeting whether it can be selected or not
    for i in range(1,len(l)):
        if l[i][0]>endmax:
            res.append(l[i][2])
            endmax=l[i][1]
    # Print final selected meetings
    for i in ans:
        print(i + 1, end = " ")
    print()
        
    
if __name__ == '__main__':
     
    # Starting time
    s = [ 3, 1, 0, 5, 8, 5 ]
 
    # Finish time
    f = [ 4, 2, 6, 7, 9, 9 ]
 
    # Number of meetings.
    n = len(s)
 
    l = []
 
    for i in range(n):
         
        # Creating object of meeting
        # and adding in the list
        l.append([s[i], f[i], i+1])
         
    # Function call
    maxMeeting(l, n)
    
