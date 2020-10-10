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




## Options ы
## Start GA;
##Set frequency in GHz

#ListOfStates = [];
#for State_Number in range(0,64,1):
#    for BitA in range(0,8,1):
#        for BitB in range(0,8,1):
#            ListOfStates.append(getStateForGA(State_Number, BitA, BitB));


            
#DegreeList = [];
#S21List = [];

#for i in range(0,4096,1):
#    DegreeList.append(ListOfStates[i].StatePhase);
#    S21List.append(ListOfStates[i].StateS21);



#rho =  S21List;
#theta =  DegreeList;

#RHO = [];
#Theta = [];

#for i in range(0,4096,1):
#    Theta.append((theta[i]*(np.pi/180)));
#    RHO.append(10**(rho[i]/20));



#plt.polar(Theta,  RHO, 'k*', markersize = 1, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Optimized for 10 GHz');


#plt.ylim(1,1.5);
##plt.xlim(0,np.pi/4);
#plt.yticks(np.arange(1,1.5,0.5))

#plt.grid(True);

#plt.legend(loc=3);


#plt.show();
################################################################



#print('isho');








#FinalSolution, IterationList, FitnessList = GeneticAlgorithm(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);
#DataResult = GetFinalSystem(FinalSolution); 

#ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz_Test.txt', 'w')
#ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
#ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
#ConfigStateFile.write(DataResult.StateSystemName);
#ConfigStateFile.close;

#FullDataSet = CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult);
#pickle.dump(FullDataSet, open('FullDataSet_'+str(ConfigModule.frequency)+'GHz_Test.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);





############## СКО ФАЗА человек и нет общее########################################
#ViewResult =  pickle.load(open('FullDataSet_10GHz_PhaseOnly.pkl', 'rb'));
#ViewResultHuman =  pickle.load(open('FullDataSet_10GHz_Human.pkl', 'rb'));
#ViewResultSuperBad = pickle.load(open('FullDataSet_10GHz_SuperBadHuman.pkl', 'rb'));


#print('загрузил?!!!!');

#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_Phase_List
#y2 = ViewResultHuman.Final_RMS_Phase_List;
#y3 = ViewResultSuperBad.Final_RMS_Phase_List;


#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'}


#plt.ylabel('СКО фаза, °',**csfont);  # Подписи у
#plt.xlabel('Частота, ГГц',**csfont);  # Подписи х

#plt.xlim(5,               15     );  
#plt.ylim(0.25,               4 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0.25,4,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='ГА' ,markevery=5);
#plt.plot(x,y2, 'gP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='Ручной подбор',markevery=5);
#plt.plot(x,y3, 'bs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w', label ='Неоптимизированный' ,markevery=5);

#plt.legend(loc=0);
#plt.show()
########################################################

















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



############## СКО ФАЗА ВСЕ общее########################################

#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult85 = pickle.load(open('FullDataSet_8.5GHz.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz.pkl', 'rb'));
#ViewResult95 = pickle.load(open('FullDataSet_9.5GHz.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#ViewResult105 = pickle.load(open('FullDataSet_10.5GHz.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz.pkl', 'rb'));
#ViewResult115 = pickle.load(open('FullDataSet_11.5GHz.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz.pkl', 'rb'));

#ViewResultSuperBad = pickle.load(open('FullDataSet_10GHz_SuperBadHuman.pkl', 'rb'));


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
#y10 = ViewResultSuperBad.Final_RMS_Phase_List


#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'};

#plt.ylabel('СКО фаза, °',**csfont);  # Подписи у
#plt.xlabel('Частота, ГГц', **csfont);  # Подписи х

