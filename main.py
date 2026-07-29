import student 
import stats
import sort
import marks
import file_handler
students=file_handler.load_Students()
choice=-1
while choice!=9:
    print("------MENU--------")
    print("1.Add a student record:")
    print("2.Show All Students:")
    print("3.Update students:")
    print("4.Delete a student record:")
    print("5.Add student marks:")
    print("6.Show student marks:")
    print("7.Sort student based on their names")
    print("8.search for a student")
    print("9.Exit!")
    choice=int(input("ENTER YOUR CHOICE:"))
    

    if choice==1:
        student.add_students(students)
    elif choice==2:
        student.display_students(students)
    elif choice==3:
        student.update_Student(students)
    elif choice==4:
        student.delete_student(students)
    elif choice==5:
        marks.add_marks(students)
    elif choice==6:
        stats.show_stats(students)
    elif choice==7:
        sort.sorting_Students(students)
    elif choice==8:
        student.search_students(students)



        

