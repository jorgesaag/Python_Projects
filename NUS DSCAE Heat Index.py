import pathlib, os, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
new_path = pathlib.Path.home() / "Documents" / "Certificaciones Online" / "edX" / "Data Science for Construction, Architecture and Engineering" / "4 - Operations - Statistics and Visualization"
os.chdir(new_path)
#ieq_data_pivoted = ieq_data.pivot_table(index='Country', columns='ThermalSensation_rounded', values='Air temperature (C)', aggfunc='mean')
ieq_data = pd.read_csv("ashrae_thermal_comfort_database_2.csv", index_col='Unnamed: 0')
print(ieq_data.info())
#What if we're interested in a more comprehensive index for evaluating thermal environment?
#Heat index , which includes both Air temperature (C) and Relative humidity (%) is a metric that simulates the real temperature
#people feel (e.g, higher humidity would make people feel warmer).
#In this exercise, try first to calculate the heat index based on Air temperature (C) and Relative humidity (%),
#then work out the average heat index for each Cooling startegy_building level in each Building type (rounded to two decimal places).
#Finally, provide the lowest value among them as your answer
#(e.g., the lowest value xx.xx may come from Cooling startegy_building level A in Building type B).

#Here is a short introduction of heat index:
#The heat index, also known as the apparent temperature, is an index that combines air temperature and relative humidity to reflect
#what the temperature feels like to the human body.
#For example, people usually feel warmer under higher humidity, even at the same temperature.
#The heat index is calculated from the following formula:

#HI = c1 + c2T + c3R + c4TR + c5T^2 + c6R^2 + c7T^2R + c8TR^2 + c9T^2R^2

#where:
#HI = heat index (in degrees Celsius)
#T = ambient dry-bulb temperature (in degrees Celsius)
#R = relative humidity (percentage value between 0 and 100)
c1 = -8.78469475556
c2 = 1.61139411
c3 = 2.33854883889
c4 = -0.14611605
c5 = -0.012308094
c6 = -0.0164248277778
c7 = 0.002211732
c8 = 0.00072546
c9 = -0.000003582

#Calculate heat index and assign to a new column 'HI'



# Use groupby() or pivot_table() function aggregated by mean(), and find the lowest value among aggregated values
