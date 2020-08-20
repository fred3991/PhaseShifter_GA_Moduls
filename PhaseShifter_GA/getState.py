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



def getState(State_Number, BitA, BitB):
    ntwk = rf.Network('C:/Users/FedorovEA/data/state'+str(State_Number)+'/PS_test__'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB)+'.s2p')
    S21 = float(ntwk.s21[str(ConfigModule.frequency)+'ghz'].s_db[...]);
    Fi  = float(ntwk.s21[str(ConfigModule.frequency)+'ghz'].s_deg[...]);
    StateFullName = ('State_'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB));
    StateBitA = BitA;
    StateBitB = BitB;
    StateNumber = State_Number;
    StateS21 = S21;
    StatePhase = Fi;
    return State(StateFullName,StateBitA , StateBitB, StateNumber, StateS21, StatePhase)

