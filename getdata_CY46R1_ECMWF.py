#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
import os,sys
import pandas as pd
from datetime import datetime
server = ECMWFDataServer()
product = 'hindcast' # forecast, hincast
dirbase = '/nird/projects/NS9853K/DATA/S2S'
dir = '%s/%s/%s/'%(dirbase,product,'/ECMWF/sfc')
forcastcycle = 'CY46R1'

basedict = {
    'class': 's2',
    'dataset': 's2s',
    'expver': 'prod',
    'model': 'glob',
    'origin': 'ecmf',
    'stream': 'STREAM',
    'time': '00:00:00'
}

l = range(0,1128,24)
paired = ['-'.join([str(v) for v in l[i:i + 2]]) for i in range(len(l))]
final = '/'.join(paired[0:-1])

meta = {
    'tp': {
        'param': '228228',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join(['%i'%i for i in range(0,1128,24)]) 
    },
    
     't2m': {
        'param': '167',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join([final]) 
    },
    
     'sst': {
        'param': '34',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join([final]) 
    },
    
     'u10': {
        'param': '165',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join(['%i'%i for i in range(0,1128,24)]) 
    },
    
    'v10': {
        'param': '166',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join(['%i'%i for i in range(0,1128,24)]) 
    }
}

dates_monday = pd.date_range("20190701", periods=52, freq="7D") # forecats start Monday
dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecats start Thursday
   
    
   # Program start
for filename in (
    'tp',
):
    for dates in dates_monday:
        d = dates.strftime('%Y-%m-%d')
        refyear = int(d[:4])
        prefix = 'ftype'
        datadir = '%s/%s'%(dir,filename)
        if not os.path.exists(datadir)  :
            os.makedirs(datadir)
        hdate = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])
        target = '%s/%s_%s_%s_%s_%s.grb'%(datadir,filename,forcastcycle,d,prefix,hdate)
        if not os.path.isfile(target):
           dic = basedict.copy()
           for k,v in meta[filename].items():
               dic[k] = v
           dic['date'] = d
           dic['type'] = prefix
           if ( product == 'hindcast' ):
               dic['hdate'] = hdate
               if prefix == 'pf':
                   ll = range(1,11,1) # 10 members
                   paired = '/'.join(['/'.join([str(v) for v in ll[i:i + 1]]) for i in range(len(ll))])
                   dic['number'] =  '%s' %(paired)
           if ( product == 'forecast' ):
               if prefix == 'pf':
                   ll = range(1,51,1) # 50 members
                   paired = '/'.join(['/'.join([str(v) for v in ll[i:i + 1]]) for i in range(len(ll))])
                   dic['number'] =  '%s' %(paired)
           dic['target'] = target    
           print(dic)
           if server is not None:
               server.retrieve(dic)
