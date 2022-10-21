def printTriangle(size):
    starCount = 0
    for i in range(size):
        for j in range(0, i + 1):
            starCount += 1
        print("*" * len(range(0, i + 1)))
    return(starCount)

def main():
    print('Here is a triangle with height 4:')
    numStars = printTriangle(4)
    print('That triangle had ' + str(numStars) + ' total stars.')
    print("Here is a triangle with height 7:")
    numStars = printTriangle(0)
    print("That triangle had " + str(numStars) + " total stars.")

main()
