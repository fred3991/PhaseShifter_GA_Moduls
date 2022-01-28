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
from GeneticTimeGoal import GeneticTimeGoal

from RMSPhaseForFreq import RMSPhaseForFreq
from RMSS21ForFreq import RMSS21ForFreq
from Calc_RMS_List_Phase import Calc_RMS_List_Phase
from Calc_RMS_List_S21 import Calc_RMS_List_S21

from FinalSystemData import FinalSystemData

from GetFinalSystem import GetFinalSystem
from DrawFunction import DrawFunction




# Options ы
# Start GA;
#Set frequency in GHz

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



#plt.polar(Theta,  RHO, 'k*', markersize = 1, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='Optimized for 10 GHz');


#plt.ylim(1,1.5);
##plt.xlim(0,np.pi/4);
#plt.yticks(np.arange(1,1.5,0.5))

#plt.grid(True);

#plt.legend(loc=3);


#plt.show();
###############################################################



#print('isho');


#start_time = time.time()
#FinalSolution, IterationList, FitnessList = GeneticAlgorithm(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);
#full_time = time.time() - start_time;
#print("--- %s seconds ---" % (time.time() - start_time))

#DataResult = GetFinalSystem(FinalSolution); 

#ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz_Human_Paper.txt', 'w')
#ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
#ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
#ConfigStateFile.write(DataResult.StateSystemName);
#ConfigStateFile.close;

#FullDataSet = CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult);
#pickle.dump(FullDataSet, open('FullDataSet_'+str(ConfigModule.frequency)+'GHz_Human_Paper.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);
#print("--- %s seconds ---" % (time.time() - start_time));



############################################
#############################################
#start_time = time.time()
#FinalSolution, IterationList, FitnessList = GeneticTimeGoal(ConfigModule.PopulSize, ConfigModule.FitnessGoal, ConfigModule.MutationCoefficient, ConfigModule.Iterations);
#full_time = time.time() - start_time;
#print("--- %s seconds ---" % (time.time() - start_time))

#DataResult = GetFinalSystem(FinalSolution); 

#ConfigStateFile = open('ConfigStateFile_'+str(ConfigModule.frequency)+'GHz_TimeTest_1.txt', 'w')
#ConfigStateFile.write('RMS Phase error '+str(FinalSolution.RMS_Phase)+'\n');
#ConfigStateFile.write('RMS S21 error '+str(FinalSolution.RMS_S21)+'\n');
#ConfigStateFile.write(DataResult.StateSystemName);
#ConfigStateFile.close;

#FullDataSet = CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult);
#pickle.dump(FullDataSet, open('FullDataSet_'+str(ConfigModule.frequency)+'GHz_TimeTest_1.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);
#print("--- %s seconds ---" % (time.time() - start_time))

############################################
############################################
#10 GHz
#1 - 222,91
#2 - 204.97
#3 - 204.74
#4 - 184.16
#5 - 203.91

#8 GHz
#1 - 452.033
#2 - 416-   8_GHz_TimeTest_1-1
#3 - 612.19
#4 - 602.304
#5 - 872.56

#12 GHz
#1 - 706,74
#2 - 1113.154
#3 - 756,44
#4 - 602,86
#5 - 1157,




#def cm2inch(*tupl):
#    inch = 2.54
#    if isinstance(tupl[0], tuple):
#        return tuple(i/inch for i in tupl[0])
#    else:
#        return tuple(i/inch for i in tupl)
###########
############# СКО ФАЗА человек и нет общее########################################
###################################################################################
###################################################################################
#ViewResult =  pickle.load(open('FullDataSet_10GHz_ALL_New.pkl', 'rb'));
#ViewResultHuman =  pickle.load(open('FullDataSet_10GHz_Human_Paper.pkl', 'rb'));
#ViewResultSuperBad = pickle.load(open('FullDataSet_10GHz_SuperBadHuman.pkl', 'rb'));
##print('загрузил?!!!!');


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


#t =  ViewResult.Final_List_Frequencies;
#y_1_1 = ViewResult.Final_RMS_Phase_List;
#y_1_2 = ViewResult.Final_RMS_S21_List;
#y_2_1 = ViewResultHuman.Final_RMS_Phase_List;
#y_2_2 = ViewResultHuman.Final_RMS_S21_List;
#y_3_1 = ViewResultSuperBad.Final_RMS_Phase_List;
#y_3_2 = ViewResultSuperBad.Final_RMS_S21_List;



