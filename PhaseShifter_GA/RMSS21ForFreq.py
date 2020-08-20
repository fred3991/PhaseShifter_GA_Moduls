import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle



def RMSS21ForFreq(StateList, Frequency_i):
    #StateNum = []
    S21List = []
    for state_is in range(0,64,1):
        #StateNum.append(state_is);
        S21List.append(StateList[state_is].StateS21[Frequency_i]);
    MeanS21 = statistics.mean(S21List);
    SumList=[];
    for i in range(0,64,1):
        i_element = pow((S21List[i]-MeanS21),2);
        SumList.append(i_element);
    Sum_up = np.sum(SumList);
    RMS_S21 = np.sqrt(Sum_up/(len(SumList)-1));
    return RMS_S21

