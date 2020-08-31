import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle
import time

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


FinalSolution, IterationList, FitnessList = GeneticAlgorithm(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);
DataResult = GetFinalSystem(FinalSolution); 

ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz_SmallPopul32.txt', 'w')
ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
ConfigStateFile.write(DataResult.StateSystemName);
ConfigStateFile.close;

FullDataSet = CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult);
pickle.dump(FullDataSet, open('FullDataSet_'+str(ConfigModule.frequency)+'GHz_SmallPopul32.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);




#############################    GHz
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#print('загрузил?!!!!');

##график РМС фазы
#Plot_RMS_Phase_vs_Frequency = DrawFunction(
#                              ViewResult.Final_List_Frequencies, 
#                              ViewResult.Final_RMS_Phase_List, 
#                     ( int(min(ViewResult.Final_List_Frequencies)),               int(max(ViewResult.Final_List_Frequencies))     ),
#                     ( min(ViewResult.Final_RMS_Phase_List)-min(ViewResult.Final_RMS_Phase_List),  max(ViewResult.Final_RMS_Phase_List)+min(ViewResult.Final_RMS_Phase_List)   ), 
#                     np.arange( int(min(ViewResult.Final_List_Frequencies)),               int(max(ViewResult.Final_List_Frequencies)) , step=1 ), 
#                     np.arange( min(ViewResult.Final_RMS_Phase_List)-min(ViewResult.Final_RMS_Phase_List),  max(ViewResult.Final_RMS_Phase_List)+min(ViewResult.Final_RMS_Phase_List)   , step = 0.5  ), 
#                     'ro', 2.5, str('RMS Phase Error '+str(ViewResult.CentralFrequency)+' GHz'), 'Frequency, GHz', 'RMS Phase Error, °', 'RMS phase error vs. freq' );
######################################

#plt.grid(color='k', linestyle='--', linewidth=0.3)
#plt.ylabel('∆ Отклонение фазы, °');  # Подписи у
#plt.xlabel('Состояние');  # Подписи х

#plt.plot(ViewResult.Final_List_Frequencies,  ViewResult.Final_RMS_Phase_List);
#plt.plot(ViewResult12.Final_List_Frequencies,  ViewResult12.Final_RMS_Phase_List);

#plt.show;



#IdealPhaseList = [];

#for state in range(0,64,1):
#    Phase = state*5.625;
#    IdealPhaseList.append(Phase);

#RealPhaseList = np.ndarray.tolist(ViewResult.Final_Phase_List)

#x = np.arange(0,64,1);
#deltaPhase = []
#for i in range(0,64,1):
#    deltaPhase.append((RealPhaseList[i]-IdealPhaseList[i]));


#plt.grid(color='k', linestyle='--', linewidth=0.3)
#plt.ylabel('∆ Отклонение фазы, °');  # Подписи у
#plt.xlabel('Состояние');  # Подписи х
#plt.xlim(0,63);   # границы X
#plt.xticks(np.arange(0,64,1))
#plt.yticks(np.arange(-2,2,0.1))
#plt.grid(color='k', linestyle='--', linewidth=0.3);
#plt.plot(x,deltaPhase, '-o',   markersize = 5, markerfacecolor = 'r',  label='dsfsd');
#plt.legend(loc=0);
#plt.show();


#print('END All!!!!');



####################



############### СКО ФАЗА ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult85 = pickle.load(open('FullDataSet_8.5GHz.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz.pkl', 'rb'));
#ViewResult95 = pickle.load(open('FullDataSet_9.5GHz.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#ViewResult105 = pickle.load(open('FullDataSet_10.5GHz.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz.pkl', 'rb'));
#ViewResult115 = pickle.load(open('FullDataSet_11.5GHz.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz.pkl', 'rb'));


#print('загрузил?!!!!');

#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_Phase_List
#y2 = ViewResult85.Final_RMS_Phase_List;
#y3 = ViewResult9.Final_RMS_Phase_List;
#y4 = ViewResult95.Final_RMS_Phase_List;
#y5 = ViewResult10.Final_RMS_Phase_List;
#y6 = ViewResult105.Final_RMS_Phase_List;
#y7 = ViewResult11.Final_RMS_Phase_List;
#y8 = ViewResult115.Final_RMS_Phase_List;
#y9 = ViewResult12.Final_RMS_Phase_List;

#plt.ylabel('RMS Phase Error, °');  # Подписи у
#plt.xlabel('Frequency, GHz');  # Подписи х

#plt.xlim(5,               15     );  
#plt.ylim(0,               5.5 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0,5,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro-', markersize = 4, markerFacecolor = 'k', label ='8 GHz');
#plt.plot(x,y2, 'go-', markersize = 4,  markerFacecolor = 'y',label ='8.5 GHz');
#plt.plot(x,y3, 'bh-', markersize = 4,  markerFacecolor = 'w',label ='9 GHz');
#plt.plot(x,y4, 'kd-', markersize = 4,  markerFacecolor = 'k',label ='9.5 GHz');
#plt.plot(x,y5, 'mh-', markersize = 4, markerFacecolor = 'k', label ='10 GHz');
#plt.plot(x,y6, 'yo-', markersize = 4,  markerFacecolor = 'g',label ='10.5 GHz');
#plt.plot(x,y7, 'cd-', markersize = 4,  markerFacecolor = 'k',label ='11 GHz');
#plt.plot(x,y8, 'kh-', markersize = 4,  markerFacecolor = 'y',label ='11.5 GHz');
#plt.plot(x,y9, 'ko-', markersize = 4,  markerFacecolor = 'w',label ='12 GHz');

#plt.legend(loc=0);
#plt.show()
###########################################################

############### СКО S21 ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult85 = pickle.load(open('FullDataSet_8.5GHz.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz.pkl', 'rb'));
#ViewResult95 = pickle.load(open('FullDataSet_9.5GHz.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#ViewResult105 = pickle.load(open('FullDataSet_10.5GHz.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz.pkl', 'rb'));
#ViewResult115 = pickle.load(open('FullDataSet_11.5GHz.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz.pkl', 'rb'));


#print('загрузил?!!!!');

#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_S21_List
#y2 = ViewResult85.Final_RMS_S21_List;
#y3 = ViewResult9.Final_RMS_S21_List;
#y4 = ViewResult95.Final_RMS_S21_List;
#y5 = ViewResult10.Final_RMS_S21_List;
#y6 = ViewResult105.Final_RMS_S21_List;
#y7 = ViewResult11.Final_RMS_S21_List;
#y8 = ViewResult115.Final_RMS_S21_List;
#y9 = ViewResult12.Final_RMS_S21_List;

#plt.ylabel('RMS S21 Error, dB');  # Подписи у
#plt.xlabel('Frequency, GHz');  # Подписи х

#plt.xlim(5,               15     );  
#plt.ylim(0.1,               0.75 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0.1,0.75,0.05))

#plt.grid(color='k', linestyle='--', linewidth=0.3)


#plt.plot(x,y1, 'ro-', markersize = 4, markerFacecolor = 'k', label ='8 GHz');
#plt.plot(x,y2, 'go-', markersize = 4,  markerFacecolor = 'y',label ='8.5 GHz');
#plt.plot(x,y3, 'bh-', markersize = 4,  markerFacecolor = 'w',label ='9 GHz');
#plt.plot(x,y4, 'kd-', markersize = 4,  markerFacecolor = 'k',label ='9.5 GHz');
#plt.plot(x,y5, 'mh-', markersize = 4, markerFacecolor = 'k', label ='10 GHz');
#plt.plot(x,y6, 'yo-', markersize = 4,  markerFacecolor = 'g',label ='10.5 GHz');
#plt.plot(x,y7, 'cd-', markersize = 4,  markerFacecolor = 'k',label ='11 GHz');
#plt.plot(x,y8, 'kh-', markersize = 4,  markerFacecolor = 'y',label ='11.5 GHz');
#plt.plot(x,y9, 'ko-', markersize = 4,  markerFacecolor = 'w',label ='12 GHz');

#plt.legend(loc=0);
#plt.show()
############################################################


############### ГА Анализ Итерации - фитнес ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult85 = pickle.load(open('FullDataSet_8.5GHz.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz.pkl', 'rb'));
#ViewResult95 = pickle.load(open('FullDataSet_9.5GHz.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#ViewResult105 = pickle.load(open('FullDataSet_10.5GHz.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz.pkl', 'rb'));
#ViewResult115 = pickle.load(open('FullDataSet_11.5GHz.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz.pkl', 'rb'));

                      
#print('загрузил?!!!!');

#x = ViewResult.Final_Iteration_List;
#y1 = ViewResult.Final_Fitness_List
#y2 = ViewResult85.Final_Fitness_List;
#y3 = ViewResult9.Final_Fitness_List;
#y4 = ViewResult95.Final_Fitness_List;
#y5 = ViewResult10.Final_Fitness_List;
#y6 = ViewResult105.Final_Fitness_List;
#y7 = ViewResult11.Final_Fitness_List;
#y8 = ViewResult115.Final_Fitness_List;
#y9 = ViewResult12.Final_Fitness_List;

#plt.ylabel('Fitness Value');  # Подписи у
#plt.xlabel('Iterations');  # Подписи х

#plt.xlim(0,               4096     );  
#plt.ylim(0.4,              1.2 );  

#plt.xscale("linear");

#plt.xticks(np.arange(0,4096,500))
#plt.yticks(np.arange(0.4,1.2,0.1))

#plt.grid(color='k', linestyle='--', linewidth=0.3)


#plt.plot(x,y1, 'r-.', markersize = 2, markerFacecolor = 'k', label ='8 GHz');
#plt.plot(x,y2, 'g.-', markersize = 2,  markerFacecolor = 'y',label ='8.5 GHz');
#plt.plot(x,y3, 'b.--', markersize = 2,  markerFacecolor = 'w',label ='9 GHz');
#plt.plot(x,y4, 'k.-', markersize = 2,  markerFacecolor = 'k',label ='9.5 GHz');
#plt.plot(x,y5, 'm.-.', markersize = 2, markerFacecolor = 'k', label ='10 GHz');
#plt.plot(x,y6, 'y-.', markersize = 2,  markerFacecolor = 'g',label ='10.5 GHz');
#plt.plot(x,y7, 'c-.', markersize = 2,  markerFacecolor = 'k',label ='11 GHz');
#plt.plot(x,y8, 'k--', markersize = 2,  markerFacecolor = 'y',label ='11.5 GHz');
#plt.plot(x,y9, 'k.-.', markersize = 2,  markerFacecolor = 'w',label ='12 GHz');

#plt.legend(loc=0);
#plt.show()
###########################################################


############### ГА Анализ Мутациии - фитнес ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResultMut30 = pickle.load(open('FullDataSet_8GHz_PhaseOnly_Mut_30.pkl', 'rb'));

                      
#print('загрузил?!!!!');

#x = ViewResult.Final_Iteration_List;

#y1 = ViewResult.Final_Fitness_List
#y2 = ViewResultMut30.Final_Fitness_List;


#plt.ylabel('Fitness Value');  # Подписи у
#plt.xlabel('Iterations');  # Подписи х

#plt.xlim(0,               4096     );  
#plt.ylim(0,              2 );  

#plt.xticks(np.arange(0,4096,500))
#plt.yticks(np.arange(0,2,0.1))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro', markersize = 2, label ='Mutation 3 %');
#plt.plot(x,y2, 'k+', markersize = 2, label ='Mutation 30 %');


#plt.legend(loc=0);
#plt.show()
############################################################


############### ГА Анализ Кроссинговер - фитнес ВСЕ общее########################################
#ViewResult1 = pickle.load(open('FullDataSet_8GHz_PhaseOnly_PanmixOnly.pkl', 'rb'));
#ViewResult2 = pickle.load(open('FullDataSet_8GHz_PhaseOnly_Outbreed.pkl', 'rb'));
#ViewResult3 = pickle.load(open('FullDataSet_8GHz_PhaseOnly_InbredOnly.pkl', 'rb'));
#ViewResult4 = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
                      
#print('загрузил?!!!!');

#x = ViewResult1.Final_Iteration_List;

#y1 = ViewResult1.Final_Fitness_List
#y2 = ViewResult2.Final_Fitness_List;
#y3 = ViewResult3.Final_Fitness_List;
#y4 = ViewResult4.Final_Fitness_List;

#plt.ylabel('Fitness Value');  # Подписи у
#plt.xlabel('Iterations');  # Подписи х

#plt.xlim(0,               4096    );  
#plt.ylim(0.4,              1.9 );  

#plt.xticks(np.arange(0,4096,100))
#plt.yticks(np.arange(0.4,1.9,0.1))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'rh-', markersize = 3.5,markerFacecolor = 'k', label ='Panmix Only');
#plt.plot(x,y2, 'go-', markersize = 3.5, markerFacecolor = 'w',label ='Outbreeding Only');
#plt.plot(x,y3, 'b*-', markersize = 3.5,markerFacecolor = 'y', label ='Inbreeding Only');
#plt.plot(x,y4, 'k+-', markersize = 3.5, markerFacecolor = 'r',label ='All %');

#plt.legend(loc=0);
#plt.show()
############################################################



############### СКО ФАЗА Только фаза########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult85 = pickle.load(open('FullDataSet_8.5GHz_PhaseOnly.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz_PhaseOnly.pkl', 'rb'));
#ViewResult95 = pickle.load(open('FullDataSet_9.5GHz_PhaseOnly.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz_PhaseOnly.pkl', 'rb'));
#ViewResult105 = pickle.load(open('FullDataSet_10.5GHz_PhaseOnly.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz_PhaseOnly.pkl', 'rb'));
#ViewResult115 = pickle.load(open('FullDataSet_11.5GHz_PhaseOnly.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz_PhaseOnly.pkl', 'rb'));


#print('загрузил?!!!!');

#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_Phase_List
#y2 = ViewResult85.Final_RMS_Phase_List;
#y3 = ViewResult9.Final_RMS_Phase_List;
#y4 = ViewResult95.Final_RMS_Phase_List;
#y5 = ViewResult10.Final_RMS_Phase_List;
#y6 = ViewResult105.Final_RMS_Phase_List;
#y7 = ViewResult11.Final_RMS_Phase_List;
#y8 = ViewResult115.Final_RMS_Phase_List;
#y9 = ViewResult12.Final_RMS_Phase_List;

#plt.ylabel('RMS Phase Error, °');  # Подписи у
#plt.xlabel('Frequency, GHz');  # Подписи х

#plt.xlim(5,               15.5     );  
#plt.ylim(0,               5 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0,5,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro-', markersize = 4, markerFacecolor = 'k', label ='8 GHz');
#plt.plot(x,y2, 'go-', markersize = 4,  markerFacecolor = 'y',label ='8.5 GHz');
#plt.plot(x,y3, 'bh-', markersize = 4,  markerFacecolor = 'w',label ='9 GHz');
#plt.plot(x,y4, 'kd-', markersize = 4,  markerFacecolor = 'k',label ='9.5 GHz');
#plt.plot(x,y5, 'mh-', markersize = 4, markerFacecolor = 'k', label ='10 GHz');
#plt.plot(x,y6, 'yo-', markersize = 4,  markerFacecolor = 'g',label ='10.5 GHz');
#plt.plot(x,y7, 'cd-', markersize = 4,  markerFacecolor = 'k',label ='11 GHz');
#plt.plot(x,y8, 'kh-', markersize = 4,  markerFacecolor = 'y',label ='11.5 GHz');
#plt.plot(x,y9, 'ko-', markersize = 4,  markerFacecolor = 'w',label ='12 GHz');

#plt.legend(loc=0);
#plt.show()
#############################################################


############### СКО ФАЗА человек и нет общее########################################
#ViewResult =  pickle.load(open('FullDataSet_10GHz_PhaseOnly.pkl', 'rb'));
#ViewResultHuman =  pickle.load(open('FullDataSet_10GHz_Human.pkl', 'rb'));

#print('загрузил?!!!!');

#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_Phase_List
#y2 = ViewResultHuman.Final_RMS_Phase_List;


#plt.ylabel('RMS Phase Error, °');  # Подписи у
#plt.xlabel('Frequency, GHz');  # Подписи х

#plt.xlim(5,               15     );  
#plt.ylim(0,               4 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0,4,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro-', markersize = 4, markerFacecolor = 'k', label ='10 GHz GA');
#plt.plot(x,y2, 'ko-', markersize = 4,  markerFacecolor = 'y',label ='10 GHz Human');


#plt.legend(loc=0);
#plt.show()
###########################################################




###################Круговая градусы
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));


