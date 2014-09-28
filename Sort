#different sort methods
#bubble sort
def bubbleSort():
    l = [99,101,37,54,2,93,8,1,17,13,44]
    print(l)
    length = len(l)
    for i in range(0, length-1):
        for j in range(i+1, length):
            if l[j] < l[i]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
    print l 
    
    
    
#selection sort
def selectionSort():
  l = [99,101,37,54,2,93,8,1,17,13,44]
  print(l)
  length = len(l)
  for i in range(length):
    maxIndex = l[0]
    for j in range(1,length-i):
      if l[j] > l[maxIndex]:
        maxIndex = j
    temp = l[maxIndex]
    l[maxIndex] = l[length - i -1]
    l[length -i - 1] = temp
  print l
  
  #insertion Sort
  def insertionSort():
    l = [99,101,37,54,2,93,8,1,17,13,44]
    print(l)
    length = len(l)
    for i in range(length):
      current = l[i]
      pos = i
      while pos > 0 and l[pos - 1] > current:
        l[pos] = l[pos-1]
        pos-=1
      l[pos] = current
    print l
    
#mergeSort
data = [99,101,37,54,2,93,8,1,17,13,44]

******


#quickSort
data = [99,101,37,54,2,93,8,1,17,13,44]
def quickSort(data):
    if not data:
        return []
    pivot = data[0]
    less = [x for x in data if x < pivot]
    more = [x for x in data if x >= pivot]
    return quickSort(less) + [pivot] + quickSort(more)
