import numpy as np
import math

class Percolation:

	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.sites = np.zeros([rows,cols])
		self.connected_sites = np.zeros([rows,cols])
		for i in range(rows*cols):
			self.connected_sites[math.floor(i/cols), i%cols] = i

	def open(self,row,col):
		self.sites[row,col] = 1
		site_index = row*self.cols + col
		# Check if neighbours sites are open. If the are, connected them
		self.check_and_connect(row,col)

	def check_and_connect(self,row,col):
		up_row = row-1
		if(up_row >= 0 and self.site_is_open(up_row, col)):
			print("connect with up")
			self.connect_sites((row,col), (up_row,col))

		down_row = row+1
		if(down_row < self.rows and self.site_is_open(down_row, col)):
			print("connect with down")
			self.connect_sites((row,col), (down_row,col))

		left_col = col-1
		if(left_col >= 0 and self.site_is_open(row, left_col)):
			print("connect with left")
			self.connect_sites((row,col), (row,left_col))

		right_col = col+1
		if(right_col < self.cols and self.site_is_open(row, right_col)):
			print("connect with right")
			self.connect_sites((row,col), (row,right_col))


	def site_is_open(self, row, col):
		return self.sites[row, col]


	# find root of site
	def get_root_site(self,row,col):
		if(self.connected_sites[row, col] == row*self.cols + col):
			return (row,col)
		else:
			target_index = self.connected_sites[row, col]
			print(int(target_index%self.cols))
			return self.get_root_site(math.floor(target_index/self.cols), int(target_index%self.cols))

	# connect 2 sites (tuples of rows and cols)
	def connect_sites(self,site1,site2):
		root1 = self.get_root_site(site1[0], site1[1])
		root2 = self.get_root_site(site2[0], site2[1])
		print("Connecting site at position: (" + str(site1[0]) 
			+ ", " + str(site1[1]) + 
			") with site at position: (" + 
			str(site2[0]) + ", " + str(site2[1]) + ")")
		self.connected_sites[root2[0], root2[1]] = self.connected_sites[root1[0], root1[1]]

	def sites_are_connecetd(self,site1,site2):
		root1 = self.get_root_site(site1[0], site1[1])
		root2 = self.get_root_site(site2[0], site2[1])
		return root1 == root2

	def percolates(self):
		for i in range(self.cols):
			if(self.site_is_open(self.rows-1, i)):
				for j in range(self.cols):
					if(self.sites_are_connecetd((self.rows-1, i), (0, j))):
						return True
		return False

perc = Percolation(5,5)
perc.open(1,1)
perc.open(1,2)
print(perc.connected_sites)
print(perc.get_root_site(1,2))
# print(perc.sites_are_connecetd((1,1), (1,2)))
perc.open(3,2)
perc.open(4,2)
print(perc.sites_are_connecetd((4,2), (3,2)))
print(perc.connected_sites)
perc.open(2,2)
print(perc.connected_sites)
print(perc.sites_are_connecetd((4,2), (1,1)))
perc.open(0,3)
perc.open(0,1)
print(perc.percolates())




