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


def Mutation(Chromosome, MutationCoeff):

    NumberOfMutants = 64*(MutationCoeff/100);

    NumberOfMutants = round(NumberOfMutants);

    NumberOfMutants = int(NumberOfMutants)
    
    randomstates = []
    for i in range(0,NumberOfMutants):
            n = random.randint(0,63)
            randomstates.append(n);
    
    randomstates = list(set(randomstates));

    sequence = [-1, 1];
    
    BitChange = random.choice(sequence); 

    for i in randomstates:

        GodNumber = random.randint(0,6);

        if GodNumber==0:
            Chromosome.StateList[i].StateBitA = random.randint(0,7)
            Chromosome.StateList[i].StateBitB = random.randint(0,7)

        elif GodNumber==1:
            Chromosome.StateList[i].StateBitA = random.randint(0,7)

        elif GodNumber==2:
            Chromosome.StateList[i].StateBitB = random.randint(0,7)
        
        elif GodNumber==3:
            BitState = Chromosome.StateList[i].StateBitA;

            if (BitState>0 and BitState<7):
                Chromosome.StateList[i].StateBitA = BitState+BitChange;
            if BitState==0:
                Chromosome.StateList[i].StateBitA = BitState+1;
            if BitState==7:
                Chromosome.StateList[i].StateBitA = BitState-1;
                
        elif GodNumber==4:
            BitState = Chromosome.StateList[i].StateBitB;
            if (BitState>0 and BitState<7):
                Chromosome.StateList[i].StateBitB = BitState+BitChange;
            if BitState==0:
                Chromosome.StateList[i].StateBitB = BitState+1;
            if BitState==7:
                Chromosome.StateList[i].StateBitB = BitState-1;	
        elif GodNumber==5:
            BitStateA = Chromosome.StateList[i].StateBitA;
            BitStateB = Chromosome.StateList[i].StateBitB;

            if ((BitStateA>0 and BitStateA<7) and (BitStateB>0 and BitStateB<7)):
                Chromosome.StateList[i].StateBitA = BitStateA+BitChange;
                Chromosome.StateList[i].StateBitB = BitStateB+BitChange;
            else:
                Chromosome.StateList[i].StateBitA = BitStateA;
                Chromosome.StateList[i].StateBitB = BitStateB;
        else:
            BitStateA = Chromosome.StateList[i].StateBitA;
            BitStateB = Chromosome.StateList[i].StateBitB;

            Chromosome.StateList[i].StateBitA = BitStateB;
            Chromosome.StateList[i].StateBitB = BitStateA;

    StateList = Chromosome.StateList;

    RMS_Phase = CalcRMSPhase(StateList);
    RMS_S21 = CalcRMSS21(StateList);
    StateSystemName = 'StateSystem'+'\n'
    for state_name in range(0,64,1):
        Name = str(StateList[state_name].StateNumber)+'_'+str(StateList[state_name].StateBitA)+'_'+str(StateList[state_name].StateBitB)+'\n';
        StateSystemName = StateSystemName+Name;
    FitnessValue = CalcFitness(RMS_Phase, RMS_S21);
    #print('Random System is created!!!');
    return StateSystem(StateList, RMS_Phase, RMS_S21, StateSystemName, FitnessValue)

