from sheetsu import SheetsuClient
import json

class Student(object):
    def __init__(self, studentOutput, grades):
        self.Fname = studentOutput['NameFirst']
        self.Lname = studentOutput['NameLast']
        self.studentId = studentOutput['StudentId']
        self.Grades = grades

    def grades(self):
        self.MyGrades = {"Math":0,"English":0,"Kiswahili":0,"Science":0,"SocialStudies":0}
        for x in self.MyGrades:
            self.MyGrades[x] = int(self.Grades[x])
        self.Cumulative = sum(self.MyGrades.values())


    def table(self):
        text = self.studentId + ", " + self.Lname + ", " + self.Fname
        return text
    def tableGrades(self):
        self.grades()
        text = self.studentId + ", " + self.Lname + ", " + self.Fname + "\n----------------\n"
        for x in self.MyGrades:
            text = text + x + ": " + str(self.MyGrades[x]) + "\n"
        text = text + "Cumulative: " + str(self.Cumulative)
        return text
