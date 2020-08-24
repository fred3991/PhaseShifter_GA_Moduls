from FullDataSet import FullDataSet
import ConfigModule
import numpy as np

def CreateDataSet(FinalSolution, IterationList, FitnessList, DataResult):

    Final_StateList = FinalSolution.StateList;

   

    PhaseList = [];
    for state_is in range(0,64,1):
        PhaseList.append(Final_StateList[state_is].StatePhase-Final_StateList[0].StatePhase);
    #Unwrap        
    PhaseList = np.deg2rad(PhaseList);
    PhaseList = np.unwrap(PhaseList);
    PhaseList = np.rad2deg(PhaseList);

    Final_Phase_List = PhaseList;

    S21List = []

    for state_is in range(0,64,1):
        #StateNum.append(state_is);
        S21List.append(Final_StateList[state_is].StateS21);
    Final_S21_List = S21List;

    CentralFrequency = ConfigModule.frequency;
    RMS_Phase_CentralFrequency = FinalSolution.RMS_Phase;
    RMS_S21_CentralFrequency = FinalSolution.RMS_S21;
    FitnessValue_CentralFrequency = FinalSolution.FitnessValue;
    Final_Iteration_List = IterationList;
    Final_Fitness_List = FitnessList;
    Final_List_Frequencies = ConfigModule.List_Frequencies;
    Final_RMS_Phase_List = DataResult.RMS_Phase_List;
    Final_RMS_S21_List =   DataResult.RMS_S21_List;

    return FullDataSet(
        Final_StateList,
        Final_Phase_List,
        Final_S21_List,
        CentralFrequency, 
        RMS_Phase_CentralFrequency, 
        RMS_S21_CentralFrequency, 
        FitnessValue_CentralFrequency, 
        Final_Iteration_List, 
        Final_Fitness_List,
        Final_List_Frequencies, 
        Final_RMS_Phase_List, 
        Final_RMS_S21_List);

                       #Final_StateList,
                       #Final_Phase_List,
                       #Final_S21_List,
                       #CentralFrequency, 
                       #RMS_Phase_CentralFrequency, 
                       #RMS_S21_CentralFrequency, 
                       #FitnessValue_CentralFrequency, 
                       #Final_Iteration_List, 
                       #Final_Fitness_List,
                       #Final_List_Frequencies, 
                       #Final_RMS_Phase_List, 
                       #Final_RMS_S21_List):