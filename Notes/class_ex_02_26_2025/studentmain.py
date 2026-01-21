from StudentV2 import Student
# s1 = Student("Tony", 2000)
# s2 = Student("Bala", 1999)

# print(s1.school_name, s2.school_name)

#for the first one, we manually set up the ID, the 2nd one is auto generated

# Student.update_school_name("Texas A&M")
# print(s1.school_name, s2.school_name)
# print(Student.school_name)
# print(Student.student_cnt)
#
# s1.id = 8000000000
# print(s1.id)
#
# print(Student.get_age(s1.yob))

# A better way to do it is to use the class name
# print(Student.school_name)
# print(Student.student_cnt)

students = [
    Student("alice", 3,  "123-222-2222"),
    Student("bob", 3.5, "830-213-2122"),
    Student("charlie", 3, "210-122-3412"),

]

#Prints the first index within the students list
# print(students[0])

def search_students_by_phone(students, target_phone):
    found_student = None
    for student in students:
        if student.get_phone() == target_phone:
            found_student = [student.name, student.get_phone()]
            break
    return found_student
    #Not the best way to implement, but its straight forward
target = "830-213-2122"
find_student = search_students_by_phone(students, target)

if find_student:
    print(find_student)
else:
    print("Student is not found, HE'S LOST TO THE DIMENSION")

#Find students whose GPA is greater than 3.25
def filter_students_by_gpa(students, target_gpa):
    for student in students:
        if student.get_gpa() >= target_gpa:
            filtered_students.append([student.name, student.get_gpa(),
                                      student.get_phone()])

        return filtered_students

filtered_students = filter_students_by_gpa(students, 4.0 )

if len(filtered_students)>0:
    for s in filtered_students:
        print(s)
else:
    "FUCK YOU"