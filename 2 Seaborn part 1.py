# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:28:07 2018

@author: AGARWAS3
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets


df = pd.read_csv('battles.csv')


df.head(3)

sns.barplot(x='year', y ='major_death', data = df)

# with some style settings
sns.set_style('whitegrid')
sns.barplot(x='year', y ='major_death', data = df)

# to define the styling or change the customizations of our visualizations
#set(), set_style(), set_context (), set_palette()

# right now we need to use set_context


# you can also use
plt.style.use('seaborn')
plt.style.use('default')


#anyways lets get back to seaborn

sns.set_context(font_scale = 2, rc = {'font.size':15, 'axes.labelsize' : 20})
sns.set_style('whitegrid')
sns.barplot(x='year', y ='major_death', data = df)

sns.axes_style()


#### 2 Factor Plot : Nested bar plot

ex2 = sns.factorplot(x = 'attacker_size', y = 'defender_size', data = df, hue = 'attacker_outcome', kind = 'bar', palette = 'muted')

# x axis are mixed up
# sizes or x tick rotation

ex2 = sns.factorplot(x = 'attacker_size', y = 'defender_size', data = df, hue = 'attacker_outcome', kind = 'bar', palette = 'muted')
plt.xticks(rotation=70)
plt.rcParams['xticks.labelsize']=9



#### 3 Joint Kernel Density Estimate

# bi variate date - where each value of one of the variable is paired with a value of other variable

iris = datasets.load_iris()
X = iris.data[:,:]
X = pd.DataFrame(X)
X.rename(columns = { 0: 'sepal_len', 1: 'sepal_wid', 2: 'petal_len', 3: 'petal_wid'}, inplace = True)

ex3 = sns.jointplot(x = X['sepal_len'], y = X['petal_len'], kind = 'kde', size = 7, space = 1, color = 'b')



#### 4 Heatmaps
# we will use the datasets with seaborn
# we will use flights data

flights = sns.load_dataset('flights')
flights = flights.pivot(index = 'month', columns = 'year', values = 'passengers')
ex4 = sns.heatmap(flights)

# some of the parameters we can pass
ex4 = sns.heatmap(flights, annot = True, fmt = 'd')

ex4 = sns.heatmap(flights, cmap = 'BuPu')

ex4 = sns.heatmap(flights, linewidths = 0.2)

ex4 = sns.heatmap(flights, cbar = False, )


#### 5 Swarm Plot
# does not scale well with large quantities of data
pokemon = pd.read_csv('Pokemon.csv', index_col = '#')

pokemon.dtypes
pokemon.info()

ex5 = sns.swarmplot(data = pokemon, x = 'Type 1', y = 'Attack')
plt.xticks(rotation = 45)
plt.rcParams({'xtick.labelsize': 15 })



#### 6 Linear Regression

ex6 = sns.lmplot( data = pokemon, x = 'Attack', y = 'HP', hue = 'Generation')


#### 7 Violin Plot

ex7 = sns.violinplot(data = pokemon, x = 'Type 1', y = 'Attack')
ex7 = sns.violinplot(data = pokemon, x = 'Type 1', y = 'Attack', inner = None)

#### Combine 2 plots

pokemon_plot = sns.violinplot(data = pokemon, x = 'Type 1', y = 'Attack', inner = None)
pokemon_plot = sns.swarmplot(data = pokemon, x = 'Type 1', y = 'Attack', color = 'white', edgecolor = 'gray')
plt.rcParams



#### 8 relplot

mpg = sns.load_dataset('mpg')
ex8 = sns.relplot(data = mpg, x = 'mpg', y ='horsepower' , hue = 'origin')


#### 9 Scatterplot

exercise = sns.load_dataset('exercise')
ex9 = sns.scatterplot(data = exercise, x = 'id', y = 'pulse', hue = 'kind')


#### 10 lineplot
flights = sns.load_dataset('flights')
ex10 = sns.lineplot(data = flights, x = 'year', y = 'passengers')
ex10 = sns.lineplot(data = flights, x = 'year', y = 'passengers', hue = 'month')






