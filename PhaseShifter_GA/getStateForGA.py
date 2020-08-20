import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle
import os.path
import datetime

from State import State

from GetSystemByNumber import GetSystemByNumber

import ConfigModule


FileSystemCheck = os.path.exists('C:/Users/FedorovEA/source/repos/PhaseShifter_GA/PhaseShifter_GA/FileSystem'+str(ConfigModule.frequency)+'GHz.pkl')

if FileSystemCheck==False:

    print('FileSystem Does not Exist!!!');
    FileSystem = [];
    for state_number in range(0,64,1):
        FileSystem.append(GetSystemByNumber(state_number));
    print('File System is ready');
    print('File System Len is '+str(len(FileSystem)));
    for i in range(0,64,1):
        print(str(FileSystem[i].StateSystemName));
    print('FileSystem Is Ready....Starting GA')
    pickle.dump(FileSystem, open('FileSystem'+str(ConfigModule.frequency)+'GHz.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL);
if FileSystemCheck==True:
    print('FileSystem Exist!!!');
    FileSystem = pickle.load(open('C:/Users/FedorovEA/source/repos/PhaseShifter_GA/PhaseShifter_GA/FileSystem'+str(ConfigModule.frequency)+'GHz.pkl', 'rb'))



def getStateForGA(State_Number, BitA, BitB):




    StateFullName = ('State_'+str(State_Number)+'_'+str(BitA)+'_'+str(BitB));
    StateBitA = BitA;
    StateBitB = BitB;
    StateNumber = State_Number;
    StateS21 = FileSystem[State_Number].StateList[BitA*8+BitB].StateS21;
    StatePhase = FileSystem[State_Number].StateList[BitA*8+BitB].StatePhase;

    return State(StateFullName,StateBitA , StateBitB, StateNumber, StateS21, StatePhase)
