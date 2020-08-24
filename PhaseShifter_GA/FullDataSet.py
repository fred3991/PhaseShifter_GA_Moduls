
#Полная дата для дальнеших анализов
class FullDataSet:
    def __init__(self, Final_StateList,
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
                       Final_RMS_S21_List):

            self.Final_StateList = Final_StateList;

            self.Final_Phase_List = Final_Phase_List;
            self.Final_S21_List = Final_S21_List;


            self.CentralFrequency = CentralFrequency;
            self.RMS_Phase_CentralFrequency = RMS_Phase_CentralFrequency;
            self.RMS_S21_CentralFrequency = RMS_S21_CentralFrequency;

            self.FitnessValue_CentralFrequency  = FitnessValue_CentralFrequency;

            self.Final_Iteration_List = Final_Iteration_List;
            self.Final_Fitness_List = Final_Fitness_List;

            self.Final_List_Frequencies = Final_List_Frequencies;

            self.Final_RMS_Phase_List  = Final_RMS_Phase_List;
            self.Final_RMS_S21_List = Final_RMS_S21_List;
