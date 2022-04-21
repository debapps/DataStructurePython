#
# This program implements the Double Linked List.
#

# Class for Double Linked Node.
class DoubleLinkNode:
    # Initialization Method.
    def __init__(self, data = None, prevLink = None, nextLink = None):
        self.data = data
        self.prev = prevLink
        self.next = nextLink

# Class for Double Linked List.
class DoubleLinkedList:
    # Initialization Method.
    def __init__(self):
        self.head = DoubleLinkNode('HEAD')
        self.tail = DoubleLinkNode('TAIL')
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # This method adds item at the begining of the linked list. Complexity - O(1).
    def addItemHead(self, item):
        self.nodeAdd = DoubleLinkNode(item, prevLink = self.head, nextLink = self.head.next)
        self.head.next.prev = self.nodeAdd
        self.head.next = self.nodeAdd
    
    # This method adds item at the end of the linked list. Complexity - O(1).
    def addItemTail(self, item):
        self.nodeAdd = DoubleLinkNode(item, prevLink = self.tail.prev, nextLink = self.tail)
        self.tail.prev.next = self.nodeAdd
        self.tail.prev = self.nodeAdd

    # This method adds item at the index position of the linked list.
    def addItemIndex(self, item, index):
        if index < 0 or index > self.getLength():
            raise IndexError('Error! Please provide the proper index value.')

        if index == 0:
            self.addItemHead(item)
        elif index == self.getLength():
            self.addItemTail(item)
        else:
            self.itrNode = self.head.next
            nodeIdx = 0
            while nodeIdx < index - 1:
                self.itrNode = self.itrNode.next
                nodeIdx += 1
            
            self.nodeAdd = DoubleLinkNode(item, prevLink = self.itrNode, nextLink = self.itrNode.next)
            self.itrNode.next.prev = self.nodeAdd
            self.itrNode.next = self.nodeAdd
    
    # This method takes a item list and add the items from the list at the end of the linked list.
    def addItemList(self, itemList):
        for item in itemList:
            if self.getLength():
                self.addItemTail(item)
            else:
                self.addItemHead(item)
    
    # This method removes the item from the beginning of the linked list. 
    def removeItemHead(self):
        self.linkNode = self.head.next
        print('Removing .. ', self.linkNode.data)
        self.linkNode.next.prev = self.head
        self.head.next = self.linkNode.next

    # This method removes the item from the end of the linked list. 
    def removeItemTail(self):
        self.linkNode = self.tail.prev
        print('Removing .. ', self.linkNode.data)
        self.tail.prev = self.linkNode.prev
        self.linkNode.prev.next = self.tail

    # This method removes the item at the given index position of the linked list. 
    def removeItemIndex(self, index):
        if index < 0 or index >= self.getLength():
            raise IndexError('Error! Please provide the proper index value.')

        if index == 0:
            self.removeItemHead()
        elif index == self.getLength() - 1:
            self.removeItemTail()
        else:
            self.itrNode = self.head.next
            nodeIdx = 0
            while nodeIdx < index - 1:
                nodeIdx += 1
                self.itrNode = self.itrNode.next

            print('Removing ..', self.itrNode.next.data) 
            self.itrNode.next.next.prev = self.itrNode
            self.itrNode.next = self.itrNode.next.next

    # This Method gets the length of the linked list.
    def getLength(self):
        # Initialize the length is zero.
        length = 0

        self.itrNode = self.head.next

        while self.itrNode.data != self.tail.data:
            length += 1
            self.itrNode = self.itrNode.next
        
        return length
    
    # This method prints the all items in the linked list from the head of the list.
    def printHeadList(self):
        print('List starting from HEAD...')
        self.itrNode = self.head.next

        while self.itrNode.data != self.tail.data:
            print(str(self.itrNode.data) + ' <--> ', end='')
            self.itrNode = self.itrNode.next
        
        print('\n')

    # This method prints the all items in the linked list from the tail of the list.
    def printTailList(self):
        print('List starting from TAIL...')
        self.itrNode = self.tail.prev

        while self.itrNode.data != self.head.data:
            print(str(self.itrNode.data) + ' <--> ', end='')
            self.itrNode = self.itrNode.prev
        
        print('\n')

    # This method retruns the index of a given item in the linked list. if item is not found in the list, them
    # it return -1. Linear Search Algorithm: Complexity - O(n).
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
    dlinkList = DoubleLinkedList()

    # Add Items.
    # dlinkList.addItemHead('Toyota')
    # dlinkList.addItemTail('Nisan')
    # dlinkList.addItemTail('Honda')
    # dlinkList.addItemHead('Mercedes')

    # dlinkList.addItemIndex('Ford', 2)
    
    dlinkList.addItemList(['Mercedes', 'Toyota', 'Ford', 'Nisan', 'Honda', 'Douge', 'BMW', 'GMC', 'Chevrolet', 'Corvette'])

    # Print List.
    dlinkList.printHeadList()
    
    # Remove Item.
    # dlinkList.removeItemHead()
    # dlinkList.removeItemTail()
    dlinkList.removeItemIndex(3)
    
    # Print List.
    dlinkList.printHeadList()
    dlinkList.printTailList()

    dlinkList.addItemIndex('Nissan Altima', 3)

    # Print List.
    dlinkList.printHeadList()
    dlinkList.printTailList()

    # Serach Element.
    print('Index: ', dlinkList.indexOfItem('Nissan Altima'))
    print('Index: ', dlinkList.indexOfItem('Mercedes'))
    print('Index: ', dlinkList.indexOfItem('Corvette'))
    print('Index: ', dlinkList.indexOfItem('Maruti'))

    # Print Length of the list.
    # print('Length: ', dlinkList.getLength())

if __name__ == '__main__':
    main()