import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle


def RemoveTwins(Population):
    Population = sorted(Population, key = lambda StateSystem: StateSystem.FitnessValue);
    doublelist = [];
    for i in range(0, (len(Population)-1),1):
        if (Population[i].RMS_Phase) != (Population[i+1].RMS_Phase):
            doublelist.append(Population[i]);
    
    doublelist.append(Population[(len(Population)-1)]);
    doublelist = sorted(doublelist, key = lambda StateSystem: StateSystem.FitnessValue)

    return doublelist
#####################################################
