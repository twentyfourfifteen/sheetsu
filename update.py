def action(Action, output):
    Action = Action.lower()
    if Action == "add":
        Update(output, "add")
    elif Action == "delete":
        Update(output, "delete")
    else:
        print "I haven't learned how to do that yet."

class Update(object):
    def __init__(self, output, action):
        self.studentIds = []
        for x in output:
            self.studentIds.append(x['StudentId'])
        print self.studentIds
        self.keys = []
        for x in output[0]:
            self.keys.append(x)
        print self.keys
        self.action = action
        def add(self):
            newStudent = {}
            newFName = raw_input("New First Name? ")
            newLName = raw_input("New Last Name? ")
            newId = int(max(self.studentIds)) + 1
    #    self.Fname = output['NameFirst']
    #    self.Lname = output['NameLast']
    #    self.studentId = output['StudentId']
            print "We will add: %s %s with the ID: %s when the Admin gets back" % (newFName, newLName, newId)
    #    client.create_one(name=response, score=0)
        def update(self):
            newStudent = {}
            updateId = raw_input("Which student by ID? ")
            newFName = raw_input("New First Name? ")
            newLName = raw_input("New Last Name? ")
            print "We will update: %s %s with the ID: %s when the Admin gets back" % (newFName, newLName, updateId)

        if action == "add":
            add(self)
        elif action == "update"
            update(self)


    #def delete(self):
    #response = raw_input("Delete who? ")
    #print "We will delete %s when the Admin gets back" % (response)
