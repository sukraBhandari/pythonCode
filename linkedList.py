class Node(object):
    #Node constructor
    def __init__(self, data):
        self.data = data
        self.next = None
    
    #recursive method to print the each node
    def printData(self):
        print self.data
        if self.next is not None:
            self.next.printData()


class LinkedList(object):
    #LinkedList constructor
    def __init__(self):
        self.head = None

    #add a node to beginning of the LinkedList
    def addToFirst(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            
    #add a node to the end of the LinkedList
    def addToLast(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            #loop through all the nodes until you hit the end node
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
            
    #add a node to the middle(not first and not last) of the linkedlist
    def addAtPosition(self, data, position):
        if self.head is None:
            return False
        else:
            temp = Node(data)
            current = self.head
            count = 0
            
            #loop until you hit the node right before the position
            while count < position-1:
                current = current.next
                count+=1
            
            #important step, do not lose the rest of the nodes.....
            temp.next = current.next
            current.next = temp
            return True

    #remove the first node of the Linkedlist
    def removeFromFirst(self):
        if self.head is None:
            return False
        temp = self.head.next
        self.head = temp

    #remove the very last node
    def removeFromLast(self):
        if self.head is None:
            return False

        #if only one node exits, empty the linkedList
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp is not None:
            if temp.next.next is None:
                temp.next = None
                break
            temp = temp.next

    #remove node from the defined position.
    def removeFromPosition(self, position):
        if self.head is None:
            return False
        temp = self.head
        count = 0
        while count < position - 1:
            temp = temp.next
            count+=1
        temp.next = temp.next.next

    def printData(self):
        if self.head is not None:
            self.head.printData();
