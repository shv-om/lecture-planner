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
	"""
	subjects = input("Enter subject list separated by a space eg: sub1 sub2... :\n").split()
	print("\nEnter Batch Information (Name and No. of Students")
	batches = input_batch_room('Batch Name', 'No. of students')
	print("\nEnter Class Rooms information (Room no. and Capactiy)")
	rooms = input_batch_room('Room No.', 'Capacity')
	"""

	# Temporary data
	subjects = ['Predictive Analytics','NLP','Web Technology','DBMS','OODA','Information Retrieval','Introduction to Python','Machine Learning']
	batches = [['DA', 36], ['GA', 40], ['MI', 35], ['CS', 40]]   #branch name with no. of students
	#room no. + size of room
	rooms = [['ROOM NO.1', 50], ['ROOM NO.2', 30], ['ROOM NO.3', 50], ['ROOM NO.4', 80], ['ROOM NO.5', 50], ['ROOM NO.6', 100], ['ROOM NO.7', 50], ['ROOM NO.8',100], ['ROOM NO.9', 50], ['ROOM NO.10', 100]]


	#pre defined for ease of testing
	time_period = ['9:00-10:00', '10:00-11:00', '11:00-12:00', '12:30-1:30', '1:30-2:30', '2:30-3:30', '3:30-4:30']  #cllg time from 9:00 to 4:30

	return {'subjects': subjects, 'batches': batches, 'rooms': rooms, 'time_period': time_period}


def startplanning(data):
	lecture = LecturePlanner(data['batches'][:3], data['rooms'], data['subjects'][:3], data['time_period'][:5], 2)
	lecture.planner()


while True:
	print(menu)
	m = input()

	if m == 'q':
		print("Exiting...")
		break

	elif int(m) == 1:
		data = inputdata()
		print("Data Recieved")

	elif int(m) == 2:
		print("StartPlanning...")
		startplanning(data)
		print("Time Table created")

	else:
		print("Wrong choice")

