# Time complexity: O(N2), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1)
#
#

def bubblesort(len, list):
    for i in range(len, 0, -1 ):
        for j in range(0, i-1):
            if (list[j] < list[j + 1]):
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp    

    return list

if __name__== "__main__":
    sortedlist = bubblesort( 5, [7,5,9,2,8])
    print(sortedlist)