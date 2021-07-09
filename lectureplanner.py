"""
Automatic Lecture Planner

Inputs:
Batch = []    #contains number of students from each course
rooms = []      #room no. and size of room (mention labs as well)
subjects = []   #subject code and subject
time-period = start time - end time
no_of_days =  # 5 or 6
break = 1 hr  #mention lunch break time
"""

import random
import csv

total_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class LecturePlanner:

    def __init__(self, batches, rooms, subjects, time_period, days_count):
        global total_days

        #self.teachers = self.init_gene(teachers)
        self.batches = self.init_gene(batches)
        self.rooms = self.init_gene(rooms)
        self.subjects = self.init_gene(subjects)
        self.time_period = self.init_gene(time_period)
        self.days = self.init_gene(total_days[:days_count])
        self.fitness = {}

        self.timetable = {}     # Just initialised
        self.new_population = []    # Population updated after every fitness calculation

        # self.timeday = {timeday_key1: {rooms:[], subjects:[]}, timeday_key2: {...}, ... }
        self.timeday = {}


    def __splitter(self, chromosome):
        return [(chromosome[i:i+4]) for i in range(0, len(chromosome), 4)]

    def __timedaydict(self, timeday_key):
        self.timeday[timeday_key] = {'rooms': [], 'subjects': [], 'batches': []}

    
    def init_gene(self, l):
        d = dict()
        for i in range(len(l)):
            num = f'{i:04b}'   # {0:08b}.format(i)
            d[num] = l[i]
        return d


    def init_population(self):
        """
        <teacher/subject, batch, room, time_period, day>
        """

        population = {}

        # Converting Keys into Lists
        subject = list(self.subjects)
        batch = list(self.batches)
        room = list(self.rooms)

        for b in batch:
            population[b] = []
            for day in self.days:
                for time in self.time_period:

                    #chromosome = (random.choice(self.subjects), random.choice(self.batches), random.choice(self.rooms), time, day)

                    chromosome = random.choice(subject) + random.choice(batch) + random.choice(room) + time + day
                    population[b].append(chromosome)

        return population


    def calc_fitness(self, population):
        # We can calculate fitness using hashing on chromosomes

        batch_day = []      # Batch Day Time
        sub_bat_day = []    # Subject Batch Day

        for chromo in population:
            self.fitness[chromo] = 0

            # [Subject, [Batch, Limit], [Room No, Vacancy], Time Period, Day]
            splitted_chromo = self.__splitter(chromo)

            timeday_key = splitted_chromo[3] + splitted_chromo[4]

            self.__timedaydict(timeday_key)

            # performing check for empty rooms
            if splitted_chromo[2] not in self.timeday[timeday_key]['rooms']:
                self.fitness[chromo] += 1
                self.timeday[timeday_key]['rooms'].append(splitted_chromo[2])

            # performing check if the number of students is less than the capacity of the room
            # print(chromo)
            if self.batches[splitted_chromo[1]][1] <= self.rooms[splitted_chromo[2]][1]:
                self.fitness[chromo] += 1

            # performing check if any subject is occuring for another batch at the same time same day
            if splitted_chromo[0] not in self.timeday[timeday_key]['subjects']:
                self.fitness[chromo] += 1
                
                # performing check if the batch is having same subject at the same day
                temp1 = splitted_chromo[0] + splitted_chromo[1] + splitted_chromo[3]
                if temp1 not in sub_bat_day:
                    self.fitness[chromo] += 1
                    sub_bat_day.append(temp1)

                self.timeday[timeday_key]['subjects'].append(splitted_chromo[0])

            # performing check if the batch is having any other subject class at the same time same day
            if splitted_chromo[1] not in self.timeday[timeday_key]['batches']:
                temp = splitted_chromo[1] + splitted_chromo[3] + splitted_chromo[4]
                if temp not in batch_day:
                    self.fitness[chromo] += 1
                    self.timeday[timeday_key]['batches'].append(splitted_chromo[1])
                    batch_day.append(temp)


            if self.fitness[chromo] == 5 and chromo in self.new_population:
                self.new_population.remove(chromo)

        #print(self.timeday, len(self.timeday), subject_day, sep="\n")


    def crossover(self, pop):

        newpop = []
        choices = [4, 8, 12, 16]

        paired = [[pop[x], pop[x+1]] for x in range(0, len(pop)-1, 2)]
        
        for chromo_pairs in paired:
            #performing single point crossover
            c1 = list(chromo_pairs[0])
            c2 = list(chromo_pairs[1])
            
            #selecting a random point
            r = random.choice(choices)
            #print('crossover pt:',r)
            
            for i in range(r, len(c1)):
                c1[i], c2[i] = c2[i], c1[i]
                chrome1 = ''.join(c1)
                chrome2 = ''.join(c2)

            newpop.extend([chrome1, chrome2])
        
        return newpop


    def mutation(self, pop):

        newpop = []
        
        for chrome in pop:
            r = random.randint(0,19)
            #print('mutation pt',r)
            chrome = list(chrome)
            chrome[r] = str(1 - int(chrome[r]))
            chrome = ''.join(chrome)

            newpop.append(chrome)
        
        return newpop


    def makecsv(self, population):

        top_header = [self.time_period[x] for x in self.time_period]
        side_header = [y for y in self.days]

        pop = []
        for i in population:
            pop.extend(population[i])
        
        with open('timetable.csv', 'w', encoding='UTF-8') as f:

            writer = csv.writer(f)

            writer.writerow(top_header)

            data_list = [pop[i:i+7] for i in range(0, len(pop), 7)]

            for data in data_list:
                data1 = []
                for chromo in data:
                    data1.append([self.subjects[chromo[:4]], self.batches[chromo[4:8]][0], self.rooms[chromo[8:12]][0]])
                #print(data1)
                writer.writerow(data1)


    def print_pop(self, population, fitness):
        
        #population = self.init_population()

        for pop in population:
            for chromosome in population[pop]:
                print(chromosome, fitness[chromosome], '--> ' + self.subjects[chromosome[:4]], self.batches[chromosome[4:8]], self.rooms[chromosome[8:12]], self.time_period[chromosome[12:16]], self.days[chromosome[16:]], sep=", ")


    def planner(self):
        population = self.init_population()

        for i in population:
            self.new_population.extend(population[i])

        #self.print_pop(population, self.fitness)

        while True:
            if self.new_population != []:
                self.calc_fitness(self.new_population)
                self.new_population = self.crossover(self.new_population)
                print(len(self.new_population))

            else:
                break

        #self.makecsv(population)
