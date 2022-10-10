import numpy as np
import matplotlib.pyplot as pyplot
import TemperatureData

x_axis = []
year = 1990
for i in range (0,30): 
    x_axis.append(year)
    year += 1
class Chart:
    def drawLineChart(x,y,xlabel,ylabel):
        if y == 0:
            fig = pyplot.figure()

            pyplot.title("Minimum Temperature of 1990-2019 Annually")
            pyplot.ylabel('Min Temperature (C)')
            pyplot.xlabel('Years')
            
            year = 1990
            min_temp_yearly = []
            min_temp_finallist = []
            for i in range (0,359):
                if (TemperatureData.temp_data.date_obj[0][i] == year):
                    min_temp_yearly.append(TemperatureData.temp_data.min_temp[i])
                
                if year != TemperatureData.temp_data.date_obj[0][i] or i == 358:
                    year += 1
                    min_temp_finallist.append(np.min(min_temp_yearly))
                    min_temp_yearly = []
                    min_temp_yearly.append(TemperatureData.temp_data.min_temp[i])
                    
            pyplot.plot(x_axis,min_temp_finallist, marker='o')
            pyplot.show()   

        if y != 0:
            fig = pyplot.figure()

            pyplot.title("Maximum Temperature of 1990-2019 Annually")
            pyplot.ylabel('Max Temperature (C)')
            pyplot.xlabel('Years')

            year = 1990
            max_temp_yearly = []
            max_temp_finallist = []
            for i in range (0,359):
                if (TemperatureData.temp_data.date_obj[0][i] == year):
                    max_temp_yearly.append(TemperatureData.temp_data.max_temp[i])
                       
                if year != TemperatureData.temp_data.date_obj[0][i] or 358 == i:
                    max_temp_finallist.append(np.max(max_temp_yearly))
                    max_temp_yearly = []
                    max_temp_yearly.append(TemperatureData.temp_data.max_temp[i])
                    year += 1
            pyplot.plot(x_axis,max_temp_finallist, marker='o')
            pyplot.show() 
                    
    def drawBarChart(x,y,xlabel,ylabel):
        
        if y == 0:
            fig = pyplot.figure()
            
            pyplot.title("Average Snowfall between 1990-2019 Annually")
            pyplot.ylabel('Snowfall')
            pyplot.xlabel('Years')
            
            year = 1990
            Snowfall_yearly = []
            Snowfall_finallist = []
            for i in range (0,359):
                if (TemperatureData.temp_data.date_obj[0][i] == year):
                    Snowfall_yearly.append(TemperatureData.temp_data.snowFall[i])
                
                if year != TemperatureData.temp_data.date_obj[0][i] or i == 358:
                    year += 1
                    Snowfall_finallist.append(np.mean(Snowfall_yearly))
                    Snowfall_yearly = []
                    Snowfall_yearly.append(TemperatureData.temp_data.snowFall[i])
                    
            pyplot.bar(x_axis,Snowfall_finallist, align='center', alpha=0.5)
            pyplot.show()   

        if y != 0:
            fig = pyplot.figure()

            pyplot.title("Average Temperature of 1990-2019 Annually")
            pyplot.ylabel('Temperature (C)')
            pyplot.xlabel('Years')

            year = 1990
            avg_temp_yearly = []
            avg_temp_finallist = []
            for i in range (0,359):
                if (TemperatureData.temp_data.date_obj[0][i] == year):
                    avg_temp_yearly.append(TemperatureData.temp_data.max_temp[i])
                    avg_temp_yearly.append(TemperatureData.temp_data.min_temp[i])
                       
                if year != TemperatureData.temp_data.date_obj[0][i] or 358 == i:
                    avg_temp_finallist.append(np.mean(avg_temp_yearly))
                    avg_temp_yearly = []
                    avg_temp_yearly.append(TemperatureData.temp_data.max_temp[i])
                    avg_temp_yearly.append(TemperatureData.temp_data.min_temp[i])
                    year += 1
            pyplot.bar(x_axis,avg_temp_finallist, align='center', alpha=0.5)
            pyplot.show() 
