def add_marks(students):
    r_no=int(input("enter roll number:"))
    for records in students:
        if r_no==records['roll_number']:
            print("Roll number found now add marks!")
            sub_1=int(input(" DATA BASE:"))
            records['sub_1']=sub_1
            sub_2=int(input(" COMPUTER ORGANIZATION AND ASSEMBLY LANGUAGE:"))
            records['sub_2']=sub_2
            sub_3=int(input(" THEORY OF AUTOMATA:"))
            records['sub_3']=sub_3
            sub_4=int(input(" SOFTWARE ENGINERING:"))
            records['sub_4']=sub_4
            print("records added successfully!")
            return
    print("roll number not found!")