#
# This program implements the Single Linked List.
#

class SingleLinkNode:
    # Initialization method.
    def __init__(self, data = None, nextLink = None):
        self.data = data
        self.next = nextLink

class SingleLinkedList:
    # Initialization.
    def __init__(self):
        self.head = SingleLinkNode()
    
    # This method adds item at the first position (after head node) of the Linked List. Complexity - O(1)
    def addItemAtFirst(self, item):
        # Create a new node and assign it to the first position of the linked list.
        self.node = SingleLinkNode(item, self.head.next)
        self.head.next = self.node

    # This method returns the length of the linked list. 
    def getLength(self):
        # Set the initial lenght is zero.
        lenght = 0

        # Traverse the linked list to the end item.
        self.linkNode = self.head.next

        while self.linkNode:
            lenght += 1
            self.linkNode = self.linkNode.next
        
        return lenght
    
    # This method traverses the Linked List and print the data of each node.
    def printList(self):
        self.linkNode = self.head.next
        while self.linkNode:
            print(str(self.linkNode.data) + ' --> ', end='')
            self.linkNode = self.linkNode.next
        
        print('\n')
    
    # This method adds item at the end of the linked list. Complexity - O(n)
    def addItemAtEnd(self, item):
        # Traverse the linked list to the end item.
        self.linkNode = self.head.next

        while self.linkNode:
            if self.linkNode.next is None:
                break
            self.linkNode = self.linkNode.next
        
        # Create a new node and assign it to end position of the linked list.
        self.node = SingleLinkNode(item)
        self.linkNode.next = self.node
    
    # This method takes a list of items and adds the list of items at the end of the linked list.
    def addItemList(self, itemList):
        for item in itemList:
            if self.getLength():
                self.addItemAtEnd(item)
            else:
                self.addItemAtFirst(item)
            
    # This method adds item at the index position of the linked List. Commplexity - O(n).
    def addItemAtIndex(self, item, index):
        if index < 0 or index > self.getLength():
            raise IndexError('Error: Please provide the proper index position!')

        if index == 0:
            self.addItemAtFirst(item)
        elif index == self.getLength():
            self.addItemAtEnd(item)
        else:
            self.linkNode = self.head.next

            nodeIdx = 1
            while nodeIdx < index:
                self.linkNode = self.linkNode.next
                nodeIdx += 1

            self.node = SingleLinkNode(item, self.linkNode.next)
            self.linkNode.next = self.node
    
    # This method removes the item at the index position of the linked list
    def removeIndex(self, index):
        if index < 0 or index >= self.getLength():
            raise IndexError('Error: Please provide the proper index position!')

        if index == 0:
            self.removeFirstItem()
        elif index == self.getLength() - 1:
            self.removeLastItem()
        else:
            self.linkNode = self.head.next
            nodeIdx = 1

            while nodeIdx < index:
                self.linkNode = self.linkNode.next
                nodeIdx += 1

            print('Removing.. ', self.linkNode.next.data)
            self.linkNode.next = self.linkNode.next.next

    
    # This method removes the first item of the linked list.
    def removeFirstItem(self):
        self.linkNode = self.head.next
        print('Removing.. ', self.linkNode.data)
        self.head.next = self.linkNode.next

    # This method removes the last item of the linked list.
    def removeLastItem(self):
        self.linkNode = self.head.next

        while True:
            if self.linkNode.next.next is None:
                break
            self.linkNode = self.linkNode.next
        
        print('Removing.. ', self.linkNode.next.data)
        self.linkNode.next = None

    # This method searches the linked list for a given item and returns the index value of the first match of the item in the linked list.
    # Linear Search - Complexity: O(n).
    def indexOfItem(self, item):
        nodeIdx = -1
        self.linkNode = self.head.next
        itemFound = False

        while self.linkNode:
            nodeIdx += 1

            if self.linkNode.data == item:
                itemFound = True
                break

            self.linkNode = self.linkNode.next
        
        if itemFound:
            return nodeIdx
        else:
            return -1

def main():
    linkList = SingleLinkedList()
    
    # Add elements
    # linkList.addItemAtFirst('Blue')
    # linkList.addItemAtFirst('Green')
    
    # # Print the list.
    # linkList.printList()

    # linkList.addItemAtEnd('Orange')
    # linkList.addItemAtEnd('Purple')
    # linkList.addItemAtFirst('Red')

    # # Print the list.
    # linkList.printList()

    # linkList.addItemAtIndex('Magenta', 4)

    linkList.addItemList(['Red', 'Green', 'Blue', 'Orange', 'Magenta', 'Purple', 'Amber', 'Yellow', 'Gray', 'Black'])

    # Print the list.
    linkList.printList()

    # Print the length of the list.
    # print('Length: ', linkList.getLength())

    # Remove Items.
    # linkList.removeIndex(6)
    
    # Print the list.
    # linkList.printList()

    # Search item.
    print('Index: ' , linkList.indexOfItem('Bittu'))

    
if __name__ == '__main__':
    main()


