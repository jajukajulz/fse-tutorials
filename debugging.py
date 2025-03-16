# usage: python debugging.py

# example dict
student_name = "first name"
student_surname = "last name"
import pdb; pdb.set_trace()
student_age = 33
student_record = {"student_name": student_name, "student_surname": student_surname, "student_age": student_age}
print(student_record) #prints the whole dictionary