#R_S21 =  ViewResult10.Final_S21_List;
#theta =  ViewResult10.Final_Phase_List;

#theta = np.ndarray.tolist(theta);
#NewTheta = [];
#New_R21 = [];

#for i in range(len(theta)):
#    NewTheta.append(theta[i]*(np.pi/180))

#for j in range(len(R_S21)):
#    New_R21.append(20**(R_S21[j]/10))


#Type_RS21 = type(New_R21);
#Type_Theta = type(NewTheta);

#plt.polar(NewTheta,  New_R21, 'rh', MarkerSize = 4);
#plt.show();
###############################################################



###################### Градусы по состояниям #####################
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#FinalSet_List = [];
#FreqStates = []


#def getPhaseFreq(State_Number, BitA, BitB, Freq):
#    ntwk = rf.Network('C:/Users/FedorovEA/data/state'+str(State_Number)+'/PS_test__'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB)+'.s2p')
#    Fi  = float(ntwk.s21[str(Freq)+'ghz'].s_deg[...]);
#    StatePhase = Fi;
#    return StatePhase


#FinalSet_List = [];
#PhaseListFreq = [];



#for allstates in range(0,64,1):
#    for allfreqlist in np.arange(5,15,0.1):
#        print('я работаю, подожди  '+str(allstates));
#        PhaseListFreq.append(getPhaseFreq(allstates,ViewResult10.Final_StateList[allstates].StateBitA,ViewResult10.Final_StateList[allstates].StateBitB,allfreqlist))

 
#    FinalSet_List.append(PhaseListFreq);
#    PhaseListFreq=[];



