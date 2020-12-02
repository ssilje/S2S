#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:58:17 2020

@author: ssilje
"""
from ecmwfapi import ECMWFDataServer
import os,sys
from datetime import datetime





datadir = 'DATA'
#server = None
server = ECMWFDataServer() 
# what is used in the generated script

basedict = {
    'class': 's2',
    'format': 'netcdf',
    'dataset': 's2s',
    'expver': 'prod',
    'model': 'glob',
    'origin': 'ecmf',
    'stream': 'enfh',
    'time': '00:00:00'
}

meta = {
    'tp': {
        'param': '228228',
        'area': '10/-180/80/180',
        'grid': '0.5/0.5',
        'levtype': 'sfc',
        'step': '/'.join(['%i'%i for i in range(0,721,24)])
    }
    
}

def getdatesformonth(month):
    a = (
       '2020-08-03/2020-08-06/2020-08-10/2020-08-13/2020-08-17/2020-08-20/2020-08-24/2020-08-27/2020-08-31',
    )
    for b in a:
        dates = b.split('/')
        if datetime.strptime(dates[0],'%Y-%m-%d').month == month:
            return dates
    return []

#https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1
#Ensemble identifier code:    CY46R1
#Short Description:    Global ensemble system that simulates initial uncertainties using singular vectors and ensemble of data assimilation and model uncertainties due to physical parameterizations using a stochastic scheme. based on 51 members, runs twice a week (Monday and Thursday at 00Z) up to day 46.
#Research or operational: Operational
#Data time of first forecast run:   11 June 2019

for filename in (
    'tp',
    #'sst',
):

    #for month in [2,3,4,5,9,10,11,12]:
    #for month in [8]:
    for month in range(1,13):
    #for month in [1]:

        dates = getdatesformonth(month)

        for d in dates:

            print(d)
            refyear = int(d[:4])
            hdate = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])

            for prefix in (
                'cf',
           #     'pf',
            ):

                target = '%s/%s_%s_%s.nc'%(datadir,filename,prefix,d)
                if not os.path.isfile(target):
                    dic = basedict.copy()
                    for k,v in meta[filename].items():
                        dic[k] = v
                    dic['date'] = d
                    dic['type'] = prefix
                    dic['hdate'] = hdate
                    dic['target'] = target
                    if prefix == 'pf':
                        dic['number'] = '1/2/3/4/5/6/7/8/9/10'
                    print(dic)
                    if server is not None:
                        server.retrieve(dic)



