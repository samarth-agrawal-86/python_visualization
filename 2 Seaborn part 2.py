# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:40:55 2018

@author: agarwas3
"""
'''
https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
https://elitedatascience.com/python-seaborn-tutorial
https://seaborn.pydata.org/tutorial.html

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


###### 1 NUMERICAL VARIABLES
tips = sns.load_dataset('tips')
pokemon = pd.read_csv('pokemon.csv')

sns.relplot( data = tips, x = 'total_bill', y = 'tip', kind = 'scatter')       

sns.relplot( data = pokemon, x = 'Attack', y = 'Defense' , kind = 'scatter', hue='Type 1', size = 'Total')

sns.relplot( data = pokemon, x = 'Attack', y = 'Defense' , kind = 'scatter', hue='Type 1', col = 'Legendary', row = 'Type 2')

sns.relplot( data = pokemon, x = 'Attack', y = 'Defense' , kind = 'scatter', hue='Type 1', col = 'Type 2', col_wrap = 4)


sns.relplot( data = pokemon, x = 'Attack', y = 'Defense', kind = 'line', hue = 'Legendary', ci = False,  markers = [True])



###### 2 CATEGORICAL VARIABLES
pokemon['Type 1'].unique()
pokemon['Type 1'].nunique()
pokemon['Type 2'].unique()
pokemon['Type 2'].nunique()

# 1 Scatterplots

sns.catplot(data = pokemon, x = 'Type 1', y = 'Attack', kind = 'strip', jitter = True)
sns.catplot(data = pokemon, x = 'Type 1', y = 'Attack', kind = 'swarm')


# 2 Distribution plots

sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'box', hue = 'Legendary')

sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'boxen')

sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'violin')

sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'violin', hue = 'Legendary', split = True)

# we can combine two plots
g = sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'violin', inner = None)
g = sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'swarm', ax = g.ax)
## this doesn't work

# one way it works is to use swarmplot instead of catplot
g = sns.catplot( data = pokemon, x = 'Generation', y='Attack', kind = 'violin')
sns.swarmplot( data = pokemon, x = 'Generation', y='Attack', ax = g.ax)




# 3 Statistical Estimation Chart

sns.catplot(data = pokemon, x = 'Generation', y = 'Attack', kind = 'bar')
sns.catplot(data = pokemon, x = 'Generation', kind = 'count')

sns.catplot(data = pokemon, x = 'Generation', y ='Attack', kind = 'point')













































