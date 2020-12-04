class Subject:
    def __init__(self, name, teachers, studentsMax):
        self._name = name
        self._studentsMax = studentsMax
        self._teachers = teachers

    def __str__(self): return self._name

class Teacher:
    def __init__(self, name):
        self._name = name

    def __str__(self): return self._name


class Audience:
    def __init__(self, number, places):
        self._number = number
        self._places = places


class LessonTime:
    def __init__(self, time):
        self._time = time


class Speciality:
    def __init__(self, name, subjects):
        self._name = name
        self._subjects = subjects


class Class:
    def __init__(self, id, spec, subject):
        self._id = id
        self._spec = spec
        self._subject = subject
        self._teacher = None
        self._lessonTime = None
        self._audience = None

    def __str__(self):
        return str(self._spec._name) + "," + str(self._audience._number) + "," + str(self._teacher._name) + "," + str(self._lessonTime._time)
