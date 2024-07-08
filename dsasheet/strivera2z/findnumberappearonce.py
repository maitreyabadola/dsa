def findnumapponce(arr1: [int] ) :
    # find frequency of each number from 1 to n
    # print where frequency is 0
   # nums = [-1] * len(arr1)
    nums = {}
    
    for i in arr1:
        nums[i] = nums.get(i,0) + 1
    
    for x in  nums:
        if nums[x] == 1:
            return x

if __name__== "__main__":
    print(findnumapponce([4,1,2,1,2]))
