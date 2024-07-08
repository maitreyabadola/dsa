# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

def LeftRotatebyN(n: int , list: [int]) -> [int]:
    # park the elements in the temp array
    temp = []
    for i in range(len(list)- n , len(list) ):
        temp.append(list[i])
    
    # move the elements. 
    for j in range(len(list)-1 -n, -1, -1):
         list[j+n] = list[j]

    for i in range(len(temp)):
            list[i] = temp[i]


    return list

if __name__== "__main__":
    newArray = LeftRotatebyN(3,[ 3,7,8,9,10,11])
    print(newArray)