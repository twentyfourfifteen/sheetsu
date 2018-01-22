import json

def listEm(students):
    print "\nStudent ID Last Name, First Name"
    for x in students:
        print students[x].table()
    print "\n"

def lookup(students):
    Sname = raw_input("Lookup by last name: ")
    print "\nStudent ID Last Name, First Name"
    studentFilter = filter(lambda x: students[x].Lname.lower()==Sname.lower(), students)
    for x in studentFilter:
        print students[x].tableGrades()
    print "\n"

class Update(object):
    def __init__(self, studentOutput, action):
        self.studentIds = []
        for x in studentOutput:
            self.studentIds.append(x['StudentId'])
        self.keys = []
        for x in studentOutput[0]:
            self.keys.append(x)
        self.action = action
        def add(self):
            newStudent = {u'StudentId': u'', u'NameFirst': u'', u'Grade': u'', u'NameLast': u''}
            newFName = raw_input("New First Name? ")
            newLName = raw_input("New Last Name? ")
            newId = int(max(self.studentIds)) + 1
    #    self.Fname = studentOutput['NameFirst']
    #    self.Lname = studentOutput['NameLast']
    #    self.studentId = studentOutput['StudentId']
            newStudent["StudentId"] = newId
            writeOut(newStudent)
            print "We will add: %s %s with the ID: %s when the Admin gets back" % (newFName, newLName, newId)
    #    client.create_one(name=response, score=0)
        def update(self):
            updateId = raw_input("Which student ID? ")
            newFName = raw_input("New First Name? ")
            newLName = raw_input("New Last Name? ")
            newStudent.StudentId = updateId
            writeOut(newStudent)
            print "We will update: %s %s with the ID: %s when the Admin gets back" % (newFName, newLName, updateId)

        if action == "add":
            add(self)
        elif action == "update":
            update(self)

def writeOut(newStudent):
    print "writing"
    with open('store.json','w') as data:
        data = json.load(data)
        print data[0]
        data[0].update(newStudent)
        print data
        json.dumps(data)

#with open(json_file) as json_data:
#    data = json.load(json_data)
#    data[0]['range'].append(int(number))
#print data

    #def delete(self):
    #response = raw_input("Delete who? ")
    #print "We will delete %s when the Admin gets back" % (response)
