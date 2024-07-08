def MoveZerostoEnd(n: int , list: [int]) -> [int]:
    j = -1

    # Place the pointer j
    for i in range(n):
        if list[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return list
    
    # move the pointers i and j and swap accordingly
    for i in range(j +1, n):
        if list[i] != 0:
            list[i], list[j] = list[j] , list[i]
            j +=1

    return list

if __name__== "__main__":
    newArray = MoveZerostoEnd(8,[ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1])
    print(newArray)