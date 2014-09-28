#binary search tree

class Node(object):
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    
class Tree(object):
  def __init__(self):
    self.root = Node(data)
    
  def addChild(self,data):
    if self.root is None:
      self.root = Node(data)
    else:
      current = self.root
      lastNode = False
      while not lastNode:
        parent = current
        if data < current.data:
          current = current.left
          if current is None:
            parent.left = Node(data)
            lastNode = True
        else:
          current = current.right
          if current is None:
            parent.right = Node(data)
            lastNode = True
            
  def printInorder(self, node):
    if node is not None:
      self.printInorder(node.left)
      print node.data
      self.printInorder(node.right)
      
  def printPreorder(self, node):
    if node is not None:
      print node.data
      self.printPreorder(node.left)
      self.printPreorder(node.right)
      
  def printPostorder(self, node):
    if node is not None:
      self.printPostorder(node.left)
      self.printPostoder(node.right)
      print node.data
    
  def printBreathFirst(self):
    node = [self.root]
    while node:
      current = node.pop(0)
      print current.data
      if current.left is not None:
        node.append(current.left)
      if current.right is not None:
        node.append(current.right)
        
        
  def treeDepth(self, node, depth=0):
    if node is None:
      return depth
    return max(self.treeDepth(node.left, depth+1), self.treeDepth(node.right, depth+1)
    
  def printLeaf(self, node):
    if node is None:
      return 0
    if node.left is None and node.right is None:
      print node.data
      return 1
    else:
      return self.printLeaf(node.left) + self.printLeaf(node.right)
      
  def findData(self, node, find):
    if node is None:
      return False
    if node.data == find:
      return True
    elif find < node.data:
      return self.findData(node.left, find)
    else:
      return self.findData(node.right, find)
      
  
     
  
