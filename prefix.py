#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prefix.py
#  
#  Copyright 2016 Sajal Tyagi <sajaltyagi@Sajals-MacBook-Air.local>
#  

class Stack:
	def __init__(self):
		 self.stack = []
	
	def pop(self):
		return self.stack.pop()
	
	def isEmpty(self):
		return (self.stack == [])
	
	def peek(self):
		return self.stack[len(self.stack)-1]
	
	def push(self, ele):
		self.stack.append(ele)

def evaluate(exp):
	tokens = list(exp)
	tokens.reverse()
	output = [] 
	#i = 0
	for i in range(len(tokens)):
		if tokens[i] == ' ':
			continue
		if tokens[i] >= 'a' and tokens[i] <= 'z':
			output.append(tokens[i])
		elif tokens[i] == '*' or tokens[i] == '/' or tokens[i] == '+' or tokens[i] == '-':
			while not mystack.isEmpty() and hasPrecedence(tokens[i],mystack.peek()):
				output.append(mystack.pop())
			mystack.push(tokens[i])
		elif tokens[i] == ')':
			mystack.push(tokens[i])
		elif tokens[i] == '(':
			while mystack.peek() != '(':
				output.append(mystack.pop())
			mystack.pop()
		#print(tokens[i])
	
	while not mystack.isEmpty():
		output.append(mystack.pop())
	return output

def hasPrecedence(op1,op2):
	if op2 == '(':
		return False
	elif (op1 == '-' or op1 == '+') and (op2 == '/' or op2 == '*'):
		return True
	else :
		return False


mystack = Stack()
exp = input("\n\n\tWrite ur expression : ")
final = ""
ml = evaluate(exp)
ml.reverse()
print("\n\n\n\t",ml)
