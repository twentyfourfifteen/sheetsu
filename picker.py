from sheetsu import SheetsuClient
import json
from student import *
from actions import *

clientStudent = SheetsuClient("fa9ce8496310")
clientGrades = SheetsuClient("8efe1f243cb1")

debug = False

if debug:
    DataLocation = "local"

def dataLocate():
    dl = raw_input("Local or Remote: ")
    dl = dl[0].lower()
    if dl == "r":
        return "remote"
    else: return dl

try:
    DataLocation
except NameError:
    DataLocation = dataLocate()

def getData(location,fileName,client):
    fileName = fileName + '.json'
    if location == "remote":
        data = client.search(sheet="Sheet1")
        with open(fileName, 'w') as outfile:
            json.dump(data, outfile)
        return data
    else:
        with open(fileName, 'r') as outfile:
            data = json.load(outfile)
        return data

studentOutput = getData(DataLocation,"studentStore",clientStudent)
gradeOutput = getData(DataLocation,"gradeStore",clientGrades)

grades = gradeOutput
students = {}
i=0
for x in studentOutput:
    sid = str(x['StudentId'])
    gradePass = filter(lambda r: r['StudentId']==sid,grades)
    students[i] = Student(x,gradePass[0])
    i+=1

def action(Action, studentOutput):
    Action = Action.lower()
    if Action == "list":
        listEm(students)
    elif Action == "lookup":
        lookup(students,)
    elif Action == "add":
        Update(studentOutput, "add")
    elif Action == "delete":
        Update(studentOutput, "delete")
    else:
        print "I haven't learned how to do that yet."

Action = raw_input("What would you like to do:\nList, Lookup, Add or Delete? ")
action(Action, studentOutput)


#if __name__ == '__main__':
#  main()
