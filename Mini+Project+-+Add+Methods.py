import datetime

class MusicSchool:

	students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Cello"]],
                "Eric":   [12, "583-356-223", ["Singing"]]}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	# Add your methods below this line
	def print_students_data(self):
		for key, value in MusicSchool.students.items():
			self.print_student(key)

	def print_student(self, student):
		if student in MusicSchool.students:
			value = MusicSchool.students[student]
			print(f"Student: {student} who is {value[0]} years old and is taking {value[2]}")

	def add_student(self, name, data):
		MusicSchool.students.update({name: data})

	def save_data(self, filename):
		timestamp = datetime.datetime.now()
		update_time = timestamp.strftime("%d-%m-%Y %H:%M:%S")
		f = open(filename, 'a')
		f.write(f"\nUPDATED TIME - {update_time}\n")
		f.write("NAME \t DATA\n")
		for key, value in MusicSchool.students.items():
			f.writelines(f"{key}\t{value}\n")
		f.write("----------------------------------------------------")

# Create the instance

s = MusicSchool(8, 15000)
s.print_students_data()
s.print_student("Gino")
s.add_student("Jack", [60, "562-234-234", ["Piano"]])
s.add_student("Sam", [42, "634-756-354", ["Guitar", "Keyboard"]])

s.print_students_data()
# Saving data if required
# s.save_data("students_data.txt")