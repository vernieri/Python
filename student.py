import os
from tela import *
from person import *


class Student(Person):
	pass

	def __init__(self, period, room, grade, extra):
		self.period = period
		self.room = room
		self.grade = grade
		self.extra = extra

