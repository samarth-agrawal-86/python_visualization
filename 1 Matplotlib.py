# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:09:29 2018

@author: agarwas3
"""

import numpy as np
import matplotlib.pyplot as plt


import matplotlib as mpl
mpl.get_backend()

'''
# artist layer

root of visuals is a set of containers .. which includes a figure object , subplot and axes

contains primitives... such as Line2D, Rectangle, collections such as PathCollection 

axes in the most common to interact with 

axis object.. axes is plural .. it has x axis, y axis


# scriptling layer... 

pyplot

'''


##### 1 Line Graph
x = [10,20,30,40]
y = [1,2,3,4]

x2 = [11, 22, 33,44]
y2 = [100, 200, 300, 400]

plt.plot(x, y, label = 'First Line')
plt.plot(x2, y2, label = 'Second Line')
plt.title('Interesting Graph\nCheck it out') # \n will add the next content in new line
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.legend()
plt.show()



##### 2 Bar chart 


x = [2,4,6,8,10]
y =[4,5,3,2,8]


x2 = [1,3,5,7,9]
y2 = [7,2,9,3,8]

plt.bar(x, y , label = 'Bars 1', color = 'r')
plt.bar(x2, y2, label = 'Bars 2', color = 'b')

plt.title('Bar Chart') 
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.legend()
plt.show()

##### 3 Histograms
# histogram is to show a distribution. 

population_ages = [22,3,34,2,45,2,54,76,43,76,43,87,98,32,27,38,14]

bins = [0, 10,30, 50, 80]
plt.hist(population_ages, bins = bins,  histtype='bar',  label = 'Population 1', color = 'c', rwidth=0.8)
plt.title('Hist Chart') 
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


##### 4 Scatter Plots

x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4,5,6,7,8]

plt.scatter(x, y , marker = 'x', s = 200, color = 'k', label = 'Scatter points')

plt.title('Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.legend()
plt.show()


##### 5 Stack Plots
days = [1,2,3,4,5]
sleeping = [6,4,7,5,6]
playing= [2,1,3,2,1]
working = [8,9,11,10,6]

# there are no legends in this.. there's a small hack. add blank plots to this
plt.plot([] ,[], color = 'm', label = 'Sleeping')
plt.plot([] ,[], color = 'c', label = 'Playing')
plt.plot([] ,[], color = 'r', label = 'Working')

plt.stackplot(days, sleeping, playing, working, colors = ['m','c','r']) # this is little tricky here... colors not color

plt.title('Stack Plot')
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.legend()
plt.show()




##### 6 Pie Charts

days = [1,2,3,4,5]
sleeping = [6,4,7,5,6]
playing= [2,1,3,2,1]
working = [8,9,11,10,6]


slices = [7,2,13]
activities = ['sleeping', 'playing', 'working']

cols = ['c', 'm', 'r','k']

plt.pie(slices, labels = activities, colors = cols, startangle = 90, shadow = True, 
        explode = (0,0.2,0), autopct = '%1.1f%%')

plt.title('Pie Plot')
plt.show()



##### 7 Loading data from Files
import pandas as pd

dataset = pd.read_csv('fortune1000.csv', header = 0)
x = dataset['Rank']
y = dataset['Revenue']
plt.plot(x, y )
plt.xlabel('Rank')
plt.ylabel('Revenue')
plt.title('Loading data from files')
plt.show()



##### 8 Getting data frm internet
import urllib

# Quandl
# APIs

stock_price_url = ''

source_code = urllib.request.urlopen(stock_price_url).read().decode()








