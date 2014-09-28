# find a saddle in a 2d Array
# saddle point is nothing but a cell values which has greater value among
# all the cell values in that row as well as it should be the smallest
# value among the column in which it is found......???
def saddle():
    matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    row_max = []
    col_min = []
    for i in range(0,len(matrix)):
        maxi = matrix[i][0]
        mini = matrix[0][i]
        for j in range(0,len(matrix[0])):
            if matrix[i][j] > maxi:
                maxi = matrix[i][j]
            if matrix[j][i] < mini:
                mini = matrix[j][i]

        row_max.append(maxi)
        col_min.append(mini)

    print ([x for x in row_max if x in col_min])
