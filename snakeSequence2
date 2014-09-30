#print snakesequence:
# find longest increasing sub sequence in 2d array.
# you can go any direction
# for example: in matrix
#           [[1,1,2,7,6],
#           [5,4,1,10,5],
#           [6,3,2,3,4]]
# the longest seq is 1,2,3,4,5,6,7


# in this problem, I am using graph method, which I learned in the "Introdcution to Algorithm" taught by Michael Littman
# through Udacity

#our matrix data
matrix = [[1,1,2,7,6],
         [5,4,1,10,5],
         [6,3,2,3,4]]


G={}
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def find_neighbors(m,i,j):
    rowLength = len(m)
    colLength = len(m[0])
    leftRow = max(0,i-1)
    rightRow = i+2 if i < rowLength-1 else i+1
    topCol = max(0, j-1)
    bottomCol = j+2 if j < colLength-1 else j+1
    return [((row,col),(i,j)) for row in range(leftRow,rightRow) for col in range(topCol,bottomCol) if not(row==i and col==j)]

def make_list():
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            l+=find_neighbors(matrix,i,j)
    for (x,y) in l: make_link(G,x,y)

def snake_sequence(G, node):
    path = {}
    to_visit = [node]
    path[node] = [node]
    while to_visit:
        current = to_visit.pop(0)
        value = matrix[current[0]][current[1]]
        for each in G[current]:
            if each not in path and matrix[each[0]][each[1]]-1 == value:
                path[each] = path[current]+[each]
                to_visit.append(each)
    return path[max(path,key=path.get)]

def check_graph():
  make_list()
  longest = [snake_sequence(G,node) for node in G.keys()]
  print [matrix[x[0]][x[1]] for x in max(longest,key=len)]
