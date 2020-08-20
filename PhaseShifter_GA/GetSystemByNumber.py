import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

from CalcRMSPhase import CalcRMSPhase
from CalcRMSS21 import CalcRMSS21
from CalcFitness import CalcFitness
from getState import getState


from StateSystem import StateSystem

def GetSystemByNumber(state_number):
    PrimaryStateSubList = [];        
    for bit_A in range(0,8,1):
        for bit_B in range(0,8,1):
            BitA = bit_A;
            BitB = bit_B;   
            CurrentState = getState(state_number, BitA, BitB);       
            PrimaryStateSubList.append(CurrentState);
    RMS_Phase = 0;
    RMS_S21 = 0;
    StateSystemName = 'StateSystem'+'\n'
    for state_name in range(0,64,1):
        Name = str(PrimaryStateSubList[state_name].StateNumber)+'_'+str(PrimaryStateSubList[state_name].StateBitA)+'_'+str(PrimaryStateSubList[state_name].StateBitB)+'\n';
        StateSystemName = StateSystemName+Name;
    FitnessValue = CalcFitness(RMS_Phase, RMS_S21);
    print('System state '+str(state_number)+' added')  
    return StateSystem(PrimaryStateSubList, RMS_Phase, RMS_S21, StateSystemName, FitnessValue)

