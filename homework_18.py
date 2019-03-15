import matplotlib.pyplot as plt
import pandas as pd

#import from excel
df = pd.read_excel('data_tasks.xlsx', sheet_name = 'task1')
print(df)

print(df.values[:,1])

df2 = pd.read_excel('data_tasks.xlsx', sheet_name = 'task2')
print(df2)

# plot 1

x_timepoints = df.iloc[:,0]
y_temp = df.iloc[:, 1]
std_dev1 = df.iloc[:, 2]
plt.errorbar(x_timepoints, y_temp, yerr = std_dev1, fmt = "rs--", linewidth =3,
             elinewidth = 0.5, ecolor = 'k', capsize =5, capthick=1)
plt.xlabel("Time (Minutes)", fontweight = 'bold', fontsize = 14)
plt.ylabel("Temperature (Celsius)", fontweight = 'bold', fontsize = 14)
plt.savefig("lineplot.png", dpi = 600)

# plot 2
plt.figure()
cities = ["Las Vegas", "Durango", "Denver"]
x_timepoints2 = df2.iloc[:,0 ]
x_timepoints2 = list(x_timepoints2)
del x_timepoints2[0]

LV_temps = df2.iloc[:,1]
LV_temps = list(LV_temps)
del LV_temps[0]
LV_DV = list(df2.iloc[:,2])
del LV_DV[0]

DUR_temps = df2.iloc[:, 3]
DUR_temps = list(DUR_temps)
del DUR_temps[0]
DUR_DV = list(df2.iloc[:,4])
del DUR_DV[0]

DEN_temps = df2.iloc[:, 5]
DEN_temps = list(DEN_temps)
del DEN_temps[0]
DEN_DV = list(df2.iloc[:, 6])
del DEN_DV[0]

import numpy as np

barWidth = 0.25

r1 = np.arange(len(LV_temps))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, LV_temps, color = '#7f6d5f', width = barWidth, edgecolor = 'white', label = 'Las Vegas Temperatures',
        yerr = LV_DV, capsize = 5)
plt.bar(r2, DUR_temps, color = '#557f2d', width = barWidth, edgecolor = 'white', label = 'Durango Temperatures',
        yerr = DUR_DV, capsize = 5)
plt.bar(r3, DEN_temps, color = '#2d7f5e', width = barWidth, edgecolor = 'white', label = 'Denver Temperatures',
        yerr = DEN_DV, capsize = 5)
        
plt.xlabel('Time (Hours)', fontweight = 'bold', fontsize = 14)
plt.xticks([r + barWidth for r in range(len(LV_temps))], x_timepoints2)
plt.ylabel('Temperature (Celsius)', fontweight = 'bold', fontsize = 14)
plt.legend()
plt.savefig('bargraph.png', dpi = 600)