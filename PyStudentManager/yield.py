students = []


def read_file():
	try:
		f = open("student.txt","r")
		for student in f.readlines(f):
			student.appdend(student)
		f.close
	except Exception:
		print("Could not save file")


def read_students(f):
	for line in f:
		yield line


read_file()
print(students)
