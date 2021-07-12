# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

# approach 1 -> sort the array      [method 1]
# approach 2 -> hashmap or count array      [mehtod 2 & 6]
# approach 3 -> S = (x-y), S^2 = (x^2-y^2) => (x+y)=(x^2-y^2)/(x-y) => solve (x+y)&(x-y) to get x then y        [method 7]
# x is missing no. & y is the repeating no. => problem of storing high values of summation and square summation

# approach 4 -> using XOR       [method 5]

def getTwoElements(arr, n):
    global x, y
    x = 0
    y = 0
      
    # Will hold xor of all elements 
    # and numbers from 1 to n 
    xor1 = arr[0]
      
    # Get the xor of all array elements
    for i in range(1, n):
        xor1 = xor1 ^ arr[i]
          
    # XOR the previous result with numbers 
    # from 1 to n
    for i in range(1, n + 1):
        xor1 = xor1 ^ i
      
    # Will have only single set bit of xor1
    set_bit_no = xor1 & ~(xor1 - 1)
      
    # Now divide elements into two 
    # sets by comparing a rightmost set 
    # bit of xor1 with the bit at the same 
    # position in each element. Also, 
    # get XORs of two sets. The two 
    # XORs are the output elements. 
    # The following two for loops 
    # serve the purpose
    for i in range(n):
        if (arr[i] & set_bit_no) != 0:
            # arr[i] belongs to first set
            x = x ^ arr[i]
        else:
            # arr[i] belongs to second set
            y = y ^ arr[i]
              
    for i in range(1, n + 1):
        if (i & set_bit_no) != 0: 
            # i belongs to first set
            x = x ^ i
        else:
            # i belongs to second set
            y = y ^ i 
    # x and y hold the desired 
    # output elements 