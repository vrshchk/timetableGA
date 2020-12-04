from university import *
from data import *
import random as rnd

class Evaluation:
    def __init__(self):
        self._data = Data()
        self._classes = []
        self._problems = 0
        self._healthRate = -1
        self._classNumb = 0
        self._ishealthRateChanged = True

    def get_classes(self):
        self._ishealthRateChanged = True
        return self._classes

    def get_healthRate(self):
        if (self._ishealthRateChanged == True):
            self._healthRate = self.calculate_healthRate()
            self._ishealthRateChanged = False
        return self._healthRate


    def initialize(self):
        specs = self._data._specs
        for i in range(0, len(specs)):
            subjects = specs[i]._subjects
            for j in range(0, len(subjects)):
                newClass = Class(self._classNumb, specs[i], subjects[j])
                self._classNumb = self._classNumb + 1
                newClass._lessonTime = Data()._meetingTimes[rnd.randrange(0, len(Data()._meetingTimes))]
                newClass._audience = Data()._rooms[rnd.randrange(0, len(Data()._rooms))]
                newClass._teacher = subjects[j]._teachers[rnd.randrange(0, len(subjects[j]._teachers))]
                self._classes.append(newClass)
        return self


    def calculate_healthRate(self):
        self._problems = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i]._audience._places < classes[i]._subject._studentsMax):
                self._problems += 1
            for j in range(0, len(classes)):
                if (j > i):
                    if (classes[i]._lessonTime == classes[j]._lessonTime):
                        if (classes[i]._audience == classes[j]._audience): self._problems += 1
                        if (classes[i]._teacher == classes[j]._teacher): self._problems += 1
        return 1 / ((1.0*self._problems + 1))


    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue
