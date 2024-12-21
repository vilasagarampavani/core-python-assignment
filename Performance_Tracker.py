def average_marks(marks):
    return  sum (marks)/len(marks)
stu = eval(input("Enter name and marks in the subjects : "))
average_marks_stu = {}
for name, marks in stu.items():
    average_marks_stu[name] = round(average_marks(marks), 2)
top_student = max(average_marks_stu, key=average_marks_stu.get)
print("\nAverage Marks:", average_marks_stu)
print("Top Performer: ",top_student)