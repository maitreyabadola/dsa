# Time complexity: O(N2), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1)
#
#

def secHighestandsecondlowest(list):
   smallest = secsmallest = highest = secondhighest = list[0]

   for i in list:
       if( smallest >= i):
           secsmallest = smallest
           smallest = i 

       if( highest <= i):
           secondhighest = highest
           highest = i

       if( secondhighest <= i):
           secondhighest = i
   
   print ( f"smallest {smallest} , sec smallest {secsmallest} ,  highest {highest} , second highest {secondhighest}")


if __name__== "__main__":
    secHighestandsecondlowest([1,2,8,3,1])