#plt.xlim(5,               15     );  
#plt.ylim(0.25,               4.5 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0.25,4.5,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='8 ГГц' ,markevery=5);
#plt.plot(x,y2, 'gP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='8.5 ГГц',markevery=5);
#plt.plot(x,y3, 'bs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w', label ='9 ГГц' ,markevery=5);
#plt.plot(x,y4, 'kd-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='9.5 ГГц',markevery=5);
#plt.plot(x,y5, 'yh-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'g', label ='10 ГГц' ,markevery=5);
#plt.plot(x,y6, 'cP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r',label ='10.5 ГГц',markevery=5);
#plt.plot(x,y7, 'rv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='11 ГГц' ,markevery=5);
#plt.plot(x,y8, 'k.-.', markersize = 9, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='11.5 ГГц',markevery=5);
#plt.plot(x,y9, 'r*-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='12 ГГц' ,markevery=5);
#plt.plot(x,y10,'kX-', markersize = 8, linewidth = 2.5, markeredgewidth = 1, markerFacecolor = 'r', label ='Неоптимизированно' ,markevery=5);


#plt.legend(loc=0);
#plt.show();

##########################################################

############ СКО S21 ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_PhaseOnly.pkl', 'rb'));
#ViewResult85 = pickle.load(open('FullDataSet_8.5GHz.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz.pkl', 'rb'));
#ViewResult95 = pickle.load(open('FullDataSet_9.5GHz.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
#ViewResult105 = pickle.load(open('FullDataSet_10.5GHz.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz.pkl', 'rb'));
#ViewResult115 = pickle.load(open('FullDataSet_11.5GHz.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz.pkl', 'rb'));


#ViewResultSuperBad = pickle.load(open('FullDataSet_10GHz_SuperBadHuman.pkl', 'rb'));



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
#y10 = ViewResultSuperBad.Final_RMS_S21_List;

#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'};


#plt.xlabel('Частота, ГГц', **csfont);  # Подписи х

#plt.ylabel('СКО |S21|, дБ',**csfont);  # Подписи у


#plt.xlim(5,               15     );  
#plt.ylim(0.1,               0.75);  

#plt.xticks(np.arange(5,15.5,1));
#plt.yticks(np.arange(0.1,0.75,0.1));

#plt.grid(color='k', linestyle='--', linewidth=0.3)


##plt.plot(x,y1, 'ro-', color = 'black', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='8 ГГц' ,markevery=5);
##plt.plot(x,y2, 'gP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='8.5 ГГц',markevery=5);
##plt.plot(x,y3, 'bs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w', label ='9 ГГц' ,markevery=5);
##plt.plot(x,y4, 'kd-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='9.5 ГГц',markevery=5);
##plt.plot(x,y5, 'yh-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'g', label ='10 ГГц' ,markevery=5);
##plt.plot(x,y6, 'cP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r',label ='10.5 ГГц',markevery=5);
##plt.plot(x,y7, 'rv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='11 ГГц' ,markevery=5);
##plt.plot(x,y8, 'k.-.', markersize = 9, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='11.5 ГГц',markevery=5);
##plt.plot(x,y9, 'r*-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='12 ГГц' ,markevery=5);

#plt.plot(x,y1, 'o-',  color = 'grey', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='8 ГГц' ,markevery=5);
#plt.plot(x,y2, 'gP-',  color = 'dimgray',  markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='8.5 ГГц',markevery=5);
#plt.plot(x,y3, 'bs-',  color = 'crimson', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w', label ='9 ГГц' ,markevery=5);
#plt.plot(x,y4, 'd-',  color = 'indigo', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='9.5 ГГц',markevery=5);
#plt.plot(x,y5, 'h-',  color = 'y', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'g', label ='10 ГГц' ,markevery=5);
#plt.plot(x,y6, 'P-',  color = 'fuchsia', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w',label ='10.5 ГГц',markevery=5);
#plt.plot(x,y7, 'v-',  color = 'navy', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='11 ГГц' ,markevery=5);
#plt.plot(x,y8, '.-.',  color = 'grey', markersize = 9, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='11.5 ГГц',markevery=5);
#plt.plot(x,y9, 'h-.',  color = 'firebrick', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='12 ГГц' ,markevery=5);
#plt.plot(x,y10,'kX-', markersize = 8, linewidth = 2.5, markeredgewidth = 1, markerFacecolor = 'r', label ='Неоптимизированно' ,markevery=5);




