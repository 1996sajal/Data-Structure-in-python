#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  postfix.py
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


def hasPrecedence(op1, op2):
	if op2 == ')' or op2 == '(':
		return False
	elif (op1 == '*' or op1 == '/') and (op2 == '-' or op2 == '*'):
		return False
	else:
		return True

def evaluate(exp):
	output = ""
	tokens = list(exp)

	for i in range(len(tokens)):
		if tokens[i] == ' ':
			continue
		if tokens[i] >= 'a' and tokens[i] <= 'z':
			while i < len(tokens) and tokens[i] >= 'a' and tokens[i] <= 'z':
				output = output + tokens[i]
				i += 1
		elif tokens[i] == '*' or tokens[i] == '/' or tokens[i] == '-' or tokens[i] == '+':
			while (not mystack.isEmpty() and hasPrecedence(tokens[i], mystack.peek())):
				print(tokens[i])
				output = output + mystack.pop()
			mystack.push(tokens[i])
		elif tokens[i] == '(':
			mystack.push(tokens[i])
		elif tokens[i] == ')':
			while mystack.peek() != '('	:
				output = output + mystack.pop()
			mystack.pop()
	while not mystack.isEmpty():
		if mystack.peek() == '(':
			mystack.pop()
		else :
			output = output + mystack.pop()
	return output

mystack = Stack()
exp = input("\n\nWrite input expression : ")

print("\n\nOutput :",evaluate(exp))
