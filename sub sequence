#check if any subsequence add upto the user input
def subSequence(n):
  l = [2,7,6,3,5,8,9]
  for i in range(len(l)-1):
    total = l[i]
    for j in range(i+1, len(l)):
      total += l[j]
      if total == n:
        return i+1, j+1
      if total > n:
        break
  return False
  
#example if user enter 16, then 7+6+3= 16
#so output out be 2,4
  
