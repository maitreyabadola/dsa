# Time complexity: O(N2), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1)
#
#

def Getlargest(list):
    max = list[0]
    for i in list:
        if(max < i):
            max = i
    return max

if __name__== "__main__":
    largest = Getlargest([7,5,9,2,8])
    print(largest)