#fig, ax1 = plt.subplots()
#ax1.set_xlabel('Frequency, GHz',**csfont);
#ax1.set_ylabel('RMS Phase Error (deg)°',**csfont)


#ax1.plot(t,y_1_1, 'ro-', markersize = 6, linewidth = 1.5, markeredgewidth = 1, mfc = 'k',  label ='GA - RMS Phase Error' ,markevery=5);
#ax1.plot(t,y_2_1, 'r:P', markersize = 6, linewidth = 1.5, markeredgewidth = 1, mfc = 'r',  label ='Manual - RMS Phase Error' ,markevery=5);
#ax1.plot(t,y_3_1, 'r.-.', markersize = 6, linewidth = 1, markeredgewidth = 1, mfc = 'b',  label ='Not optimized - RMS Phase Error' ,markevery=5);

#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#ax2.set_ylabel('RMS Gain Error (dB)',**csfont)  # we already handled the x-label with ax1

#ax2.plot(t,y_1_2, 'bo-', markersize = 6, linewidth = 1.5, markeredgewidth = 1, mfc = 'k', label ='GA - RMS Gain Error',markevery=5);
#ax2.plot(t,y_2_2, 'b:P', markersize = 6, linewidth = 1, markeredgewidth = 1, mfc = 'r',  label ='Manual - RMS Gain Error' ,markevery=5);
#ax2.plot(t,y_3_2,'b.-.', markersize = 6, linewidth = 1, markeredgewidth = 1, mfc = 'b', label ='Not optimized - RMS Gain Error' ,markevery=5);

#ax1.set_xlim(5,15);
#ax1.set_ylim(0.25,4);
#ax2.set_ylim(0.15,0.85);
##ax2.set_xlim(5,15);
#ax1.set_xticks(np.arange(5,15.5,1));
##ax2.set_yticks(np.arange(0.0,2.05,0.05))
#ax1.grid(color='k', linestyle='--', linewidth=0.3)
##fig.tight_layout()  # otherwise the right y-label is slightly clipped
##plt.grid(color='k', linestyle='--', linewidth=0.3)

#fig = plt.gcf();
#fig.set_dpi(300.0) 
#fig.set_size_inches(9, 9)


#ax1.legend(loc=0)
##ax2.legend(loc=2)
##plt.show()

#plt.savefig("ManualVsGa3.tiff", dpi=300, format="tiff", bbox_inches=0, pad_inches=0)

#######################################################
#######################################################
#######################################################
#######################################################




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

#plt.plot(x,y1, 'ro-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='8 ГГц' ,markevery=5);
#plt.plot(x,y2, 'gP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'y',label ='8.5 ГГц',markevery=5);
#plt.plot(x,y3, 'bs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'w', label ='9 ГГц' ,markevery=5);
#plt.plot(x,y4, 'kd-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'y',label ='9.5 ГГц',markevery=5);
#plt.plot(x,y5, 'yh-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'g', label ='10 ГГц' ,markevery=5);
#plt.plot(x,y6, 'cP-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'r',label ='10.5 ГГц',markevery=5);
#plt.plot(x,y7, 'rv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='11 ГГц' ,markevery=5);
#plt.plot(x,y8, 'k.-.', markersize = 9, linewidth = 1, markeredgewidth = 1, mfc = 'y',label ='11.5 ГГц',markevery=5);
#plt.plot(x,y9, 'r*-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='12 ГГц' ,markevery=5);
#plt.plot(x,y10,'kX-', markersize = 8, linewidth = 2.5, markeredgewidth = 1, mfc = 'r', label ='Неоптимизированно' ,markevery=5);


#plt.legend(loc=0);
#plt.show();

##########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
##########################################################
##########################################################
############ СКО S21 ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_ALL_New.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz_ALL_New.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz_ALL_New.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz_ALL_New.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz_ALL_New.pkl', 'rb'));

#ViewResultSuperBad = pickle.load(open('FullDataSet_10GHz_SuperBadHuman.pkl', 'rb'));
#print('загрузил?!!!!');
#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_S21_List
#y3 = ViewResult9.Final_RMS_S21_List;
#y5 = ViewResult10.Final_RMS_S21_List;
#y7 = ViewResult11.Final_RMS_S21_List;
#y9 = ViewResult12.Final_RMS_S21_List;


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

#fig = plt.gcf();
#fig.set_size_inches(6, 6)


