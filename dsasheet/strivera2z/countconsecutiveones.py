def CountConsecutiveOnes(list):
    cnt = 0
    consecutiveCounter = 0
    for i in list:
        if( i == 1):
            cnt = cnt + 1
        else:
            cnt = 0 
        consecutiveCounter = max(consecutiveCounter, cnt)
    return consecutiveCounter

if __name__== "__main__":
    newArray = CountConsecutiveOnes([1])
    print(f" there are {newArray} ones in the given list")