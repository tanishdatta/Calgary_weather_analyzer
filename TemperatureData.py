import FileIO
import numpy as np


file_path = "Project_milestone_2_TanishDatta_FurkanDastan_GRAY/CalgaryWeather.csv"
data_table = np.loadtxt(file_path , delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
file1 = FileIO.FileIO(file_path,data_table)
class TemperatureData:
    def __init__(self,y,m,min_temp,max_temp,snowFall):
        self.date_obj = (y,m)
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.snowFall = SnowFall
m = []
y = []
min_temp = []
max_temp = []
SnowFall = []

for i in range(0,359):
    y= np.append(y, file1.dataTable[i][0])
    m = np.append(m, file1.dataTable[i][1])
    max_temp = np.append(max_temp, file1.dataTable[i][2])
    min_temp = np.append(min_temp, file1.dataTable[i][3])
    SnowFall = np.append(SnowFall, file1.dataTable[i][4])

temp_data = TemperatureData(y,m,min_temp,max_temp,SnowFall)

    

    
     