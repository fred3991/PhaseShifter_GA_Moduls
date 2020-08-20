import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

#Классы
from StateSystem import StateSystem

#Функции ГА
from CalcRMSPhase import CalcRMSPhase
from CalcRMSS21 import CalcRMSS21
from CalcFitness import CalcFitness

from getStateForGA import getStateForGA

#Аутбридинг  - родители рандомный, второй самый далекий
def Outbreeding(Population):
    FatheIndex = random.randint(0,(len(Population)-1));

    if FatheIndex < ((len(Population)-1)//2):
        W = random.randint(0,(len(Population)-1)//4);
        MotherIndex  = W;
    elif FatheIndex > ((len(Population)-1)//2):
        W = random.randint(((len(Population)-1)//2),(len(Population)-1));
        MotherIndex  = W;
    else:
        W = random.randint(0,(len(Population)-1));
        MotherIndex  = W;

    SystemMother = Population[MotherIndex];
    SystemFather = Population[FatheIndex];

    StateList = [];        
    for state_number in range(0,64,1):

        if state_number%2 == 0:     
            
            BitA = SystemFather.StateList[state_number].StateBitA;     
            BitB = SystemFather.StateList[state_number].StateBitB; 
        else:

            BitA = SystemMother.StateList[state_number].StateBitA;     
            BitB = SystemMother.StateList[state_number].StateBitB; 


        CurrentState = getStateForGA(state_number, BitA, BitB);               
        StateList.append(CurrentState)
    RMS_Phase = CalcRMSPhase(StateList);
    RMS_S21 = CalcRMSS21(StateList);         
    StateSystemName = 'StateSystem'+'\n'
    for state_name in range(0,64,1):
        Name = str(StateList[state_name].StateNumber)+'_'+str(StateList[state_name].StateBitA)+'_'+str(StateList[state_name].StateBitB)+'\n';
        StateSystemName = StateSystemName+Name;
    FitnessValue = CalcFitness(RMS_Phase, RMS_S21);
    return StateSystem(StateList, RMS_Phase, RMS_S21, StateSystemName, FitnessValue)

