#print https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

def PrintSequence(rows):
    i =1 
    
    while i <= rows:
        j =1
        while j <= i:
            print(j, end=" ")
            j = j + 1
        print("")
        i = i + 1


if __name__ == "__main__":
    PrintSequence(10)
		