#this program checks if the parenthesis are valid
#example (()) is valid whereas ())) is invalid

def parenCheck(string):
  l = []
  for each in string:
    if each =="(":
      l.append(each)
    else:
      if len(l)>0:
        l.pop()
      else:
        return False
  if not l:
    return True
  return False
