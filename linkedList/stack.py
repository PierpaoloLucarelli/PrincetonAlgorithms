from node import Node

class Stack:

	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def push(self, item):
		new_node = Node(item)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		if(self.head == None):
			return None
		popped = self.head.item
		self.head = self.head.next
		return popped

	def __str__(self):
		output = ""
		node = self.head
		while(not self.is_empty()):
			output += str(node.item)
			node = node.next
			if(node == None):
				break
			output += ", "
		return output


stack = Stack()
stack.push("hi")
print(stack)

p = stack.pop()
print(p)

p = stack.pop()
print(p)

