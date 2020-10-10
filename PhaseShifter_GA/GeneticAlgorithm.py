import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

#Классы
from StateSystem import StateSystem
from State import State

#Функции ГА
from CalcRMSPhase import CalcRMSPhase
from CalcRMSS21 import CalcRMSS21
from CalcFitness import CalcFitness
from GetSystemRandom import GetSystemRandom
from getStateForGA import getStateForGA
from getState import getState

from Panmixis import Panmixis
from Inbreeding import Inbreeding
from Outbreeding import Outbreeding
from Evolution import Evolution
from Mutation import Mutation


from RemoveTwins import RemoveTwins


from RMSPhaseForFreq import RMSPhaseForFreq
from RMSS21ForFreq import RMSS21ForFreq
from Calc_RMS_List_Phase import Calc_RMS_List_Phase
from Calc_RMS_List_S21 import Calc_RMS_List_S21




import ConfigModule

def GeneticAlgorithm(PopulSize, FitnessGoal, MutationCoefficient, Iteration):


    Population = [];
    IterationList = []
    FitnessList  = []
    #Start
    #Creating Population
    for i in range(PopulSize):
        Population.append(GetSystemRandom()); 
    Population = sorted(Population, key = lambda StateSystem: StateSystem.FitnessValue)
    #Population = sorted(Population, key = lambda StateSystem: StateSystem.FitnessValue)
    IterationCounter = 0;
    Iteration = Iteration;
    #Start GA
   
    while IterationCounter<Iteration:
        IterationCounter = IterationCounter + 1;
        IterationList.append(IterationCounter);
        FitnessList.append(Population[0].FitnessValue);
        Child_Population = [];
        Child_Mutant = [];
        Population_Mutant = [];
        MutantPopulation = [];
        EvolutionList = []
        print('Start Iteration! '+str(IterationCounter))
        print('Best fitness Before iteration is '+str(Population[0].FitnessValue))
        for i in range(0,PopulSize,1):
            Child_Population.append(Outbreeding(Population));
            Child_Population.append(Inbreeding(Population));
            Child_Population.append(Panmixis(Population));
        for i in range(0,len(Child_Population)//2,1):
            MutantPopulation.append(Mutation(Child_Population[i],MutationCoefficient)) 
        #for i in range(0,32,1):
        #   EvolutionList.append(Evolution(Population[i]));
        Population = Population + Child_Population + MutantPopulation #+ EvolutionList;
        Population = sorted(Population, key = lambda StateSystem: StateSystem.FitnessValue)
        Population = RemoveTwins(Population);
        print('Total Population is ' + str(len(Population)))
        del Population[PopulSize:(len(Population))];
        print('Population After '+str(len(Population)));
        print('Best fitness After iteration is '+str(Population[0].FitnessValue))
        print ('List of Fitness.....');
        print('S21 is !!!!!! '+str(Population[0].RMS_S21))
        for i in range(0,9,1):
            print('Chromosome '+str(i)+' Fitness is '+str(Population[i].FitnessValue));
        if Population[0].FitnessValue<FitnessGoal:
            print('GA is Successful!!!!')
            break

    FinalSolution = Population[0];

    return FinalSolution, IterationList, FitnessList