#FirstStatePhaseList = [];

#for i in range(len(np.arange(5,15,0.1))):
#    FirstStatePhaseList.append(FinalSet_List[0][i]);

#for freq_range in range(len(np.arange(5,15,0.1))):
#    for states_unwrap in range(0,64,1):
#        FinalSet_List[states_unwrap][freq_range] = FinalSet_List[states_unwrap][freq_range]-FirstStatePhaseList[freq_range];


#Final_List_Phases = [];

#for freqlist in range(len(np.arange(5,15,0.1))):

#    FreqOneList = [];

#    for i in range(0,64,1):

#        FreqOneList.append(FinalSet_List[i][freqlist]-FinalSet_List[0][freqlist]);
      
#    FreqOneList = np.deg2rad(FreqOneList);
#    FreqOneList = np.unwrap(FreqOneList);
#    FreqOneList = np.rad2deg(FreqOneList);
#    Final_List_Phases.append(FreqOneList)
 

#SuperFinal = [];
#TempFreqs = [];
#for freq_range in range(len(np.arange(5,15,0.1))):
#    for states_unwrap in range(0,64,1):
#        TempFreqs.append(Final_List_Phases[freq_range][states_unwrap]);

#    SuperFinal.append(TempFreqs);
#    TempFreqs = [];




