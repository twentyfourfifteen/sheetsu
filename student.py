from sheetsu import SheetsuClient
import json

class Student(object):
    def __init__(self, studentOutput, grades):
        self.Fname = studentOutput['NameFirst']
        self.Lname = studentOutput['NameLast']
        self.studentId = studentOutput['StudentId']

    def grades(self):
        client = SheetsuClient('8efe1f243cb1')
        grades = client.search(StudentId=self.studentId)
        self.Grades = grades[0]
        self.MyGrades = {"Math":0,"English":0,"Kiswahili":0,"Science":0,"SocialStudies":0}
        for x in self.MyGrades:
            self.MyGrades[x] = int(self.Grades[x])
        #self.English = int(self.Grades['English'])
        #self.Kiswahili = int(self.Grades['Kiswahili'])
        #self.Science = int(self.Grades['Science'])
        #self.SocialStudies = int(self.Grades['SocialStudies'])
        self.Cumulative = sum(self.MyGrades.values())


    def table(self):
        text = self.studentId + " " + self.Lname + ", " + self.Fname
        return text
    def tableGrades(self):
        self.grades()
        text = self.studentId + " " + self.Lname + ", " + self.Fname + "\n"
        text = text + "Math:" +  str(self.MyGrades['Math']) + "\nEnglish:" +  str(self.MyGrades['English']) + "\nCumulative:"  + str(self.Cumulative)
        return text
