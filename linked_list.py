""" LinkedList in Python """

#Singly LinkedList
class Node:
	def __init__(self, val):
		self.next = None
		self.val = val

	def __str__(self):
		return str(self.val)

	def add_next(self, node):
		self.next = node

	def get_next (self):
		return self.next.val

#Doubly Linked list
class DoubleLinkedList:

	def __init__(self,val):
		self.next = None
		self.previous = None
		self.val = val


	def __str__(self):
		return str(self.val)

	def add_next(self, node):
		self.next = node

	def add_previous(self,node):
		self.previous = node

	def get_next(self):
		return self.next.val

	def get_prev(self):
		return self.previous.val



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.add_next(b)
b.add_next(c)
c.add_next(d)

print('-'* 30 + " Singly LinkedList "+ '-'* 30)

print(a) #--> 1
print(a.get_next()) #--> 
print(b.get_next())
print(c.get_next())

#-------------------------------------------------
print('-'* 30 + " Doubly LinkedList "+ '-'* 30)
a = DoubleLinkedList(4)
b = DoubleLinkedList(5)
c = DoubleLinkedList(6)
d = DoubleLinkedList(7)

a.add_next(b)
b.add_next(c)
c.add_next(d)

b.add_previous(a)
c.add_previous(b)
d.add_previous(c)

print(a)
print(a.get_next())
print(b.get_prev())
print(b.get_next())
print(c.get_prev())




