import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

from State import State

import ConfigModule

def getStateAllFreq(State_Number, BitA, BitB, Frequencies):
    ntwk = rf.Network('C:/Users/FedorovEA/data/state'+str(State_Number)+'/PS_test__'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB)+'.s2p');
    S21  = [];  #создание списков для с21 и фазы для диапазона частот количеством len(Frequencies)
    Fi   = [];  # для оптимизации по этим частотам

    for freqlist in range(len(Frequencies)):  # Считываем по частотам список фазы и амплитуды по выбранным частотам
        S21.append(float(ntwk.s21[str(Frequencies[freqlist])+'ghz'].s_db[...]));
        Fi.append(float(ntwk.s21[str(Frequencies[freqlist])+'ghz'].s_deg[...]));

    StateFullName = ('State_'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB));
    StateS21 = S21;  # присвоение в классе листа частот для состояния
    StatePhase = Fi;  # присвоение в классе листа частот для состояния
    StateBitA = BitA; # записваем номер бита А
    StateBitB = BitB; # записваем номер бита B
    StateNumber = State_Number;
    print('ШО? '+str(StateNumber));

    return State(StateFullName,StateBitA , StateBitB, StateNumber, StateS21, StatePhase)
