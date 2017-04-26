us_data = [
]

china_data = [
]

world_data = [
]

class Data(object):
    def __init__(self, year, gdp, urban_air, suburban_air, rural_air, air_index):
        self.year = year
        self.gdp = gdp
        self.urban_air = urban_air
        self.suburban_air = suburban_air
        self.rural_air = rural_air
        self.air_index = air_index
    
stuff = [
    Data(1983, 1007.82, 1.5, 0.69, 0.70, 1.32),
    Data(1984, 1108.50, 1.4, 0.65, 0.66, 1.29),
    Data(1985, 1311.22, 1.53, 0.62, 0.63, 1.29),
    Data(1986, 1363.27, 1.56, 1.012, 0.66, 1.29),
    Data(1987, 1495.24, 1.51, 1.10, 0.70, 1.29),
    Data(1988, 1755.44, 1.48, 1.09, .72, 1.3),
    Data(1989, 1897.01, 1.64, 1.23, 0.77, 1.45),
    Data(1990, 2010.2, 1.55, 1.36, 0.75, 1.41),
    Data(1991, 2365.65, 1.66, 1.31, 0.77, 1.4, ),
    Data(1992, 2942.86, 1.5, 1.32, 0.73, 1.32),
    Data(1993, 3979.59, 1.37, 1, 0.62, 1.14),
    Data(1994, 5171.43, 1.33, 1.08, 0.63, 1.11),
    Data(1995, 6442.86, 1.23, 1.02, 0.69, 1.05),
    Data(1996, 7576.52, 1.37, 0.92, 0.70, 1.03),
    Data(1997, 8758.5, 1.53, .85, .68, 1.06),
    Data(1998, 9605.44, 1.42, 0.83, 0.65, 1.00),
    Data(1999, 10477.89, 1.33, 0.74, 0.65, 0.98),
    Data(2000, 11750.68, 1.23, 0.73, 0.64, 0.96),
    Data(2001, 12714.97, 1.24, 0.77, 0.63, 0.82),
    Data(2002, 13825.17, 0.92, 0.73, 0.66, 0.91),
    Data(2003, 15890.48, 0.94, 0.73, 0.6, 0.92),
    Data(2004, 18811.9, 1.03, 0.85, 0.64, 1.01),
    Data(2005, 22956.46, 1.00, 0.81, 0.62, 1.00)
]

# import matplotlib.pyplot
import matplotlib.pyplot as plt
import pylab
import numpy as np

years = [item.year for item in stuff \
        if item.year > 1982]
        # if item.year > 1991]
gdps = [item.gdp for item in stuff \
        if item.year > 1982]
        # if item.year > 1991]
air_index = [item.air_index for item in stuff \
        if item.year > 1982]
        # if item.year > 1991]
# color='#23373b'
color='#000000'
plt.scatter(years, gdps, color=color)
# plt.scatter(years, air_index)
plt.plot(np.unique(years), np.poly1d(np.polyfit(years, gdps, 1))(np.unique(years)), color=color)
plt.show()
