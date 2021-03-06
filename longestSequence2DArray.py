#please check out my snakesequence2 for similar but more robust solution....
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
         
         
#our graph G is dictionary
G = {}



def make_link(G, node1, node2):
  #this function gives the distance(which is 1 in our case) between two connected nodes(or neighbors)
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G
    
    

def find_neighbors(m, i, j):
  #this method will find and returns all the neighbor indexes to an element located at i,j indexes
  rowLength = len(matrix)
  colLength = len(matrix[0])

  #this is very important, finding left,right,top and bottom index without giving out of bound error
  left_neighbor = max(0, i-1)
  right_neighbor = i+2 if i < rowLength-1 else i+1
  top_neighbor = max(0, j-1)
  bottom_neighbor = j+2 if j < colLength-1 else j+1

  #return all valid neighbors
  return [((row,col),(i,j)) for row in range(left_neighbor,right_neighbor) for col in range(top_neighbor,bottom_neighbor) if not(row == i and col == j) ]

 
  
def makeList():
  l = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0]):
      l += find_neighbors(matrix, i, j)
  
  for (x,y) in l:
    make_link(G, x, y)
   
   
def find_sequence(G, node):
  neighbor_to_visit = [node]
  path = [node]
  while neighbor_to_visit:
    current_node = neighbor_to_visit.pop()
    current_node_value = matrix[current_node[0]][current_node[1]]
    for each in G[current_node]:
      if matrix[each[0]][each[1]] - current_node_value == 1 and each not in path:
        neighbor_to_visit.append(each)
        path.append(each)
  return path
  
def check_graph():
  makeList()
  longest = []
  for node in G.keys():
    newSequence = find_sequence(G, node)
    if len(newSequence) > len(longest):
        longest = newSequence
  print set([matrix[x[0]][x[1]] for x in longest])

  
