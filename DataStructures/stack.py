# try out Python stack functions

# create a new empty stack
stack = []

# push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents
print(stack)

# pop an element off the stack
x = stack.pop()
print("Popped element is " + x.__str__())
print("Stack elements " + stack.__str__())
