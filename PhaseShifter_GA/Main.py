import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

import os.path
import datetime


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

from getStateAllFreq import getStateAllFreq

from RemoveTwins import RemoveTwins

from GeneticAlgorithm import GeneticAlgorithm

from RMSPhaseForFreq import RMSPhaseForFreq
from RMSS21ForFreq import RMSS21ForFreq
from Calc_RMS_List_Phase import Calc_RMS_List_Phase
from Calc_RMS_List_S21 import Calc_RMS_List_S21

from FinalSystemData import FinalSystemData

from GetFinalSystem import GetFinalSystem
from DrawFunction import DrawFunction



import ConfigModule



# Options
# Start GA;
#Set frequency in GHz



#ConfigModule.frequency = 8; #Frequency in GHz
#ConfigModule.List_Frequencies = np.arange(3, 20, 1); # Нужный лист частот для посмотрое
#ConfigModule.MutationCoefficient = 3;
#ConfigModule.FitnessGoal = 0;
#ConfigModule.Iterations = 256;
#ConfigModule.PopulSize = 64;


# def GeneticAlgorithm(PopulSize, FitnessGoal, MutationCoefficient, Iteration):
#    return FinalSolution, IterationList, FitnessList


FinalSolution, IterationList, FitnessList = GeneticAlgorithm(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);




#class FinalSystemData: StateList, RMS_Phase_List, RMS_S21_List, StateSystemName
DataResult = GetFinalSystem(FinalSolution); 



ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz.txt', 'w')
ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
ConfigStateFile.write(DataResult.StateSystemName);
ConfigStateFile.close;







#график РМС фазы
Plot_RMS_Phase_vs_Frequency = DrawFunction(ConfigModule.List_Frequencies, 
                      DataResult.RMS_Phase_List, 
                     ( float(min(ConfigModule.List_Frequencies)-1),               float(max(ConfigModule.List_Frequencies)+1)        ),
                     ( 0,                                              round(float(max(DataResult.RMS_Phase_List)))), 
                     np.arange(float(min(ConfigModule.List_Frequencies)-1),   float(max(ConfigModule.List_Frequencies)),          step=1), 
                     np.arange(0 ,   float(max(DataResult.RMS_Phase_List)+1), step=1), 
                     'rh', 4, str('RMS Phase Error '+str(ConfigModule.frequency)+' GHz'), 'Frequency, GHz', 'RMS Phase Error, °', 'RMS phase error vs. freq');


#def DrawFunction(x, y, xlim, ylim, xTicks, yTicks, LineColorType, MarkerSize, LineLabel, xlabel, ylabel, plotTitle):

Plot_RMS_S21_vs_Frequency = DrawFunction(
                      ConfigModule.List_Frequencies, 
                      DataResult.RMS_S21_List, 

                     ( float(min(ConfigModule.List_Frequencies)-1),               float(max(ConfigModule.List_Frequencies)+1)        ),

                     ( 0, round(round(float(max(DataResult.RMS_S21_List)),2)+round(float(min(DataResult.RMS_S21_List))),2)           ), 

                     np.arange(float(min(ConfigModule.List_Frequencies)-1),   float(max(ConfigModule.List_Frequencies)),          step=1), 

                     np.arange(0 ,   float(max(DataResult.RMS_S21_List)), step=round(min(DataResult.RMS_S21_List),1)), 

                     'b*', 4, str('RMS S21 Error '+str(ConfigModule.frequency)+' GHz'), 'Frequency, GHz', 'RMS S21 Error, °', 'RMS S21 error vs. freq');


#Plot_Fitness_vs_Iterations = DrawFunction(

#                      IterationList, 
#                      FitnessList, 
#                     ( 0,               max(IterationList)  ),

#                     ( 0,                                              round(float(max(FitnessList)))), 

#                     np.arange(0,   float(max(IterationList)),          step=(ConfigModule.Iterations//10)), 

#                     np.arange(0 ,   float(max(FitnessList)+1), step=round(min(FitnessList),2)), 

#                     'g*', 4, str('Iterations'), 'Iterations', 'Fitness Value', 'Iterations vs. Fitness Value');







print('END All!!!!');