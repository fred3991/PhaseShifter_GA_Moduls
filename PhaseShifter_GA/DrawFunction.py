import skrf as rf
from matplotlib import pyplot as plt
import numpy as np
import math as math
import statistics
import random
import toolz
import pickle


def DrawFunction(x, y, xlim, ylim, xTicks, yTicks, LineColorType, MarkerSize, LineLabel, xlabel, ylabel, plotTitle):
    x = x;
    y = y;
    plt.grid(color='k', linestyle='--', linewidth=0.3)
    plt.ylabel(ylabel);  # Подписи у
    plt.xlabel(xlabel);  # Подписи х
    plt.xlim(xlim);   # границы X
    plt.ylim(ylim);  # границы Y
    plt.xticks(xTicks)
    plt.yticks(yTicks)   
    plt.grid(color='k', linestyle='--', linewidth=0.3);
    plt.title(plotTitle);
    plt.plot(x,y, LineColorType,   markersize = MarkerSize, markerfacecolor = 'k',  label=LineLabel);
    plt.legend(loc=0);
    return  plt.show();
