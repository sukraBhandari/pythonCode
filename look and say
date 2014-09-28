#look and say, example
#1
#11
#21
#1211
#111221
#312211
#13112221
#1113213211
#31131211131221
#13211311123113112211


def lookAndSay(n):
  first = n[0]
  rest = n[1:] + ' '
  times = 1
  s = ''
  
  for each in rest:
    if each != first:
      s += str(times)+first
      first = each
      times = 1
    else:
      times +=1
  return s
  
def look():
  num = '1'
  for each in range(10):
    print num
    num = lookAndSay(num)
