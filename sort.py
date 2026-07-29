import student
def sorting_Students(students):
    choice=-1
    while choice!=3:
     print("sorting menu!")
     print("1.sort students by roll number")
     print("2.sort students by name(alphabetically)")
     print("3.exit")
     choice=int(input("enter your choice:"))

    # in python we have built in funxtion for sorting 
     if choice==1:
       students.sort(key=lambda records: records['roll_number'])
       student.display_students(students)
       return
     elif choice==2:
        students.sort(key=lambda records: records['name'])
        student.display_students(students)
        return
     else:
       print("invalid input entry!")