#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:01:59 2015

@author: Jingkang
"""

import matplotlib.pyplot as plt
    
def swiggle(seismic, time, isFilled = True, fillColor = 'blue'):
    if seismic.ndim == 1:
        plt.plot(seismic,time,color=fillColor,alpha=.5)
        plt.fill_betweenx(time, 0, seismic, seismic>0, color='blue', alpha=.25)
        plt.gca().invert_yaxis()

    else:
        nTimes, nGathers = seismic.shape
        for iGather in range(nGathers):
            # print(iGather)
            # plt.figure(1)
            # plt.figure(figsize=(8,6))
            plt.axes([0.1+0.18*iGather,0.1,.1,.8])
            # plt.plot(seismic[:,iGather]+iGather,time,color='blue',alpha=.5)
            # plt.fill_betweenx(time, iGather, seismic[:,iGather]+iGather, seismic[:,iGather]>0, color='blue', alpha=.25)
            plt.plot(seismic[:,iGather],time,color=fillColor,alpha=.5)
            plt.fill_betweenx(time, 0, seismic[:,iGather], seismic[:,iGather]>0, color=fillColor, alpha=.25)
            plt.gca().invert_yaxis()
 
        
    # plt.plot(seismic(:,0),time)
    # plt.plot(seismic(:,1) * 3,time)
    # plt.gca().invert_yaxis()
    # plt.show()