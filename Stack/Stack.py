#
# This Stack class implement stack in Python using List (resizable).
#
class Stack:
    
    # Initialization of Stack Variables.
    def __init__(self):
        self.stackItemList = []

    # Sting display of the Stack.
    def __str__(self):
        return str(self.stackItemList)
    
    # Push Method: Insert a item at the top of the stack.
    def push(self, item):
        self.stackItemList.append(item)
     
    # isEmpty Method: Check if the stack is empty or not.
    def isEmpty(self):
        if len(self.stackItemList) > 0:
            return False
        else:
            return True

    # Peek Method: Returns the top item without removing it.
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is Empty!')
        else:
            return self.stackItemList[-1]
    
    # Pop Method: Pops (Removes) the top item of the stack and returns it.
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty!')
        else:
            self.popItem = self.stackItemList.pop()
            return self.popItem

def main():
    myStack = Stack()
    
    myStack.push('H')
    myStack.push('E')
    myStack.push('L')
    myStack.push('L')
    myStack.push('O')

    print(str(myStack))
    
    try:
        print(myStack.peek())
        print(myStack.pop(), end='')
        print(myStack.pop(), end='')
        print(myStack.pop(), end='')
        print(myStack.pop(), end='')
        print(myStack.pop(), end='')
        # print(myStack.peek())
        print(myStack.pop(), end='')
    except Exception as e:
        print('\n Exception - ', e)

if __name__ == '__main__':
    main()

    