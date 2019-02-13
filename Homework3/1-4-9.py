def arraySquare(a):
    b=[]
    for line in a:
        newLine=[]
        for item in line:
                newLine.append(item)
        b.append(newLine)
    return b

#test code to make sure it prints as a square, rectangle and ragged

#squArray = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#print('Square', arraySquare(squArray))

#recArray = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
#print('Rectangle', arraySquare(recArray))

#ragArray = [[1,2,3,4,5,6,7,8],[1,2,3,4],[1,2,3,4,5,6,7,8,9],[1,2]]
#print('ragged, ',arraySquare(ragArray))