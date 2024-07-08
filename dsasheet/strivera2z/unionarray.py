def union(arr1: [int],arr2: [int] ) -> [int]:
    retarray = set()
    union = []
    for i in arr1:
        retarray.add(i)
    
    for j in arr2:
        retarray.add(j)

    for num in retarray:
        union.append(num)
    return union


if __name__== "__main__":
    print(union([1,2,3,4,5,6,7,8,9,10],[2,3,4,4,5,11,12]))
