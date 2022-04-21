# Binary Tree: Binary Tree is a tree data structure where each node have at most two child nodes.
# 
# Binary Search Tree: Binary Search Tree (BST) is a binary tree where the each left child node is less than the each
# parent node and each right node is greater than each parent node. BST have following features:
# 
# 1. It is binary tree i.e. each node have at most two child nodes.
# 2. Each left child node is less than the each parent node.
# 3. Each right child node is greater than the each parent node.
# 4. BST contains only unique items.
#
# This program implements the Binary Search Tree (BST) will all the possible methods/operations related to it.
#

# This class implement the Binary Search Tree Node.
class BinarySearchTree:

    # Initialization
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    # This method add child node.
    def addChild(self, childData):
        if self.data == childData:
            return None    
        elif self.data > childData:
            # child will be added to left tree.
            if self.leftNode:
                self.leftNode.addChild(childData)
            else:
                self.node = BinarySearchTree(childData)
                self.leftNode = self.node
        else:
            # child will be added to right tree.
            if self.rightNode:
                self.rightNode.addChild(childData)
            else:
                self.node = BinarySearchTree(childData)
                self.rightNode = self.node

    @staticmethod
    # This method creates a Binary Search Tree from the given list.
    def createTree(itemList):
        root = BinarySearchTree(itemList[0])
        
        for idx in range(1,len(itemList)):
            root.addChild(itemList[idx])
        
        return root       
    
    ## BST Travarsal Method - Depth First Search.

    # In-Order Traversal Method. (Left, Root, Right)
    def inOrderTraversal(self):
        nodeList = []

        if self.leftNode:
            nodeList += self.leftNode.inOrderTraversal()
       
        nodeList.append(self.data)

        if self.rightNode:
            nodeList += self.rightNode.inOrderTraversal()
        
        return nodeList
       
        
    # Pre-Order Traversal Method. (Root, Left, right)
    def preOrderTraversal(self):
        nodeList = []

        nodeList.append(self.data)

        if self.leftNode:
            nodeList += self.leftNode.preOrderTraversal()
       
        if self.rightNode:
            nodeList += self.rightNode.preOrderTraversal()
        
        return nodeList

    # Post-Order Traversal Method. (Left, right, Root)
    def postOrderTraversal(self):
        nodeList = []
        
        if self.leftNode:
            nodeList += self.leftNode.postOrderTraversal()
       
        if self.rightNode:
            nodeList += self.rightNode.postOrderTraversal()
        
        nodeList.append(self.data)

        return nodeList

    ## Other Methods on BST.

    # This method calculates sum of the node value of BST.
    def calculateSum(self):
        nodeList = self.inOrderTraversal()

        if isinstance(self.data, (float, int)):
            sum = 0
            for node in nodeList:
                sum += node

            return sum
        elif isinstance(self.data, str):
            sum = ''

            for node in nodeList:
                sum += node + ' + '

            return sum
        else:
            raise ValueError('Sum Operation is not posible!')

    # This method gets minimum value of the BST.
    def getMinVal(self):
        iterNode = self

        while iterNode.leftNode:
            iterNode = iterNode.leftNode

        return iterNode.data

    # This method gets the maximum value of the BST.
    def getMaxVal(self):
        iterNode = self

        while iterNode.rightNode:
            iterNode = iterNode.rightNode

        return iterNode.data

    # This method removes the node from BST with the node data provided as input.
    def removeTreeNode(self, nodeData):
        if nodeData > self.data:
            # Search in the right tree for delete.
            if self.rightNode:
                self.rightNode = self.rightNode.removeTreeNode(nodeData)
        elif nodeData < self.data:
            # Search in the left tree for delete.
            if self.leftNode:
                self.leftNode = self.leftNode.removeTreeNode(nodeData)
        else:
            # The value is equal.
            # If the matching node is leaf node.
            if self.leftNode is None and self.rightNode is None:
                return None

            # If the matching node has only left sub-tree.
            if self.rightNode is None:
                return self.leftNode

            # If the matching node has only right sub-tree.
            if self.leftNode is None:
                return self.rightNode

            # If the matching node have both left and right sub-trees:
            # 1. Calculate the maximum value of the left sub-tree. 
            # 2. Assign the maximum value to the current node data.
            # 3. Delete the node with maximum value from the left sub-tree.
            if self.leftNode and self.rightNode:
                maxVal = self.leftNode.getMaxVal()
                self.data = maxVal
                self.leftNode = self.leftNode.removeTreeNode(maxVal)
            
        return self

# Testing

def main():
    # List of unsorted elemrnts.
    numList = [6, 14, 5, 21, -9, -16, 87, 12, 8, 127, -5, 65]
    # carList = ['Dodge', 'GMC', 'Honda', 'Alfa Romeo', 'Cadilac', 'BMW', 'Toyota', 'Marcedes']

    print(numList)
    # print(carList)

    # Create a Binary Search Tree (BST) from the number list.
    bstRoot = BinarySearchTree.createTree(numList)
    # bstRoot = BinarySearchTree.createTree(carList)

    # Traverse the tree in different traversal technique.
    # print('Pre-Order Traversal....')
    # print(bstRoot.preOrderTraversal())

    print('In-Order Traversal....')
    print(bstRoot.inOrderTraversal())

    # print('Post-Order Traversal....')
    # print(bstRoot.postOrderTraversal())

    # Calculate Sum of the elements of the tree.
    # print('Sum: ', bstRoot.calculateSum())
    
    # Get the Minimum element from BST.
    # print('Min: ', bstRoot.getMinVal())

    # Get the Maximum element from BST.
    # print('Max: ', bstRoot.getMaxVal())

    # Remove Nodes from BST.
    item = 8
    bstRoot.removeTreeNode(item)
    print('After removing {}.. In-Order traversal.. {}'. format(item, bstRoot.inOrderTraversal()))


if __name__ == '__main__':
    main()
