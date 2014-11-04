#reverse the words in a sentence
string = "I love programming using python"

#output must be "python using programming love I"

def reverseSentence():
  s = string.split(' ')
  print ' '.join(s[::-1]
  
  
#alternative
def reverseSentence():
  s = string.split(' ')
    newS = []
    for each in range(len(s), 0, -1):
        newS.append(s[each-1])
    print ' '.join(newS)
    
