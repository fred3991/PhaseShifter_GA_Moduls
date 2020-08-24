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


from FullDataSet import FullDataSet

from CreateDataSet import CreateDataSet

import ConfigModule

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




## Options
## Start GA;
##Set frequency in GHz

## def GeneticAlgorithm(PopulSize, FitnessGoal, MutationCoefficient, Iteration):
##    return FinalSolution, IterationList, FitnessList

#FinalSolution, IterationList, FitnessList = GeneticAlgorithm(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);

##class FinalSystemData: StateList, RMS_Phase_List, RMS_S21_List, StateSystemName
#DataResult = GetFinalSystem(FinalSolution); 

##########################Save Calibre Txt#################################
#ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz.txt', 'w')
#ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
#ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
#ConfigStateFile.write(DataResult.StateSystemName);
#ConfigStateFile.close;
###############################################################################

#FullDataSet_12GHz = CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult);
#pickle.dump(FullDataSet_12GHz, open('FullDataSet_12GHz.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);



# Options
# Start GA;
#Set frequency in GHz

# def GeneticAlgorithm(PopulSize, FitnessGoal, MutationCoefficient, Iteration):
#    return FinalSolution, IterationList, FitnessList


#FinalSolution, IterationList, FitnessList = GeneticAlgorithm(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);
#DataResult = GetFinalSystem(FinalSolution); 

#ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz.txt', 'w')
#ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
#ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
#ConfigStateFile.write(DataResult.StateSystemName);
#ConfigStateFile.close;


#FullDataSet_8GHz = CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult);

#pickle.dump(FullDataSet_8GHz, open('FullDataSet_'+str(ConfigModule.frequency)+'GHz.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);


#                        Final_StateList, 
#                       CentralFrequency, 
#                       RMS_Phase_CentralFrequency, 
#                       RMS_S21_CentralFrequency, 
#                       FitnessValue_CentralFrequency, 
#                       Final_Iteration_List, 
#                       Final_Fitness_List,
#                       Final_List_Frequencies, 
#                       Final_RMS_Phase_List, 
#                       Final_RMS_S21_List):


################################  8  GHz
#DataSetResult_8GHz = pickle.load(open('FullDataSet_8GHz.pkl', 'rb'));
#print('загрузил?!!!!');



################################  12  GHz
DataSetResult_8GHz = pickle.load(open('FullDataSet_8GHz.pkl', 'rb'));
print('загрузил?!!!!');

#график РМС фазы
Plot_RMS_Phase_vs_Frequency = DrawFunction(
                              DataSetResult_8GHz.Final_List_Frequencies, 
                              DataSetResult_8GHz.Final_RMS_Phase_List, 
                     ( int(min(DataSetResult_8GHz.Final_List_Frequencies)-1),               int(max(DataSetResult_8GHz.Final_List_Frequencies)+2)     ),
                     ( min(DataSetResult_8GHz.Final_RMS_Phase_List)-min(DataSetResult_8GHz.Final_RMS_Phase_List),  max(DataSetResult_8GHz.Final_RMS_Phase_List)+min(DataSetResult_8GHz.Final_RMS_Phase_List)   ), 
                     np.arange( int(min(DataSetResult_8GHz.Final_List_Frequencies)-1),               int(max(DataSetResult_8GHz.Final_List_Frequencies)+2) , step=1 ), 
                     np.arange( min(DataSetResult_8GHz.Final_RMS_Phase_List)-min(DataSetResult_8GHz.Final_RMS_Phase_List),  max(DataSetResult_8GHz.Final_RMS_Phase_List)+min(DataSetResult_8GHz.Final_RMS_Phase_List)   , step = 0.5  ), 
                     'ro', 4, str('RMS Phase Error '+str(DataSetResult_8GHz.CentralFrequency)+' GHz'), 'Frequency, GHz', 'RMS Phase Error, °', 'RMS phase error vs. freq');
########################################


print(DataSetResult_8GHz.RMS_Phase_CentralFrequency);
print(DataSetResult_8GHz.RMS_S21_CentralFrequency);

R_S21 =  DataSetResult_8GHz.Final_S21_List;
theta =  DataSetResult_8GHz.Final_Phase_List;

theta = np.ndarray.tolist(theta);
NewTheta = [];
New_R21 = [];

for i in range(len(theta)):
    NewTheta.append(theta[i]*(np.pi/180))

for j in range(len(R_S21)):
    New_R21.append(20**(R_S21[j]/10))


Type_RS21 = type(New_R21);
Type_Theta = type(NewTheta);

plt.polar(NewTheta,  New_R21, 'rh', MarkerSize = 4);
plt.show();


FinalSet_List = [];
FreqStates = []


