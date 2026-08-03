
import json

def load_Students():
    file=open("student.json","r")
    # data=file.read() we will remove this because json read the file it self
    students_load=json.load(file)
    file.close()
    # we will use this "" for checking if the file i empty we cant use length here bcz type bool has no length
    return students_load


def save_Students(students):
   file=open("student.json","w")
   json.dump(students,file,indent=4)
#json.dump(students,file,indent=4) this do 3 jobs at once:1. Takes your Python list
# 2. Converts it into JSON  3. Writes it into the file 
   file.close()
  