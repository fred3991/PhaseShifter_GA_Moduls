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
from getStateForGA import getStateForGA

from StateSystem import StateSystem

def GetSystemRandom():
    StateList = [];        
    for state_number in range(0,64,1):
        BitA = random.randint(0,7);
        BitB = random.randint(0,7);   
        CurrentState = getStateForGA(state_number, BitA, BitB);       
        StateList.append(CurrentState)
    RMS_Phase = CalcRMSPhase(StateList);
    RMS_S21 = CalcRMSS21(StateList);
    StateSystemName = 'StateSystem'+'\n'
    for state_name in range(0,64,1):
        Name = str(StateList[state_name].StateNumber)+'_'+str(StateList[state_name].StateBitA)+'_'+str(StateList[state_name].StateBitB)+'\n';
        StateSystemName = StateSystemName+Name;
    FitnessValue = CalcFitness(RMS_Phase, RMS_S21);
    #print('Random System is created!!!');
    return StateSystem(StateList, RMS_Phase, RMS_S21, StateSystemName, FitnessValue)