def getPhaseFreq(State_Number, BitA, BitB, Freq):
    ntwk = rf.Network('C:/Users/FedorovEA/data/state'+str(State_Number)+'/PS_test__'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB)+'.s2p')
    Fi  = float(ntwk.s21[str(Freq)+'ghz'].s_deg[...]);
    StatePhase = Fi;
    return StatePhase


FinalSet_List = [];
PhaseListFreq = [];



for allstates in range(0,64,1):
    for allfreqlist in np.arange(7.5,8.6,0.1):
        print('я работаю, подожди  '+str(allstates));
        PhaseListFreq.append(getPhaseFreq(allstates,DataSetResult_8GHz.Final_StateList[allstates].StateBitA,DataSetResult_8GHz.Final_StateList[allstates].StateBitB,allfreqlist))

 
    FinalSet_List.append(PhaseListFreq);
    PhaseListFreq=[];



FirstStatePhaseList = [];

for i in range(len(np.arange(7.5,8.6,0.1))):
    FirstStatePhaseList.append(FinalSet_List[0][i]);

for freq_range in range(len(np.arange(7.5,8.6,0.1))):
    for states_unwrap in range(0,64,1):
        FinalSet_List[states_unwrap][freq_range] = FinalSet_List[states_unwrap][freq_range]-FirstStatePhaseList[freq_range];


Final_List_Phases = [];

for freqlist in range(len(np.arange(7.5,8.6,0.1))):

    FreqOneList = [];

    for i in range(0,64,1):

        FreqOneList.append(FinalSet_List[i][freqlist]-FinalSet_List[0][freqlist]);
      
    FreqOneList = np.deg2rad(FreqOneList);
    FreqOneList = np.unwrap(FreqOneList);
    FreqOneList = np.rad2deg(FreqOneList);
    Final_List_Phases.append(FreqOneList)
 

SuperFinal = [];
TempFreqs = [];
for freq_range in range(len(np.arange(7.5,8.6,0.1))):
    for states_unwrap in range(0,64,1):
        TempFreqs.append(Final_List_Phases[freq_range][states_unwrap]);

    SuperFinal.append(TempFreqs);
    TempFreqs = [];




LastChance = [];
Tempo = [];

for j in range(0,64,1):
    for i in range(len(np.arange(7.5,8.6,0.1))):
        Tempo.append(SuperFinal[i][j]);
    LastChance.append(Tempo);
    Tempo = [];




x = np.arange(7.5,8.6,0.1);

for i in range(0,64,1):
    plt.plot(x,LastChance[i]);

plt.xlabel('Частота, ГГц')
plt.ylabel('Фаза сигнала, °')
plt.show();




#NormalPhaseList = [];

#for state in range(0,64,1):
#    Phase = state*5.625*(np.pi/180);
#    NormalPhaseList.append(Phase);

#NormalS21 = [];

#for state in range(0,64,1):
#    S21 = 3;
#    NormalS21.append(S21);


#plt.polar(NormalPhaseList,  NormalS21 , 'b+', NewTheta,  New_R21, 'ko', MarkerSize = 3);
#plt.show();


print('END All!!!!');




























##def DrawFunction(x, y, xlim, ylim, xTicks, yTicks, LineColorType, MarkerSize, LineLabel, xlabel, ylabel, plotTitle):

#Plot_RMS_S21_vs_Frequency = DrawFunction(
#                      ConfigModule.List_Frequencies, 
#                      DataResult.RMS_S21_List, 

#                     ( float(min(ConfigModule.List_Frequencies)-1),               float(max(ConfigModule.List_Frequencies)+1)        ),

#                     ( 0, round(round(float(max(DataResult.RMS_S21_List)),2)+round(float(min(DataResult.RMS_S21_List))),2)           ), 

#                     np.arange(float(min(ConfigModule.List_Frequencies)-1),   float(max(ConfigModule.List_Frequencies)),          step=1), 

#                     np.arange(0 ,   float(max(DataResult.RMS_S21_List)), step=round(min(DataResult.RMS_S21_List),1)), 

#                     'b*', 4, str('RMS S21 Error '+str(ConfigModule.frequency)+' GHz'), 'Frequency, GHz', 'RMS S21 Error, °', 'RMS S21 error vs. freq');


##Plot_Fitness_vs_Iterations = DrawFunction(

##                      IterationList, 
##                      FitnessList, 
##                     ( 0,               max(IterationList)  ),

##                     ( 0,                                              round(float(max(FitnessList)))), 

##                     np.arange(0,   float(max(IterationList)),          step=(ConfigModule.Iterations//10)), 

##                     np.arange(0 ,   float(max(FitnessList)+1), step=round(min(FitnessList),2)), 

##                     'g*', 4, str('Iterations'), 'Iterations', 'Fitness Value', 'Iterations vs. Fitness Value');







