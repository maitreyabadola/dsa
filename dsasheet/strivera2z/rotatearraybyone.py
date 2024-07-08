def RotateArray(list, position):
    temp = list[len(list) -1]
    
    for i in range(len(list) - 2 , -1, -1 ):
        list[i+1] = list[i]         
    list[0] = temp
    return list

if __name__== "__main__":
    newArray = RotateArray([7,5,9,2,8], 1)
    print(newArray)