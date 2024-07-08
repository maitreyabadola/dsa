def findmissing(arr1: [int], num: int ) -> [int]:
    # find frequency of each number from 1 to n
    # print where frequency is 0
    nums = {}
    
    for i in arr1:
        nums[i] = 0
    
    for x in range(1,num):
        if nums.get(x, "empty") == "empty":
                return x

if __name__== "__main__":
    print(findmissing([1,2,4,5],5))
