class Node:

	def __init__(self, item=None):
		self.item = item
		self.next = None


	def __str__(self):
		return str(self.item)