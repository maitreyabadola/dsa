# Time complexity: O(N2), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1)
#
#

def IsSorted(list):
    retval = False
    seed = list[0]
    for i in list:
        if(seed > i):
            retval = False
        else:
            retval = True
            seed = i
    return retval

if __name__== "__main__":
    print( IsSorted([3,1]))