#plt.legend(loc=0);
#plt.show()
#########################################################


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



#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'}

#plt.ylabel('Фитнесс-функция',**csfont);  # Подписи у
#plt.xlabel('Итерации', **csfont);  # Подписи х

#plt.ylabel('Фитнесс-функция');  # Подписи у
#plt.xlabel('Итерации');  # Подписи х

#plt.xlim(0,               4096     );  
#plt.ylim(0.4,              1.2 );  

#plt.xscale("linear");

#plt.xticks(np.arange(0,4096,500))
#plt.yticks(np.arange(0.4,1.2,0.05))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'o-',  color = 'grey', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='8 ГГц' ,markevery=250);
#plt.plot(x,y2, 'gP-',  color = 'orange',  markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='8.5 ГГц',markevery=250);
#plt.plot(x,y3, 'bs-',  color = 'crimson', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w', label ='9 ГГц' ,markevery=250);
#plt.plot(x,y4, 'd-',  color = 'indigo', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='9.5 ГГц',markevery=250);
#plt.plot(x,y5, 'h-',  color = 'y', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'g', label ='10 ГГц' ,markevery=250);
#plt.plot(x,y6, 'P-',  color = 'c', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r',label ='10.5 ГГц',markevery=250);
#plt.plot(x,y7, 'v-',  color = 'navy', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='11 ГГц' ,markevery=250);
#plt.plot(x,y8, '.-.',  color = 'grey', markersize = 9, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='11.5 ГГц',markevery=250);
#plt.plot(x,y9, '*-',  color = 'purple', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='12 ГГц' ,markevery=250);

##plt.plot(x,y1, 'rм.', markersize = 2, markerFacecolor = 'k', label ='8 GHz');
##plt.plot(x,y2, 'g.-', markersize = 2,  markerFacecolor = 'y',label ='8.5 GHz');
##plt.plot(x,y3, 'b.--', markersize = 2,  markerFacecolor = 'w',label ='9 GHz');
##plt.plot(x,y4, 'k.-', markersize = 2,  markerFacecolor = 'k',label ='9.5 GHz');
##plt.plot(x,y5, 'm.-.', markersize = 2, markerFacecolor = 'k', label ='10 GHz');
##plt.plot(x,y6, 'y-.', markersize = 2,  markerFacecolor = 'g',label ='10.5 GHz');
##plt.plot(x,y7, 'c-.', markersize = 2,  markerFacecolor = 'k',label ='11 GHz');
##plt.plot(x,y8, 'k--', markersize = 2,  markerFacecolor = 'y',label ='11.5 GHz');
##plt.plot(x,y9, 'k.-.', markersize = 2,  markerFacecolor = 'w',label ='12 GHz');

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


#SMALL_SIZE = 12
#MEDIUM_SIZE = 16
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'}

#plt.ylabel('Фитнесс-функция',**csfont);  # Подписи у
#plt.xlabel('Итерации', **csfont);  # Подписи х


#plt.xlim(0,               4096     );  
#plt.ylim(0,              2 );  

#plt.xticks(np.arange(0,4096,500))
#plt.yticks(np.arange(0,2,0.2))

#plt.grid(color='k', linestyle='--', linewidth=0.3)


#plt.plot(x,y1, 'rv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Мутация 3 %' ,markevery=500);
#plt.plot(x,y2, 'gP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='Мутация 30 %',markevery=500);

#plt.legend(loc=0);

#plt.show();
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


#SMALL_SIZE = 12
#MEDIUM_SIZE = 16
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'}

#plt.ylabel('Фитнесс-функция',**csfont);  # Подписи у
#plt.xlabel('Итерации', **csfont);  # Подписи х

#plt.xlim(0,               350    );  
#plt.ylim(0.4,              1.9 );  

