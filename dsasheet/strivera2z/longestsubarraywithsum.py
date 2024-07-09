# Time complexity: O(N2), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1)
#
#

def longestSubArraywithSum(desiredSum,list):
    l = len(list)
    length = 0
   
    for i in range(l):  # first point
       for j in range(i, l): # start from 
            cursum = 0
            for x in range (i, j+1):
               cursum += list[x]

            if cursum == desiredSum:
                length = max(length , j-i+1)
    return length
           

if __name__== "__main__":
    print(longestSubArraywithSum(10, [2,3,5]))