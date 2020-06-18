""" Examples of Stack and Queue in 
	Stack implements Last in First Out (LIFO) i.e. new items are added to last index and items from last index are popped out first and Queue implements First in First out (FIFO) 
	i.e. new items are added to 0th index and items from 0th index
	are popped out first """

class Stack(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peak(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


stack = Stack()
print(stack.isEmpty())

stack.push(1)
stack.push(4)
stack.push(7)

print(stack.peak())
print(stack.size())
print(stack.isEmpty())
print(stack.pop())
print(stack.size())



class Queue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def deqeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

queue = Queue()

print(queue.isEmpty())

queue.enqueue(20)
queue.enqueue(32)
queue.enqueue(5)
print(queue.size())
queue.deqeue()
print(queue.size())
