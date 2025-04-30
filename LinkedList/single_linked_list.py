class LinkedListNode:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
        
class LinkedList:
    def __init__(self):
        self.headNode=None
        
    def insertAtBeginning(self, data):
        new_node = LinkedListNode(data=data, nextNode=self.headNode)
        self.headNode = new_node
        
    def searchLinkedList(self, value):
        current = self.headNode
        
        while current:
            if current.data == value:
                print(str(current.data))
                return current
                
            else:
                current = current.nextNode
        print(None)    
        return None
        
    def insertIntoLinkedList(self, value, index):
        current = self.headNode
        prevNode = None
        count = 1
        while current:
            if count == index-1:
                prevNode = current
            if count == index:
                newNode = LinkedListNode(data=value, nextNode=current)
                current = newNode
                prevNode.nextNode = current
                return 
            else:
                current = current.nextNode
                count += 1
                
    def printLinkedList(self):
        if self.headNode is None:
            print("Linked List is empty")
            return
        
        currentNode = self.headNode
        llstr = ""
        while currentNode:
            llstr = llstr+str(currentNode.data)+"-->"
            currentNode = currentNode.nextNode
            
        print(llstr+str(currentNode))
            
l1 = LinkedList()
l1.insertAtBeginning(10)
l1.insertAtBeginning(12)
l1.insertAtBeginning(14)
l1.insertAtBeginning(15)
l1.printLinkedList()
l1.insertIntoLinkedList(13, 3)
l1.printLinkedList()
            
