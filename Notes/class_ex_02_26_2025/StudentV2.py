class Student:
    def __init__(self, name, gpa=0.0, phone="000-00-0000"):
        self.name = name
        self.__gpa = gpa
        self.__phone = phone #<- private
        #The underscores are private

    def get_phone(self):
        return self.__phone

    def get_gpa(self):
        return self.__gpa

    #Check to see what this does again
    def __str__(self):
        return self.name + " " + self.__phone