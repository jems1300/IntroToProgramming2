from datetime import date
class Student:
    # class variable
    school_name = "TAMUSA"
    student_cnt = 0

    def __init__(self, name, yob, id=None):
        self.name = name
        self.yob = yob

        if id is not None:
            self.id = id
        else:
            self.id = 80000000 + Student.student_cnt
            #This automatically generates an id
        Student.increase_student_count()
        #We can't do a cls because it's not part of the parameter of def__init__

    #If I want to include a method to update the school name
    #cls refers to class
    @classmethod #<- this indicates a class method
    def update_school_name(cls, school_name):
        cls.school_name = school_name

    @classmethod
    def increase_student_count(cls):
        cls.student_cnt += 1
    #Every time this is called, we increase the class variable by 1!


    #This is a utility function
    @staticmethod
    def get_age(birth_year):
        return date.today().year - birth_year