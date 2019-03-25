class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            lastNode = self.head #duplicate head pointer
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    def insertAfterNode(self, prevNode, data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
    def printList(self):
        curNode=self.head
        while curNode!=None:
            print(curNode.data)
            curNode = curNode.next
    def deleteNode(self, key):
        curNode = self.head
        if curNode != None and curNode.data == key:
            self.head = curNode.next
            curNode = None
            return
        else:
            prev = None
            while curNode != None and curNode.data != key:
                prev = curNode
                curNode = curNode.next
            if curNode == None:
                print("The data is not found in the list")
                return
            else:
                prev.next = curNode.next
                curNode = None
                
print("Task 1")
# creating a linked list
list1 = linkedList()
list1.printList()


# appending to empty list
print("Appending 'dog'")
list1.append("dog")
# printing list
list1.printList()

# appending again
print("\nAppending 'frog'")
list1.append('frog')
list1.printList()

#prepending
print("\nPrepending 'hog'")
list1.prepend("hog")
list1.printList()

# inserting after Node
print("\nInserting 'monkey' after 'dog'")
list1.insertAfterNode(list1.head.next, 'monkey')
list1.printList()

# inserting after Node again
print("\nInserting 'grandma' after 'hog'")
list1.insertAfterNode(list1.head, 'grandma')
list1.printList()

# deleting grandma from linked list
print("\nDeleting 'grandma' from linked list")
list1.deleteNode('grandma')
list1.printList()
