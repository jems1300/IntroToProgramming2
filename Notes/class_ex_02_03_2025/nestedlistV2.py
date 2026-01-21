gradeSheet = [["John Smith", 78, 89, 92, 74, 96],
              ["David Green", 69, 82, 81, 77, 74],
              ["Joanna Lee", 87, 82, 89, 91, 85]]


name = "John"

# def find_student(name, gradeSheet):
#     found = False
#     for i in range(len(gradeSheet)):
#         if name in gradeSheet[i][0]:
#             found = True
#             break
#     if found:
#         index = i
#     else:
#         index = -1
#     return index
# name = "John"
# idx = find_student(name, gradeSheet)
#
# if idx>=0:
#     print(gradeSheet[idx])
# else:

for i in range(len(gradeSheet)):
    st = gradeSheet[i]
    grade = st[1:len(st)]
    print(st[0], sum(grade) / len(grade))