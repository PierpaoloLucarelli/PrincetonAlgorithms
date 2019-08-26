from node import Node

class Queue:

	def __init__(self):
		self.head = None
		self.tail = None


	def enqueue(self, item):
		node = Node(item)
		if(self.is_empty()):
			self.tail = node
			self.head = self.tail
		else:
			self.tail.next = node
			self.tail = node

	def dequeue(self):
		if(self.is_empty()):
			self.tail = None
		else:
			item = self.head.item
			self.head = self.head.next
			return item

	def __str__(self):
		if(self.is_empty()):
			return "Empty"
		else:
			node = self.head
			output = ""
			while(True):
				output += node.item
				if node.next == None:
					break
				output += ", "
				node = node.next
			return output



	def is_empty(self):
		return self.head == None


q = Queue()
q.enqueue("hi")
q.enqueue("my")
q.enqueue("name")
q.enqueue("is")
q.enqueue("jeff")
print("After queing")
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue("jeff")
print(q.dequeue())