import WeatherAnalyzer
import Chart

def main():
    
    x = 0
    while x <=10:
        print("1-Get Mininmum Temperature of 1990-2019")
        print("2-Get Maximum Temperature of 1990-2019")
        print("3-Get Mininmum Temperature of 1990-2019 Annually")
        print("4-Get Maximum Temperature of 1990-2019 Annually")
        print("5-Get Average Snowfall between 1990-2019 Annually")
        print("6-Get Average Temperature between 1990-2019 Annually")
        print("7-LineChart Minimum Temperature of 1990-2019 Annually")
        print("8-LineChart Maximum Temperature of 1990-2019 Annually")
        print("9-BarChart Average Snowfall between 1990-2019 Annually")
        print("10-BarChart Average Temperature between 1990-2019 Annually")
        print("11- End Program")
        print()
        option = int(input("Which option would you like 1-11?:"))
        if option == 1:
            min_Temp = WeatherAnalyzer.WeatherAnalyzer.getMinTemp()
            print("The Mininmum Temperature of 1990-2019 is:")
            print(min_Temp)
            print()
            continue
            
        if option == 2:
            max_Temp = WeatherAnalyzer.WeatherAnalyzer.getMaxTemp()
            print("The Maximum Temperature of 1990-2019 is:")
            print(max_Temp)
            print()
            continue

        if option == 3:
            min_Temp_Annually = WeatherAnalyzer.WeatherAnalyzer.getMinTempAnnually(0,0)
            print("The Mimimum Temperature of 1990-2019 Annually is: ")
            for i in range (0,30):
                print(min_Temp_Annually[i][0],min_Temp_Annually[i][1])
            print()
            continue

        if option == 4:
            max_Temp_Annually = WeatherAnalyzer.WeatherAnalyzer.getMaxTempAnnually(0,0)
            print("The Maximum Temperature of 1990-2019 Annually is: ")
            for i in range (0,30):
                print(max_Temp_Annually[i][0],max_Temp_Annually[i][1])
            print()
            continue
      
        if option == 5:
            snowfall_Annually = WeatherAnalyzer.WeatherAnalyzer.getAvgSnowFallAnnually(0,0)
            print("The Average Snowfall for 1990-2019 Annually is: ")
            for i in range (0,30):
                print(snowfall_Annually[i][0],snowfall_Annually[i][1])
            print()
            continue
        if option == 6:
            avg_temp_Annually = WeatherAnalyzer.WeatherAnalyzer.getAvgTempAnnually(0,0)
            print("The Average Temperature for 1990-2019 Annually is: ")
            for i in range (0,30):
                print(avg_temp_Annually[i][0],avg_temp_Annually[i][1])
            print()
            continue
        if option == 7:
            LineChart_min_temp = Chart.Chart.drawLineChart(0,0,0,0)
            continue
        if option == 8:
            LineChart_max_temp = Chart.Chart.drawLineChart(0,1,0,0)
            continue
        if option == 9:
            BarChart_avg_Snowfall = Chart.Chart.drawBarChart(0,0,0,0)
            continue
        if option == 10:
            BarChart_avg_temp = Chart.Chart.drawBarChart(0,1,0,0)
            continue
        else:
            print("Thank you for your time!")
            break

if __name__ == "__main__":
    main()
