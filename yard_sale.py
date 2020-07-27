#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:29:23 2020

@author: John C Wang
"""
import numpy as np
#import time
from matplotlib import pyplot as plt

n = 100 #population 
initial_wealth = 200
max_iteration = 10000
# the most one can gain/lose from a trade is 0.2 * poorer_wealth
max_trade_delta = 0.2

maximum_wealth = initial_wealth
iteration = 0
 
wealth = initial_wealth * np.ones([n,1])
wealth = np.hstack((np.arange(len(wealth)).reshape([len(wealth),1]),wealth))
wealth.dtype = np.dtype([('idx',float),('money',float)])

fig, ax = plt.subplots()
rects = ax.bar(x = wealth['idx'].reshape([1,n])[0], height= wealth['money'].reshape([1,n])[0])
ax.set_ylabel('wealth')
iteration_label = ax.text(n-20, maximum_wealth-10, f'iteration: {iteration}')

def Iterate():
    i = np.random.randint(0,n-1)
    j = i
    while i == j:
        j = np.random.randint(0,n-1)
    trade_delta_ratio = max_trade_delta * np.random.randint(0,100)/100
    w = wealth['money']
    trade_delta = w[i][0] if w[i][0] < w[j][0] else w[j][0]
    trade_delta *= trade_delta_ratio
    trade_delta *= 1 if np.random.randint(0,1) else -1
    w[i][0] += trade_delta
    w[j][0] -= trade_delta
    global maximum_wealth 
    maximum_wealth = max(w[i][0], w[j][0], maximum_wealth)
    UpdatePlot(i,j)
    
def UpdatePlot(i=-1,j=-1):
    if i == -1 or j==-1 :
        for rect, h in zip(rects, wealth['money']):
            rect.set_height(h[0])
    else:
        rects[i].set_height(wealth['money'][i][0])
        rects[j].set_height(wealth['money'][j][0])

    fig.canvas.draw()
    plt.pause(0.001)
    ax.set_ylim(0, maximum_wealth)
    iteration_label.set_position((n-20, maximum_wealth-10))
    iteration_label.set_text(f'iteration: {iteration}')
    
if __name__ == '__main__':
    UpdatePlot()
    while(iteration < max_iteration):
        Iterate()
        iteration += 1

# wealth_distribution_figure = plt.figure(1)
# plt.bar(x = wealth[:,0], height=wealth[:,1])
# wealth_distribution_figure.show()