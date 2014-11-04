#You are given a grid of numbers. A snake sequence is made up of adjacent numbers such that for each number,
#the number on the right or the number below it is +1 or -1 its value. For example, 
#matrix  = [[1,3,2,6,8],
#          [-9,7,1,-1,2],
#          [1,5,0,1,9]]
# here longest snake sequence is 3,2,1,0,1

matrix = [[1,3,2,6,8],[-9,7,1,-1,2],[1,5,0,1,9]]
def mat():
    #create an empty list, which is largest snake sequence so far
    maxL = []
    
    #loop through each elements of the matrix
    #call snakeSeq function to get largest sequence starting from that element of the matrix
    #compare len of the returned sequence with so far largest sequence.
    #print largest sequence.
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        l = snakeSeq(len(matrix), len(matrix[0]), 0,1,[matrix[0][1]])
        if len(l) > len(maxL):
          maxL = l
    print maxL
    
    
    
def snakeSeq(rows, cols, x, y, l):
    #recursive method
    #rows = number of rows: cols = number of columns: x and y = current indexes of the element
    #l = current so far list
    rightSeq = belowSeq = l
    
    #check if our indexex are within the length of matrix
    if cols > y+1:
        if matrix[x][y] == matrix[x][y+1]+1 or matrix[x][y] == matrix[x][y+1]-1:
            l.append( matrix[x][y+1])
            rightSeq = snakeSeq(rows, cols, x, y+1,l)
    if rows > x + 1:
        if matrix[x][y] == matrix[x+1][y]+1 or matrix[x][y] == matrix[x+1][y]-1:
            l.append( matrix[x+1][y])
            belowSeq = snakeSeq(rows, cols, x+1, y, l)
    if len(rightSeq) >= len(belowSeq):
        return rightSeq
    else:
        return belowSeq
    