#plt.xlabel('Frequency (GHz)', **csfont);  # Подписи х
#plt.ylabel('RMS Amplitude Error (dB)',**csfont);  # Подписи у

#plt.xlim(5,               15     );  
#plt.ylim(0.1,               0.75);  

#plt.xticks(np.arange(5,15.5,1));
#plt.yticks(np.arange(0.1,0.75,0.1));

#plt.grid(color='k', linestyle='--', linewidth=0.3)


#plt.plot(x,y1, 'ro-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='8 GHz' ,markevery=5);
#plt.plot(x,y3, 'bs-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'g', label ='9 GHz' ,markevery=5);
#plt.plot(x,y5, 'yh-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'b', label ='10 GHz' ,markevery=5);
#plt.plot(x,y7, 'rv-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='11 GHz' ,markevery=5);
#plt.plot(x,y9, 'k*-', markersize = 6.5, linewidth = 1, markeredgewidth = 1, markerFacecolor = 'k', label ='12 GHz' ,markevery=5);

#fig = plt.gcf();
#fig.set_size_inches(6, 6)

#plt.legend(loc=0);
#plt.show()
##########################################################
##########################################################
##########################################################
##########################################################



#########################################################
#########################################################
#########################################################
#########################################################
###################################################################################################################
##########################################################
############### ГА Анализ Итерации - фитнес ВСЕ общее########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_ALL_New.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz_ALL_New.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz_ALL_New.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz_ALL_New.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz_ALL_New.pkl', 'rb'));
               
#print('загрузил?!!!!');
#x = ViewResult.Final_Iteration_List;
#y1 = ViewResult.Final_Fitness_List
#y3 = ViewResult9.Final_Fitness_List;
#y5 = ViewResult10.Final_Fitness_List;
#y7 = ViewResult11.Final_Fitness_List;
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

#plt.ylabel('Fitness-function value',**csfont);  # Подписи у
#plt.xlabel('Iterations', **csfont);  # Подписи х

#plt.xlim(0,              1001     );  
#plt.ylim(0.4,              1.2 );  

#plt.xscale("linear");

#plt.xticks(np.arange(0,1001,250))
#plt.yticks(np.arange(0.4,1.2,0.1))

#plt.grid(color='k', linestyle='--', linewidth=0.3)
#plt.plot(x,y1, 'o-.',  color = 'grey', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'r', label ='8 GHz' ,markevery=50);
#plt.plot(x,y3, 'bs-.',  color = 'crimson', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'b', label ='9 GHz' ,markevery=50);
#plt.plot(x,y5, 'h-.',  color = 'y', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'y', label ='10 GHz' ,markevery=50);
#plt.plot(x,y7, 'v-.',  color = 'navy', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'g', label ='11 GHz' ,markevery=50);
#plt.plot(x,y9, '*-',  color = 'purple', markersize = 6.5, linewidth = 1, markeredgewidth = 1, mfc = 'w', label ='12 GHz' ,markevery=50);


#fig = plt.gcf();
#fig.set_dpi(300.0) 
#fig.set_size_inches(9, 9)


#plt.legend(loc=0)
##plt.show()

#plt.savefig("Plot2.tiff", dpi=300, format="tiff", bbox_inches=0, pad_inches=0)

##########################################################
##########################################################
##########################################################
##########################################################
##########################################################



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


#fig = plt.gcf();
#fig.set_size_inches(6, 6)

#csfont = {'fontname':'Times New Roman'}

#plt.ylabel('Fitness-function value',**csfont);  # Подписи у
#plt.xlabel('Iterations', **csfont);  # Подписи х

#plt.xlim(0,               351    );  
#plt.ylim(0.4,              1.9 );  

#plt.xticks(np.arange(0,351,50))
#plt.yticks(np.arange(0.4,1.9,0.1))

#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.plot(x,y1, 'rs-', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='Panmixis' ,markevery=25);
#plt.plot(x,y2, 'g8-.', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'w',label ='Outbreeding',markevery=25 );
#plt.plot(x,y3, 'bv-', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'y', label ='Inbreeding',markevery=25);
#plt.plot(x,y4, 'kP-.', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'r',label ='All operators',markevery=25);
##
##plt.yscale("log");

#plt.legend(loc=0, prop={"family":"Times New Roman"});

#fig = plt.gcf();
#fig.set_dpi(300.0) 
#fig.set_size_inches(9, 9)


#plt.legend(loc=0)
##plt.show()

