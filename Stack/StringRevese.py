from Stack import Stack

string = 'krap lufituaeb a ni kcoltop rof gniog era ew sa yadot dalg era lla ew ,gninrom ynnus a si sihT'
revString = ''

myStack = Stack()

# Push all the characters in the string into the stack.
for char in string:
    myStack.push(char)

# Pop all the characters from the stack until the stack is empty and store it into new string.
while not myStack.isEmpty():
    revString = revString + myStack.pop()

print(revString)

