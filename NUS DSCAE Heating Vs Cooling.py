import pathlib, os, pandas as pd, seaborn as sns, matplotlib.pyplot as plt

def getfiles(path):
    os.chdir(path)
    file_list = []
    for entry in os.scandir(os.getcwd()):
        if entry.is_file():
            file_list.append(entry)
    return file_list

def make_color_division(x):
  if x < 14:
    return "Heating"
  else:
    return "Cooling"

path_rawdata = pathlib.Path.home() / "Documents" / "Certificaciones Online" / "edX" / "Data Science for Construction, Architecture and Engineering" / "3 - Construction - Pandas Fundamentals" / "meter_data"
path_weather_data = pathlib.Path.home() / "Documents" / "Certificaciones Online" / "edX" / "Data Science for Construction, Architecture and Engineering" / "3 - Construction - Pandas Fundamentals" / "weather_data"
os.chdir(path_rawdata)
rawdata = pd.read_csv("UnivClass_Ciara.csv", parse_dates=True, index_col='timestamp')
os.chdir(path_weather_data)
weather_data = pd.read_csv("weather2.csv", index_col='timestamp', parse_dates=True)
weather_hourly = weather_data.resample("H").mean()
weather_hourly_nooutlier = weather_hourly[weather_hourly > -40]
weather_hourly_nooutlier_nogaps = weather_hourly_nooutlier.fillna(method='ffill')
rawdata = rawdata[~rawdata.index.duplicated(keep='first')]
comparison = pd.concat([weather_hourly_nooutlier_nogaps['TemperatureC'], rawdata['UnivClass_Ciara']], axis=1)
comparison_merged = pd.merge(weather_hourly_nooutlier_nogaps['TemperatureC'], rawdata['UnivClass_Ciara'], left_index=True, right_index=True, how='outer')
comparison = comparison.resample("D").mean()
comparison['heating_vs_cooling'] = comparison.TemperatureC.apply(lambda x: make_color_division(x))
g = sns.lmplot(x="TemperatureC", y="UnivClass_Ciara", hue="heating_vs_cooling", truncate=True, data=comparison)
g = g.set_axis_labels("Outdoor Air Temperature", "Average Hourly kWH")
#plt.show()
plt.savefig("HeatingvsCooling.png", bbox_inches = 'tight', pad_inches = .5)
