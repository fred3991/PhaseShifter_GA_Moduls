import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

NormalPhaseList = [];

for state in range(0,64,1):
    Phase = state*5.625;
    NormalPhaseList.append(Phase);

def RMSPhaseForFreq(StateList, Frequency_i):  #Cчитаем лист СКО по фазе для всех частот

    #считаем RMS фазы
    PhaseList = [];
    for state_is in range(0,64,1):
        PhaseList.append(StateList[state_is].StatePhase[Frequency_i]-StateList[0].StatePhase[Frequency_i]);
    #Unwrap        
    PhaseList = np.deg2rad(PhaseList);
    PhaseList = np.unwrap(PhaseList);
    PhaseList = np.rad2deg(PhaseList);
    #Set Unwrap to StateList
    for unwrap_state in range(0,64,1):
        StateList[unwrap_state].StatePhase[Frequency_i]=PhaseList[unwrap_state];
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
    return RMSPhaseForFreq