#plt.xticks(np.arange(0,350,50))
#plt.yticks(np.arange(0.4,1.9,0.1))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'rs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Панмиксия' ,markevery=25);
#plt.plot(x,y2, 'g8-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w',label ='Аутбридинг',markevery=25 );
#plt.plot(x,y3, 'bv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y', label ='Инбридинг',markevery=25);
#plt.plot(x,y4, 'kP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r',label ='Всё операторы',markevery=25);

#plt.legend(loc=0, prop={"family":"Times New Roman"});



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



#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'}


#plt.ylabel('RMS Phase Error, °',**csfont);  # Подписи у
#plt.xlabel('Frequency, GHz',**csfont);  # Подписи х

#plt.xlim(5,               15.5     );  
#plt.ylim(0.25,               5 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0.25,5,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'ro-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='8 GHz' ,markevery=5);
#plt.plot(x,y2, 'gP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='8.5 GHz',markevery=5);
#plt.plot(x,y3, 'bs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'w', label ='9 GHz' ,markevery=5);
#plt.plot(x,y4, 'kd-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='9.5 GHz',markevery=5);
#plt.plot(x,y5, 'yh-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'g', label ='10 GHz' ,markevery=5);
#plt.plot(x,y6, 'cP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'r',label ='10.5 GHz',markevery=5);
#plt.plot(x,y7, 'rv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='11 GHz' ,markevery=5);
#plt.plot(x,y8, 'k.-.', markersize = 9, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'y',label ='11.5 GHz',markevery=5);
#plt.plot(x,y9, 'r*-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='12 GHz' ,markevery=5);

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


#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#csfont = {'fontname':'Times New Roman'}


#plt.ylabel('RMS Phase Error, °',**csfont);  # Подписи у
#plt.xlabel('Frequency, GHz',**csfont);  # Подписи х

#plt.xlim(5,               15     );  
#plt.ylim(0.25,               4 );  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0.25,4,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'rd-', markersize = 7, markerFacecolor = 'k', label ='10 GHz GA',markevery=5);
#plt.plot(x,y2, 'kP-.', markersize = 7,  markerFacecolor = 'w',label ='10 GHz Human',markevery=5);


#plt.legend(loc=0);
#plt.show()
##########################################################




###################Круговая градусы
#ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));

#first_real = -113.27;


#rho =  ViewResult10.Final_S21_List;
#theta =  ViewResult10.Final_Phase_List;

#theta = np.ndarray.tolist(theta);

#RHO = [];
#Theta = [];

#for i in range(0,64,1):
#    #Theta.append(theta[i]+first_real);
#    RHO.append(10**(rho[i]/20))



#RHO = RHO;
#Theta = theta;



##X = [];
##Y = [];

##for i in range (0,64,1):
##    X.append(math.cos(Theta[i])*RHO[i])
##    Y.append(math.sin(Theta[i])*RHO[i])


##Z = [];

##for i in range(0,64,1):
##    Z.append(complex(X[i],Y[i]))

##Z =  np.array(Z);


##plt.polar(Z,'o');
##plt.show;




#NewTheta = [];
#New_R21 = [];

#for i in range(len(Theta)):
#    NewTheta.append(Theta[i]*(np.pi/180)- (0*(np.pi/180)))

#for j in range(len(RHO)):
#    New_R21.append(RHO[j])
#    #New_R21.append(R_S21[j])

#Type_RS21 = type(New_R21);
#Type_Theta = type(NewTheta);

#plt.polar(NewTheta,  New_R21, 'rh', markersize = 6, linewidth = 1, markeredgewidth = 1.25, markerFacecolor = 'r', label ='Оптимизация с ГА, 10 ГГц');


#ViewResult10_bad = pickle.load(open('FullDataSet_10GHz_BadHuman.pkl', 'rb'));


#R_S21_bad =  ViewResult10_bad.Final_S21_List;
#theta_bad =  ViewResult10_bad.Final_Phase_List;

#theta_bad = np.ndarray.tolist(theta_bad);
#NewTheta_bad = [];
#New_R21_Bad = [];

#for i in range(len(theta_bad)):
#    NewTheta_bad.append(theta_bad[i]*(np.pi/180))

