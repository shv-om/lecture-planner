"""
Initialize Lecture Planner
"""

from os import system, name

try:
	from lectureplanner import LecturePlanner
except ImportError as e:
	print("Error loading Lecture Planner module :(")

menu = """
\t\t***Lecure Planner***
\t1. Input Data
\t2. Start Planning
\tq. Quit (q)
"""

def clear():
	# for windows user
	if name == 'nt':
		system('cls')
	else:
		system('clear')


def input_batch_room(forname, forno):
	list1 = []
	while True:
		name = input(f"Enter the {forname}: ")
		no = int(input(f"Enter the {forno}: "))
		list1.append([name, no])

		if input("Add more (y/n): ") != 'y':
			break

	return list1



def inputdata():
	clear()
	subjects = input("Enter subject list separated by a space eg: sub1 sub2... :\n").split()
	print("\nEnter Batch Information (Name and No. of Students")
	batches = input_batch_room('Batch Name', 'No. of students')
	print("\nEnter Class Rooms information (Room no. and Capactiy)")
	rooms = input_batch_room('Room No.', 'Capacity')

	#pre defined for ease of testing
	time_period = ['9:00 - 10:00', '10:00-11:00', '11:00-12:00', '12:30-1:30', '1:30-2:30', '2:30-3:30', '3:30-4:30']  #cllg time from 9:00 to 4:30

	return {'subjects': subjects, 'batches': batches, 'rooms': rooms, 'time_period': time_period}


def startplanning(data):
	lecture = LecturePlanner(data['batches'], data['rooms'], data['subjects'], data['time_period'], 4)
	lecture.planner()


while True:
	print(menu)
	m = input()

	if m == 'q':
		print("Exiting...")
		break

	elif int(m) == 1:
		data = inputdata()

	elif int(m) == 2:
		print("StartPlanning...")
		startplanning(data)

	else:
		print("Wrong choice")

