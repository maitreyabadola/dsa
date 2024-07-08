#print https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

def PrintSequence(rows):
    for r in range(1,rows+1):
        for c in range(0,r):
            print(r, end= " ")
        print("")


if __name__ == "__main__":
    PrintSequence(10)
		