#plt.savefig("Operators.tiff", dpi=300, format="tiff", bbox_inches=0, pad_inches=0)
############################################################
#############################################################


#8 GHz
#1 - 452.033
#2 - 416-   8_GHz_TimeTest_1-1
#3 - 612.19
#4 - 602.304
#5 - 872.56

#TimeTest1 = pickle.load(open('FullDataSet_8GHz_TimeTest_1.pkl', 'rb'));
#L1 = len(TimeTest1.Final_Iteration_List)
#TimeTest2 = pickle.load(open('FullDataSet_8GHz_TimeTest_2.pkl', 'rb'));
#TimeTest3 = pickle.load(open('FullDataSet_8GHz_TimeTest_3.pkl', 'rb'));
#TimeTest4 = pickle.load(open('FullDataSet_8GHz_TimeTest_4.pkl', 'rb'));
#TimeTest5 = pickle.load(open('FullDataSet_8GHz_TimeTest_5.pkl', 'rb'));

#L1 = len(TimeTest1.Final_Iteration_List)
#L2 = len(TimeTest2.Final_Iteration_List)
#L3 = len(TimeTest3.Final_Iteration_List)
#L4 = len(TimeTest4.Final_Iteration_List)
#L5 = len(TimeTest5.Final_Iteration_List)
#print('шо')




############## СКО ФАЗА Только фаза########################################
#ViewResult = pickle.load(open('FullDataSet_8GHz_ALL_New.pkl', 'rb'));
#ViewResult9 = pickle.load(open('FullDataSet_9GHz_ALL_New.pkl', 'rb'));
#ViewResult10 = pickle.load(open('FullDataSet_10GHz_ALL_New.pkl', 'rb'));
#ViewResult11 = pickle.load(open('FullDataSet_11GHz_ALL_New.pkl', 'rb'));
#ViewResult12 = pickle.load(open('FullDataSet_12GHz_ALL_New.pkl', 'rb'));


#print('загрузил?!!!!');
#x = ViewResult.Final_List_Frequencies;
#y1 = ViewResult.Final_RMS_Phase_List
#y3 = ViewResult9.Final_RMS_Phase_List;
#y5 = ViewResult10.Final_RMS_Phase_List;
#y7 = ViewResult11.Final_RMS_Phase_List;
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



#csfont = {'fontname':'Times New Roman'}


#plt.ylabel('RMS Phase Error (deg)',**csfont);  # Подписи у
#plt.xlabel('Frequency (GHz)',**csfont);  # Подписи х

#plt.xlim(5,               15.5     );  
#plt.ylim(0.0,               5);  

#plt.xticks(np.arange(5,15.5,1))
#plt.yticks(np.arange(0,5.01,0.25))

#plt.grid(color='k', linestyle='--', linewidth=0.3)
#plt.plot(x,y1, 'ro--', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'g', label ='8 GHz' ,markevery=5);
#plt.plot(x,y3, 'bs-.', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'r', label ='9 GHz' ,markevery=5);
#plt.plot(x,y5, 'rh--', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'b', label ='10 GHz' ,markevery=5);
#plt.plot(x,y7, 'gd-', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'y', label ='11 GHz' ,markevery=5);
#plt.plot(x,y9, 'k*-', markersize = 6.1, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='12 GHz' ,markevery=5);


#fig = plt.gcf();
#fig.set_dpi(300.0) 
#fig.set_size_inches(9, 9)


#plt.legend(loc=0)
##plt.show()

#plt.savefig("PhaseRMS.tiff", dpi=300, format="tiff", bbox_inches=0, pad_inches=0)
###########################################################





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








############################################
###########################################
#################Круговая градусы############
#############################################
ViewResult10 = pickle.load(open('FullDataSet_10GHz_ALL_New.pkl', 'rb'));
rho =  ViewResult10.Final_S21_List;
theta =  ViewResult10.Final_Phase_List;

theta = np.ndarray.tolist(theta);
RHO = [];
Theta = [];

for i in range(0,64,1):
    Theta.append(theta[i]);
    RHO.append(10**(rho[i]/20))

RHO = RHO;
Theta = theta;

X = [];
Y = [];

for i in range (0,64,1):
    X.append(math.cos(Theta[i])*RHO[i])
    Y.append(math.sin(Theta[i])*RHO[i])

Z = [];

for i in range(0,64,1):
    Z.append(complex(X[i],Y[i]))


Z =  np.array(Z);


