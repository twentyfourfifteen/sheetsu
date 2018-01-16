from sheetsu import SheetsuClient
import json
from update import *

client = SheetsuClient("600798ca543a")

#output = client.search(sheet="Sheet1")
output = [{u'StudentId': u'101001', u'NameFirst': u'Zoe', u'Grade': u'4', u'NameLast': u'Smith'},{u'StudentId': u'101002', u'NameFirst': u'Max', u'Grade': u'2', u'NameLast': u'Smith'},{u'StudentId': u'101003', u'NameFirst': 'Owen', u'Grade': u'6', u'NameLast': u'Smith'}]


class Student(object):
    def __init__(self, output):
        self.Fname = output['NameFirst']
        self.Lname = output['NameLast']
        self.studentId = output['StudentId']

Sname = raw_input("Lookup by last name: ")

studentReturn = filter(lambda person: person['NameLast'].lower() == Sname.lower(), output)

students = {}
i=0
for x in studentReturn:
    students[i] = Student(x)
    i+=1

def table():
    print "Student ID Last Name, First Name"
    for x in students:
        text = students[x].studentId + " " + students[x].Lname + ", " + students[x].Fname
        print text

table()

Action = raw_input("Add or Delete? ")
action(Action, output)

#if __name__ == '__main__':
#  main()
