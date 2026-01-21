students = {} #<- Empty dictionary
print(students)

# elements in a dictionary is a key/value pairs: "key_name":value
students = {"123-45-6789":"Tom Key",
            "111-11-1111":"Alice Key",
            0:"some one"}

print("before", students)
students["new_id"] = "new student"
print("after", students)

students["111-11-1111"] = "WAZZZUP"
print("after 2x", students)

#del dist_name[key]
del students[0]
print("after deletion", students)

#an alternative way to delete is to use the pop function
print(students.pop("111-11-1111"))

keys = students.keys()
for key in students:
    print(str(key) + ":" + str(students[key]))

#key in dist
print("111-11-1111" in students)

