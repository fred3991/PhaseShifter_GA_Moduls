import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle


frequency = 10; #Frequency in GHz
List_Frequencies = np.arange(3, 20.1, 0.1); # Нужный лист частот для посмотрое
MutationCoefficient = 3;
FitnessGoal = 0;
Iterations = 33;
PopulSize = 16;
