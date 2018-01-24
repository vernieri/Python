import os
from room import *
from person import *
from student import *
from teacher import *


path = '/home/vernieri/Documentos/python/school-system/students' #Your Path here
path2 = '/home/vernieri/Documentos/python/school-system/teachers' #Your Path here
path3 = '/home/vernieri/Documentos/python/school-system/room' #Your Path here

def check(anwser):
	if (anwser is not 3):
		makePerson(anwser)
	else:
		CreateRoom()

def CreateRoom():
	rum = Room(
		raw_input('room ID: '),
		raw_input('number: '),
		raw_input('Day: '),
		raw_input('Time to Begin: '),
		raw_input('Time to Leave: '),
		raw_input('Subject: '),
		raw_input('Requested by: ')
		)
	os.chdir(path3)

	file = open(rum.r_id, 'w') 
	lines_of_text = ['Room id: '+rum.r_id+'\n', 'Number: '+rum.number+'\n', 'Day: '+rum.day+'\n', 'ttb: '+rum.ttb+'\n', 'ttl: '+rum.ttl+'\n', 'Subject: '+rum.subject+'\n', 'Request: '+rum.req+'\n']
	file.writelines(lines_of_text)
	file.close	


def makeStudent(_id, pers):
	user = Student(
		raw_input('period: '),
		raw_input('room: '),
		raw_input('grade: '),
		raw_input('extra: '),
		)

	os.chdir(path)

	file = open(_id, 'w') 
	lines_of_text = ['Id: '+_id+'\n', 'Name: '+pers.name+'\n', 'Age: '+pers.age+'\n', 'Occupation: '+pers.occupation+'\n', 'Period: '+user.period+'\n', 'Room: '+user.room+'\n', 'Grade: '+user.grade+'\n', 'Extra-Classe: '+user.extra+'\n']
	file.writelines(lines_of_text)
	file.close

def makeTeacher(_id, pers):
	teach = Teacher(
		raw_input('Salary: '),
		raw_input('Subjects: '),
		)

	os.chdir(path2)
	file = open(_id, 'w') 
	lines_of_text = ['Id: '+_id+'\n', 'Name: '+pers.name+'\n', 'Age: '+pers.age+'\n', 'Occupation: '+pers.occupation+'\n', 'Salario: '+teach.salary+'\n', 'Subjects: '+teach.subjects+'\n']
	file.writelines(lines_of_text)
	file.close

def makePerson(anwser):

	pers = Person(
		raw_input('name: '),
		raw_input('age: '),
		raw_input('ocupation: '),
		) 

	if (anwser == 1):
		first_id = '001'
		second_id = '02' #Teacher = 1, Student = 2
		os.chdir(path)
		list = os.listdir(path)
		number_files = str(len(list))
		_id = first_id+second_id+'0'+number_files
 		makeStudent(_id, pers)

	if (anwser == 2):
		first_id = '001'
		second_id = '01' #Teacher = 1, Student = 2
		os.chdir(path)
		list = os.listdir(path)
		number_files = str(len(list))
		_id = first_id+second_id+'0'+number_files
 		makeTeacher(_id, pers)