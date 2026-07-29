
def show_stats(students):
    r_no=int(input("enter roll number:"))
    for records in students:
        if r_no==records['roll_number']:
            print("student found")
            select=-1
            while select!=2:
             print("STATISTIC MENU!")
             print("1.show complete result")
             print("2.exit")
             select=int(input("ENTER:"))

             if select==1:
                marks_obtained= records['sub_1']+ records['sub_2']+ records['sub_3']+ records['sub_4']
                print( "marks obtained:",marks_obtained)
                average_marks= marks_obtained/4
                print("average marks:",average_marks)
                marks=marks_obtained
                total_marks=400
                percentage=(marks/total_marks)*100
                print("percentage:",percentage)
                print("grades:")
                if percentage>=90:
                    print("grade A")
                elif percentage>=80:
                    print("grade B")
                elif percentage>=70:
                    print("grade C")
                elif percentage >=60:
                    print("grade D")
                else:
                    print("FAIL")              
    print("student not found")
    
                   









