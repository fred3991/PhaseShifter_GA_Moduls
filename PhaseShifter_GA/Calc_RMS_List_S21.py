import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle

import ConfigModule

from RMSS21ForFreq import RMSS21ForFreq


def Calc_RMS_List_S21(StateList, Frequencies): # Создание листа СКО S21 для всех частот
    RMS_S21_List = [];
    for i in range(len(Frequencies)):
        RMS_S21_List.append(RMSS21ForFreq(StateList, i))
    return RMS_S21_List

