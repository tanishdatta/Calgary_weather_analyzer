import Date
import numpy as np
import TemperatureData

class WeatherAnalyzer:
    def __init__(self,Temperature_Data):
        Temperature_Data = TemperatureData.temp_data
        self.Temperature_Data = Temperature_Data
    def getMinTemp():
        Data = WeatherAnalyzer(0)
        min_temp = np.min(Data.Temperature_Data.min_temp)
        
        for i in range(0,359):
            if Data.Temperature_Data.min_temp[i] == min_temp:
                year = int(Data.Temperature_Data.date_obj[0][i])
                month = int(Data.Temperature_Data.date_obj[1][i])
        final_array = (f'Year:{year}   Month:{month}   Temperature:{min_temp} Degrees Celsius')
        return(final_array)
        
     
    def getMinTempAnnually(m,y):
        year_array = []
        list_min_temp = []
        list_years = []
        final_list = []
        final_final_list = []
        date = Date.Date(m,y)
        Year = date.Year
        Data = WeatherAnalyzer(0)
        for i in range(0,359):
            if (Data.Temperature_Data.date_obj[0][i]) == Year:
                year_array.append(Data.Temperature_Data.min_temp[i])
            if Data.Temperature_Data.date_obj[0][i] != Year or i == 358:
                list_years.append(f'Year: {Year}') 
                list_min_temp.append(f'Temperature: {np.min(year_array)} degrees celsius')
                final_list.append(list_years)
                final_list.append(list_min_temp)
                final_final_list.append(final_list)
                year_array = []
                final_list = []
                list_years = []
                list_min_temp = []
                year_array.append(Data.Temperature_Data.min_temp[i])
                Year += 1
        return(final_final_list)
    def getMaxTemp(): 
        Data = WeatherAnalyzer(0)
        max_temp = np.max(Data.Temperature_Data.max_temp)
        
        for i in range(0,359):
            if Data.Temperature_Data.max_temp[i] == max_temp:
                year = int(Data.Temperature_Data.date_obj[0][i])
                month = int(Data.Temperature_Data.date_obj[1][i])
        final_array = (f'Year:{year}   Month:{month}   Temperature:{max_temp} Degrees Celsius')
        return(final_array)
       
    def getMaxTempAnnually(m,y):
        year_array = []
        list_max_temp = []
        list_years = []
        final_list = []
        final_final_list = []
        date = Date.Date(m,y)
        Year = date.Year
        Data = WeatherAnalyzer(0)
        for i in range(0,359):
            if (Data.Temperature_Data.date_obj[0][i]) == Year:
                year_array.append(Data.Temperature_Data.max_temp[i])
            if Data.Temperature_Data.date_obj[0][i] != Year or i == 358:
                list_years.append(f'Year: {Year}') 
                list_max_temp.append(f'Temperature: {np.max(year_array)} degrees celsius')
                final_list.append(list_years)
                final_list.append(list_max_temp)
                final_final_list.append(final_list)
                year_array = []
                final_list = []
                list_years = []
                list_max_temp = []
                Year += 1
        return(final_final_list)
    def getAvgSnowFallAnnually(m,y):
        year_array = []
        list_avg_snowfall = []
        list_years = []
        final_list = []
        final_final_list = []
        date = Date.Date(m,y)
        Year = date.Year
        Data = WeatherAnalyzer(0)
        for i in range(0,359):
            if (Data.Temperature_Data.date_obj[0][i]) == Year:
                year_array.append(Data.Temperature_Data.snowFall[i])
            if Data.Temperature_Data.date_obj[0][i] != Year or i == 358:
                list_years.append(f'Year: {Year}') 
                list_avg_snowfall.append(f'Snowfall: {"{:.2f}".format(np.mean(year_array))}cm')
                final_list.append(list_years)
                final_list.append(list_avg_snowfall)
                final_final_list.append(final_list)
                year_array = []
                final_list = []
                list_years = []
                list_avg_snowfall = []
                year_array.append(Data.Temperature_Data.snowFall[i])
                Year += 1
        return(final_final_list)
    
    def getAvgTempAnnually(m,y):
        year_array = []
        list_avg_temp = []
        list_years = []
        final_list = []
        final_final_list = []
        date = Date.Date(m,y)
        Year = date.Year
        Data = WeatherAnalyzer(0)
        for i in range(0,359):
            if (Data.Temperature_Data.date_obj[0][i]) == Year:
                year_array.append(Data.Temperature_Data.min_temp[i])
                year_array.append(Data.Temperature_Data.max_temp[i])
            if Data.Temperature_Data.date_obj[0][i] != Year or i == 358:
                list_years.append(f'Year: {Year}') 
                list_avg_temp.append(f'Temperature: { "{:.2f}".format(np.mean(year_array))} degrees celsius')
                final_list.append(list_years)
                final_list.append(list_avg_temp)
                final_final_list.append(final_list)
                year_array = []
                final_list = []
                list_years = []
                list_avg_temp = []
                year_array.append(Data.Temperature_Data.min_temp[i])
                year_array.append(Data.Temperature_Data.max_temp[i])
                Year += 1
        return(final_final_list)