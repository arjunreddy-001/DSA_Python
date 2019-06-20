# try out Python queue functions
from collections import deque

# create an empty deque object that will function as a queue
queue = deque()

# add(enqueue) some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the queue contents
print(queue)

# pop(deque) an item off the front of the queue
x = queue.popleft()
print("Popped element is " + x.__str__())
print("Queue elements " + queue.__str__())