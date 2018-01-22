from sheetsu import SheetsuClient
import json
from actions import *

client = SheetsuClient("fa9ce8496310")

def dataLocate():
    dl = raw_input("Local or Remote: ")
    dl = dl[0]
    dl = dl.lower()
    if dl == "l":
        return "local"
    elif dl == "r":
        return "remote"
    else:
        print "try again"

try:
    DataLocation
except NameError:
    DataLocation = dataLocate()

def getData(location):
    if location == "remote":
        data = client.search(sheet="Sheet1")
        with open('store.json', 'w') as outfile:
            json.dump(data, outfile)
        return data
    else:
        with open('store.json', 'r') as outfile:
            data = json.load(outfile)
        return data

output = getData(DataLocation)

#class Student(object):
#    def __init__(self, output):
#        self.Fname = output['NameFirst']
#        self.Lname = output['NameLast']
#        self.studentId = output['StudentId']

def table(students):
    print "Student ID Last Name, First Name"
    for x in students:
        text = students[x].studentId + " " + students[x].Lname + ", " + students[x].Fname
        print text

def action(Action, output):
    Action = Action.lower()
    if Action == "list":
        listEm(output)
    elif Action == "lookup":
        lookup(output)
    elif Action == "add":
        Update(output, "add")
    elif Action == "delete":
        Update(output, "delete")
    else:
        print "I haven't learned how to do that yet."

Action = raw_input("What would you like to do:\nList, Lookup, Add or Delete? ")
action(Action, output)


#if __name__ == '__main__':
#  main()
