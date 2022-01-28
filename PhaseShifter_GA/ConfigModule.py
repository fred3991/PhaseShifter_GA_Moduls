import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle



List_Frequencies = np.arange(2, 21.1, 0.1); # Нужный лист частот для посмотрое
MutationCoefficient = 3;
FitnessGoal = 0.91;
Iterations = 4096;
PopulSize = 96;
frequency = 10; #Frequency in GHz



