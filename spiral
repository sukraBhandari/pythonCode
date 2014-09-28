##/**If an N X N matrix is given, print it in spiral order.
##Example: Below is 5 X 5 matrix
##
##i l o v e
##u a g e p
##g a x s y
##n t n y t
##a l n o h
##**/

# output ilovepythonlanguagesyntax

def sprial():
  matrix =  [["i","l","o","v","e"],
             ["u","a","g","e","p"],
             ["g","a","x","s","y"],
             ["n","t","n","y","t"],
             ["a","l","n","o","h"]]
             
  length = l = len(matrix)
  count = 0
  string = ''
  while count < length//2:
    x = y = count
    xchange = 1
    ychange = 0
    neg = -1
    for i in range(4*(l-1)):
      string+=matrix[x][y]
      if i%(l-1) == 0:
        tempchange = xchange
        xchange = ychange
        ychange = tempchange
      if i%(2*(l-1)) == 0:
        neg = -1*neg
      x = x + xchange*neg
      y = y + ychange*neg
    count+=1
    l -= 2
  if length>1 and length%2 != 0:
    string+=matrix[count][count]
  print string
