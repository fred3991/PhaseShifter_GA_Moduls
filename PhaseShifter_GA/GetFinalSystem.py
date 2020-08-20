import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle


from RMSPhaseForFreq import RMSPhaseForFreq
from RMSS21ForFreq import RMSS21ForFreq
from Calc_RMS_List_Phase import Calc_RMS_List_Phase
from Calc_RMS_List_S21 import Calc_RMS_List_S21

from FinalSystemData import FinalSystemData

from getStateAllFreq import getStateAllFreq


import ConfigModule


def GetFinalSystem(FinalSolution):

    newFileSystemData = []; # заносим в память все анализируемые файлы

    for state_number in range(0,64,1):
        newFileSystemData.append(getStateAllFreq(state_number, FinalSolution.StateList[state_number].StateBitA, FinalSolution.StateList[state_number].StateBitB, ConfigModule.List_Frequencies));
    print('File System Len is '+str(len(newFileSystemData)));
    print('FileSystem Is Ready....Starting GA')


    StateList = newFileSystemData;
    # Список состояний собран, начинаем считать все ско и параматры
    RMS_Phase_List = Calc_RMS_List_Phase(StateList, ConfigModule.List_Frequencies); # функция для расчет из листа состояний ско для всех частот - лист - добавить
    RMS_S21_List   = Calc_RMS_List_S21(StateList, ConfigModule.List_Frequencies)   # функция для расчет из листа состояний ско для всех частот fамлпитуда- лист  - добавить
    # Создание имени системы - полный список
    StateSystemName = 'StateSystem'+'\n'
    for state_name in range(0,64,1):
        Name = str(StateList[state_name].StateNumber)+'_'+str(StateList[state_name].StateBitA)+'_'+str(StateList[state_name].StateBitB)+'\n';
        StateSystemName = StateSystemName+Name;
    print('ПОсчитаем');
    # Система собрана и готова
    return FinalSystemData(StateList, RMS_Phase_List, RMS_S21_List, StateSystemName)


