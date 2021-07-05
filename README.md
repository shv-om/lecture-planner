# lecture-planner
Automatic Lecture planner application for schools and colleges
using Genetic Algorithm.

##ALGORITHM

    First, an initial generation of chromosomes is created randomly and their fitness value is analysed.

    New generations are created after this. For each geneartion, it performs the following:
        Preserve few fittest chromosomes from the previous geneartion as it is. (ELITISM)
        Randomly select a pair of chromosomes from previous generation. (Try Roulette wheel selection method)
        Perform crossover depending on crossover rate. (try single point crossover)
        perform mutation on the more fit chromosome so obtained depending on mutation rate.(kept small usually)

    Analyze the fitness of new generation and order them acc to fitness values.

    Repeat creating new generations unless chromosomes of desired fitness value are obtained i.e. fitness = 1. (stopping criteria)
