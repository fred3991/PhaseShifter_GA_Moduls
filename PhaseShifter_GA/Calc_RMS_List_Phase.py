import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

import ConfigModule

NormalPhaseList = [];

for state in range(0,64,1):
    Phase = state*5.625;
    NormalPhaseList.append(Phase);


def Calc_RMS_List_Phase(StateList, Frequencies): # Создание листа СКО Фазы для всех частот
    RMS_Phase_List = [];

    for g in range(len(Frequencies)):
        RMS_Phase = 0;
        PhaseList = [];
        for state_is in range(0,64,1):
            PhaseList.append(StateList[state_is].StatePhase[g]-StateList[0].StatePhase[g]);       
        PhaseList = np.deg2rad(PhaseList);
        PhaseList = np.unwrap(PhaseList);
        PhaseList = np.rad2deg(PhaseList);
            #Set Unwrap to StateList
        for unwrap_state in range(0,64,1):
            StateList[unwrap_state].StatePhase[g]=PhaseList[unwrap_state];
        #Делаем лист ошибки
        ErrorList = [];
        for i in range(0,64,1):     
            ErrorList.append(PhaseList[i] - NormalPhaseList[i]);
            #cреднее значение ошибки
        MeanErrorPhase = statistics.mean(ErrorList)    
            #лист суммы для 
        SumList=[];
        for sum_i in range(0,64,1):
            i_element = pow((ErrorList[sum_i]-MeanErrorPhase),2);
            SumList.append(i_element);
        Sum_up = np.sum(SumList)
        RMS_Phase = np.sqrt(Sum_up/(len(SumList)-1));
        RMS_Phase_List.append(RMS_Phase)
    return RMS_Phase_List

