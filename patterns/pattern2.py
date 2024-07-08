#print https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

def PrintSequence(rows):
    for r in range(1,rows):
        for c in range(1,r):
            print("* ", end= " ")
        print("")


if __name__ == "__main__":
    PrintSequence(5)
		