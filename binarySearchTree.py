#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  binarySearchTree.py
#  
#  Copyright 2016 Sajal Tyagi <sajalprogrammr@sajalprogrammr-HP-Pavilion-g6-Notebook-PC>
#  

class Tree:
	class Node:
		def __init__(self,element):
			self.element = element
			self.left=self.right=None
		
	def createNode(self,element):
		return self.Node(element)
	
	def insert(self,node,element):
		if node == None:
			return self.Node(element)
		elif element < node.element:
			node.left = self.insert(node.left,element)
		else:
			node.right = self.insert(node.right,element)
		return node
	
	def inorder(self,node):
		if node != None:
			self.inorder(node.left)
			print(node.element)
			self.inorder(node.right)
	
	def preorder(self,node):
		if node != None:
			print(node.element)
			self.preorder(node.left)
			self.preorder(node.right)
	
	def postorder(self,node):
		if node != None:
			self.preorder(node.left)
			self.preorder(node.right)
			print(node.element)
	
	def search(self,node,element):
		if node == None:
			return False
		elif node.element > element:
			return self.search(node.left,element)
		elif node.element < element:
			return self.search(node.right,element)
		else:
			return True
			
def main():	
	mytree = Tree()
	root = mytree.createNode(50) 		#root created 
	mytree.insert(root,34)
	mytree.insert(root,74)
	mytree.insert(root,13)
	mytree.insert(root,3)
	mytree.inorder(root)
	print(mytree.search(root,50))

if __name__=="__main__":
	main()