#for j in range(len(R_S21_bad)):
#    New_R21_Bad.append(10**(R_S21[j]/20))


#plt.polar(NewTheta_bad,  New_R21_Bad, 'bP', markersize = 3, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Not Optimized');


#IdealTheta = [];
#Ideal_R21 = []; 

#NormalPhaseList = [];

#for state in range(0,64,1):
#    Phase = state*5.625;
#    NormalPhaseList.append(Phase);


#for i in range(len(NormalPhaseList)):
#    IdealTheta.append(NormalPhaseList[i]*(np.pi/180))

#Mean_s21  = statistics.mean(New_R21)

#for j in range(0,64,1):
#    Ideal_R21.append(Mean_s21);



#plt.polar(IdealTheta,  Ideal_R21, 'kP', markersize = 4.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='Идеальный шаг 5,625, усиление 1,75 дБ');

##for d in range (0,64,1):
#   # plt.arrow(0, 0, NewTheta[d], New_R21[d], alpha = 0.5, width = 0.01, edgecolor = 'black', facecolor = 'k', lw = 0.5, zorder = 1)



#plt.ylim(0,1.5)

#plt.yticks(np.arange(0,1.5,0.5))

#plt.grid(True);

#plt.legend(loc=3);


#plt.show();
#################################################################



##################### Градусы по состояниям #####################
ViewResult10 = pickle.load(open('FullDataSet_10GHz.pkl', 'rb'));
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
    for allfreqlist in np.arange(2,20,0.1):
        print('я работаю, подожди  '+str(allstates));
        PhaseListFreq.append(getPhaseFreq(allstates,ViewResult10.Final_StateList[allstates].StateBitA,ViewResult10.Final_StateList[allstates].StateBitB,allfreqlist))

 
    FinalSet_List.append(PhaseListFreq);
    PhaseListFreq=[];



FirstStatePhaseList = [];

for i in range(len(np.arange(2,20,0.1))):
    FirstStatePhaseList.append(FinalSet_List[0][i]);

for freq_range in range(len(np.arange(2,20,0.1))):
    for states_unwrap in range(0,64,1):
        FinalSet_List[states_unwrap][freq_range] = FinalSet_List[states_unwrap][freq_range]-FirstStatePhaseList[freq_range];


Final_List_Phases = [];

for freqlist in range(len(np.arange(2,20,0.1))):

    FreqOneList = [];

    for i in range(0,64,1):

        FreqOneList.append(FinalSet_List[i][freqlist]-FinalSet_List[0][freqlist]);
      
    FreqOneList = np.deg2rad(FreqOneList);
    FreqOneList = np.unwrap(FreqOneList);
    FreqOneList = np.rad2deg(FreqOneList);
    Final_List_Phases.append(FreqOneList)
 

SuperFinal = [];
TempFreqs = [];
for freq_range in range(len(np.arange(2,20,0.1))):
    for states_unwrap in range(0,64,1):
        TempFreqs.append(Final_List_Phases[freq_range][states_unwrap]);

    SuperFinal.append(TempFreqs);
    TempFreqs = [];


LastChance = [];
Tempo = [];

for j in range(0,64,1):
    for i in range(len(np.arange(2,20,0.1))):
        Tempo.append(SuperFinal[i][j]);
    LastChance.append(Tempo);
    Tempo = [];


SMALL_SIZE = 15
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

csfont = {'fontname':'Times New Roman'}


x = np.arange(2,20,0.1);

for i in range(0,64,1):
    plt.plot(x,LastChance[i]);

plt.grid(color='k', linestyle='--', linewidth=0.3)

plt.xlim(2,20);
plt.ylim(0,370);


SMALL_SIZE = 18
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

csfont = {'fontname':'Times New Roman'}




plt.xticks(np.arange(2,20,1))
plt.yticks(np.arange(0,370, 45))

plt.xlabel('Частота, ГГц',**csfont); 
plt.ylabel('Значение фазы по состояниям, °',**csfont);



plt.show();
###############################################



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







