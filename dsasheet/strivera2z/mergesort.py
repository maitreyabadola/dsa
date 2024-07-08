# Divide and conquer algo
# it divides the array into 2 equal parts and than merges the 2 sorted parts. 
# there are 2 main functions
# merge() : merges two halves
# mergesort(), divides the array into 2 parts , low to mid, and mid+1 to high
# recursively split the array and go from top-down until all the sub-arrays sizes becomes 1. 

def merge( arr, low , high, mid):
    newArr = []
    left = low
    right = high

    while left <= mid and right <= high:
        if( arr[left] <= arr[right]):
            newArr.append(arr[left])
            left +=1
        else:
            newArr.append(arr[right])
            right +=1

    while (left <=mid):
        newArr.append(arr[left])
        left +=1

    while (right <=high):
        newArr.append(arr[right])
        right +=1

    for i in range(low,high):
        arr[i] = newArr[i-low]
  
