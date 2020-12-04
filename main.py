from data import *
from university import *
from geneticAlgorithm import *
from evaluation import *
import prettytable as prettytable

def print_generation(population):
    schedules = population._schedules
    table_data = prettytable.PrettyTable(['schedule number', 'health rate', 'numb of conflicts'])  #, 'classes [spec,class,audience,teacher,lesson time]'])
    for i in range(0, len(schedules)):
        table_data.add_row([str(i), str(round(schedules[i]._healthRate,3)), str(schedules[i]._problems)])  #, schedules[i].__str__()])
    print(table_data)


def print_schedule_as_table(schedule):
    classes = schedule.get_classes()
    table = prettytable.PrettyTable(['Class #', 'Spec', 'Course (number, max num of students)', 'Room (Capacity)', 'Teacher',  'Lesson Time)'])
    for i in range(0, len(classes)):
        table.add_row([str(i), classes[i]._spec._name, classes[i]._subject._name + " (" +
                       str(classes[i]._subject._studentsMax) +")",
                       classes[i]._audience._number + " (" + str(classes[i]._audience._places) + ")",
                       classes[i]._teacher._name ,
                       classes[i]._lessonTime._time])
    print(table)


data = Data()
generationNumber = 0
print("\n> Generation # "+str(generationNumber))
population = Population(INDIVIDUALS)
population._schedules.sort(key=lambda x: x.get_healthRate(), reverse=True)
print_generation(population)
print_schedule_as_table(population._schedules[0])
geneticAlgorithm = GeneticAlgorithm()
while (population._schedules[0].get_healthRate() != 1.0):
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population._schedules.sort(key=lambda x: x.get_healthRate(), reverse=True)
    print_generation(population)
    print_schedule_as_table(population._schedules[0])
print("\n\n")