#LastChance = [];
#Tempo = [];

#for j in range(0,64,1):
#    for i in range(len(np.arange(5,15,0.1))):
#        Tempo.append(SuperFinal[i][j]);
#    LastChance.append(Tempo);
#    Tempo = [];




#x = np.arange(5,15,0.1);

#for i in range(0,64,1):
#    plt.plot(x,LastChance[i]);

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.xlim(5,15);
#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0,360, 11.25))

#plt.xlabel('Частота, ГГц')
#plt.ylabel('Фаза сигнала, °')
#plt.show();
################################################



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


#System = GetSystemRandom();
#T = 100000;
#k = 0;

#while System.FitnessValue>0.5127403484025012:
#    #System=System;
#    #time.sleep(0.1);
#    a = 0.9999
#    TempSystem = Mutation(System,3);
#    T = a*T;
#    deltaFitness = 1e15*TempSystem.FitnessValue-1e15*System.FitnessValue;

#    if deltaFitness<0:

#        System = TempSystem;
#        k=k+1;

         
#    elif deltaFitness>=0:

#        p = np.exp(-(deltaFitness/T))
#        NewK_p = np.round(p*100);
#        OldK_p = np.round((1-p)*100);
#        God = random.randint(0,100);

#        if God>OldK_p:
#            System = TempSystem
#            k=k+1;
#        if God<OldK_p:
#            System=System;
#            k=k+1;

#    print('Итерация номер '+str(k));
#    print('Tempература '+str(T));
#    print('Фитнесс = '+str(System.FitnessValue));


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







