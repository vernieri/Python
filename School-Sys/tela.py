from process import *
import os

def tela():
	print '+------------------------------------+'
	print '1. Add Student                       +'
	print '2. Add Teacher                       +'
	print '3. Add room                          +'
	print '9. Exit                              +'
	print '+------------------------------------+'
	anwser = int(input('Pick one: '))
	anwser = check(anwser)


def main():
	tela()
main()		