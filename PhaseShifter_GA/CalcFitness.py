import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

import ConfigModule

def CalcFitness(RMS_Phase, RMS_S21):

    Weight_Phase =  0.2372
    ##1.5290730910033676
    Weight_S21 =  1.4408
    ##Weight_S21 =  1
    ##RMS S21 is 0.3462035110814324

    RMS_Phase_Fit = RMS_Phase*Weight_Phase;
    if RMS_Phase_Fit>0.5:
        RMS_Phase_Fit = 0.5; 

    RMS_S21_Fit = RMS_S21*Weight_S21;
    if RMS_S21_Fit>0.5:
        RMS_S21_Fit = 0.5;

    FitnessValue = RMS_Phase#+RMS_S21_Fit; 

    return FitnessValue

