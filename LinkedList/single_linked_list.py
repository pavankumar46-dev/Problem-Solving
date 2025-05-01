class LinkedListNode:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
        
class LinkedList:
    def __init__(self):
        self.headNode = None
        
    def insertAtBeginning(self, data):
        newNode = LinkedListNode(data=data, nextNode=self.headNode)
        self.headNode = newNode
        
    def insertAtIndex(self, value, index):
        if index == 1:
            self.insertAtBeginning(value)
            
        else:
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
                    break
                    
                current = current.nextNode
                count += 1
            
    def deleteAtIndex(self, index):
        current = self.headNode
        if index == 1: 
            self.headNode = current.nextNode
            
        else:
            count = 1
            prevNode = None
            
            while current:
                if count == index-1:
                    prevNode = current
                    
                if count == index:
                    prevNode.nextNode = current.nextNode
                    current = current.nextNode
                    break
                    
                current = current.nextNode
                count += 1
                
    def searchValueInLinkedList(self, value):
        current = self.headNode
        count = 1
        while current:
            if current.data == value:
                print(f'Value found at index: {count}')
                return
            
            current = current.nextNode
            count += 1
            
        print(f'Value not found')
        return
            
                
                
    def printLinkedList(self):
        current = self.headNode
        llstr = ""
        while current:
            llstr = llstr+str(current.data)+"->"
            current = current.nextNode
            
        print(llstr+"None")
        
ls = LinkedList()
######### Creating linked list ###################
ls.insertAtBeginning(10)
ls.insertAtBeginning(12)
ls.insertAtBeginning(13)
ls.insertAtBeginning(14)
ls.insertAtBeginning(15)
ls.insertAtBeginning(16)
print("Linked List aftr insertion")
ls.printLinkedList()
######### Inserting a new at index ###################
ls.insertAtIndex(11, 3)
print("Linked List after insertion at index 1")
ls.printLinkedList()
######### Deletion of value from linked list ###################
ls.deleteAtIndex(2)
print("Linked List after deletion at index 1")
ls.printLinkedList()
######### Searching for a value in linked list ###################
ls.searchValueInLinkedList(1)

            
        
        
