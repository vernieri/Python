import os
from tela import *
from person import *

class Teacher(Person):
	pass

	def __init__(self, salary, subjects):
		self.salary = salary
		self.subjects = subjects
