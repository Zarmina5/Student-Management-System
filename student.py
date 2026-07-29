import file_handler
def add_students(students):
    print("NEW STUDENT RECORD:")
    roll_number=int(input("Roll Number:"))
    name=input("Name:")
    father_name=input("Father Name:")
    cnic=input("CNIC:")
    gender=input("Male/Female:")
    phone_number=int(input("Phone Number:"))
    

    student_record = {
    "roll_number": roll_number,
    "name": name,
    "father_name": father_name,
    "cnic": cnic,
    "gender": gender,
    "phone_number": phone_number 
}
    students.append(student_record)
    file_handler.save_Students(students)
    print(students)
    print("student added successfully!")

def display_students(students):
    if len(students)==0:
        print('no student is added to the list')
    else:
        print(students)

def update_Student(students):
    # when you loop through the list, each iteration gives you one dictionary
    updated_rollnumber=int(input("enter the roll number of student you want to update the record:"))
    for records in students: 
    #  this records is one dict
     if records['roll_number']== updated_rollnumber:
        print("student found:)")
        choose=-1
        while choose!=7:
           
         print("UPDATE MENU:")
         print("1.Change Roll number")
         print("2.Change Name")
         print("3.any changes in father name")
         print("4.changes in CNIC")
         print("5.Any changes in gender if it missprint earlier")
         print("6.change phone number")
         print("7.exit")

         
         choose =int(input("Enter what you want to change:"))
         if choose==1:
          new_roll_number=int(input("enter new roll number"))
          for i in students:
           if new_roll_number==i['roll_number']:
            print("roll number already present!")
            return
          records['roll_number']=new_roll_number
          print("roll_number updates successfully!")


         elif choose==2:
          change_name=input("CHANGE NAME:")
          records['name']=change_name
          print("name updated succesfully")

         elif choose==3:
          f_name=input("any change in father name:")
          records['father_name']=f_name
          print("father name updated successfully")

         elif choose==4:
          new_cnic=input("enter new cnic:")
          for i in students:
            if new_cnic==i['cnic']:
              print("already exist!")
              return 
          records['cnic']=new_cnic
          print("cnic updated successfully")

         elif choose==5:
          gen=input("enter new gender if there is any miss print:")
          records['gender']=gen
          print("updation successful")

         elif choose==6:
          new_num=int(input("enter new number:"))
          for i in students:
           if i['phone_number']==new_num:
             print("already present")
             return
          records['phone_number']=new_num
          print("updation successful")
         elif choose==7:
          break
         else:
          print("invalid input choice")  
        file_handler.save_Students(students)
        return
        print("not found")
   
    
def delete_student(students):
  r_no=int(input("enter roll number:"))
  for records in students:
    if r_no==records['roll_number']:
      students.remove(records)
      print("record deleted successfully")
      file_handler.save_Students(students)
      return
  print("record not found")
   
def search_students(students):
  choice=-1
  while choice!=3:
    print("1.search student by roll number")
    print("2.search student by name")
    print("3.exit")
    choice=int(input("enter your option:"))

    if choice==1:
      found=False
      print("----SEARCHING STUDENT BY ROLL NUMBER----")

      ch=int(input("Enter Roll Number you want to search:"))
      for records in students:
        if ch==records["roll_number"]:
          found=True
          print("-------ROLL NUMBER FOUND------")
          print("*******************************")
          display_students(records) 
          print("                         ")  
      if found==False: 
       print("invalid roll number")
       print("                    ")

    elif choice==2:
       found=False
       print("------SEARCHING STUDENT BY NAME-----")
       print("                                     ")
       name_search=input("Enter Name Of The Student:")
       for i in students:
        if name_search==i["name"]:
           found=True
           print("    STUDENT FOUND!    ")
           print("   student record:     ")
           display_students(i)
           
       if found==False:  
         print("not found")
  return       

       
     
      

