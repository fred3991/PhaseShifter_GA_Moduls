import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle



List_Frequencies = np.arange(8, 12, 0.1); # Нужный лист частот для посмотрое
MutationCoefficient = 3;
FitnessGoal = 0;
Iterations = 5;
PopulSize = 32;
frequency = 10.5; #Frequency in GHz