plt.polar(Z,'w.', markersize = 0.01, linewidth =0.01, markeredgewidth = 0.01, mfc = 'w');
#plt.show;


SMALL_SIZE = 15
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

csfont = {'fontname':'Times New Roman'}

#csfont = {'fontname':'Times New Roman'}
#plt.ylabel('RMS Phase Error, °',**csfont);  # Подписи у
#plt.xlabel('Frequency, GHz',**csfont);  # Подписи х

NewTheta = [];
New_R21 = [];

R_S21 =  ViewResult10.Final_S21_List;

for i in range(len(Theta)):
    NewTheta.append(Theta[i]*(np.pi/180)- (0*(np.pi/180)))

for j in range(len(RHO)):
    New_R21.append(RHO[j])
    #New_R21.append(R_S21[j])

Type_RS21 = type(New_R21);
Type_Theta = type(NewTheta);

plt.polar(NewTheta,  New_R21, 'rp', markersize = 8, linewidth = 1, markeredgewidth = 1.25, mfc = 'r', label ='GA Optimization, 10 GHz');

#ViewResult10_bad = pickle.load(open('FullDataSet_10GHz_BadHuman.pkl', 'rb'));
#R_S21_bad =  ViewResult10_bad.Final_S21_List;
#theta_bad =  ViewResult10_bad.Final_Phase_List;

#theta_bad = np.ndarray.tolist(theta_bad);
#NewTheta_bad = [];
#New_R21_Bad = [];

#for i in range(len(theta_bad)):
#    NewTheta_bad.append(theta_bad[i]*(np.pi/180))

#for j in range(len(R_S21_bad)):
#    New_R21_Bad.append(10**(R_S21_bad[j]/20))
#plt.polar(NewTheta_bad,  New_R21_Bad, 'bP', markersize = 3, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='Not Optimized');


IdealTheta = [];
Ideal_R21 = []; 
NormalPhaseList = [];

for state in range(0,64,1):
    Phase = state*5.625;
    NormalPhaseList.append(Phase);

for i in range(len(NormalPhaseList)):
    IdealTheta.append(NormalPhaseList[i]*(np.pi/180))
Mean_s21  = statistics.mean(New_R21)

for j in range(0,64,1):
    Ideal_R21.append(Mean_s21);

plt.polar(IdealTheta,  Ideal_R21, 'ko-', markersize = 4.5, linewidth = 1, markeredgewidth = 1, mfc = 'k', label ='Ideal step 5,625 ­°');

#plt.yticks(np.arange(0,1.5,0.25))
#for d in range (0,64,1):
#    plt.arrow(0, 0, NewTheta[d], New_R21[d], alpha = 0.5, width = 0.01, edgecolor = 'black', facecolor = 'k', lw = 0.5, zorder = 1)

plt.ylim(0,1.75)
plt.yticks(np.arange(0,1.75,0.5))
plt.xticks(np.arange(0,2.0*np.pi,np.pi/6.0))
plt.grid(True);


fig = plt.gcf();
fig.set_dpi(300.0) 
fig.set_size_inches(9, 9)

plt.legend(loc=8);

#plt.show();

plt.savefig("Polar2.tiff", dpi=300, format="tiff", bbox_inches=0, pad_inches=0)

###################################
####################################
















#################################################################
##################################################################
###################### Градусы по состояниям #####################
#ViewResult10 = pickle.load(open('FullDataSet_10GHz_ALL_New.pkl', 'rb'));
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

#SMALL_SIZE = 15
#MEDIUM_SIZE = 18
#BIGGER_SIZE = 22
#plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#csfont = {'fontname':'Times New Roman'}
#x = np.arange(5,15,0.1);
#for i in range(0,64,1):
#    plt.plot(x,LastChance[i]);
#plt.grid(color='k', linestyle='--', linewidth=0.3)

#plt.xlim(5,15.1);
#plt.ylim(0,361);


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

#fig = plt.gcf();
#fig.set_size_inches(6, 6)

#plt.xticks(np.arange(5,15.01,1))
#plt.yticks(np.arange(0,370, 45))

#plt.xlabel('Frequency (GHz)',**csfont); 
#plt.ylabel('6-Bit Phase Response (deg)',**csfont);
#plt.show();
#################################################
###############################################
#############################################
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


#plt.style.use(['science','no-latex'])
#plt.style.use(['science','no-latex'])

#with plt.style.context('science','ieee'):
#    plt.figure()
#    plt.plot([1,2,3], [4,6,7])
#    plt.show();


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







