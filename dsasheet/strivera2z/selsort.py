# Time complexity: O(N2), (where N = size of the array), for the best, worst, and average cases.
# Space Complexity: O(1)
#
#

def selsort(len, list):
    for i in range(0, len -1):
        min = i

        for j in range( i+1, len -1):
             if (list[min] < list[j]):
                  min = j

        temp = list[min]
        list[min] = list[i]
        list[i] = temp    

    return list

if __name__== "__main__":
    sortedlist = selsort( 5, [7,5,9,2,8])
    print(sortedlist)