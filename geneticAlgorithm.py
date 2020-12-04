from evaluation import *
from data import *
import random as rnd
INDIVIDUALS = 10
INDIVIDUALS_TO_THE_NEXT_ROUND = 1
INDIVIDUALS_TO_CHANGE = 3
MUTATION_POSSIBILITY = 0.1

class Population:
    def __init__(self, size):
        self._size = size
        self._data = Data()
        self._schedules = []
        for i in range(0, size): self._schedules.append(Evaluation().initialize())


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(INDIVIDUALS_TO_THE_NEXT_ROUND):
            crossover_pop._schedules.append(pop._schedules[i])
        i = INDIVIDUALS_TO_THE_NEXT_ROUND
        while i < INDIVIDUALS:
            schedule1 = self._select_for_change(pop)._schedules[0]
            schedule2 = self._select_for_change(pop)._schedules[0]
            crossover_pop._schedules.append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop


    def _mutate(self, population):
        for i in range(INDIVIDUALS_TO_THE_NEXT_ROUND, INDIVIDUALS):
            self._mutate_one(population._schedules[i])
        return population


    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Evaluation().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5): crossoverSchedule.get_classes()[i] = schedule1._classes[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule


    def _mutate_one(self, mutateSchedule):
        schedule = Evaluation().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_POSSIBILITY > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule


    def _select_for_change(self, pop):
        change_pop = Population(0)
        i = 0
        while i < INDIVIDUALS_TO_CHANGE:
            change_pop._schedules.append(pop._schedules[rnd.randrange(0, INDIVIDUALS)])
            i += 1
        change_pop._schedules.sort(key=lambda x: x.get_healthRate(), reverse=True)
        return change_pop
