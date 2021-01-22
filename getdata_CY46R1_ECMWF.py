#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
import os,sys
from datetime import datetime
server = ECMWFDataServer()
product = 'PRODUCT' # forecast
dirbase = 'BASEDIR'
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

l24 = range(0,1128,24)
paired24 = ['-'.join([str(v) for v in l24[i:i + 2]]) for i in range(len(l24))]
final24 = '/'.join(paired24[0:-1])

# wind components are Instantaneous values. Need to confirm the time resilution. For now I donwload the highest temporal resolution to make a daily mean.Should I do this for t2s,sst also?
l6 = range(0,1128,6)
paired6 = ['-'.join([str(v) for v in l6[i:i + 2]]) for i in range(len(l6))]
final6 = '/'.join(paired6[0:-1])

meta = {
    'tp': {
        'param': '228228',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join(['%i'%i for i in range(0,1104,24)]) 
    },
    
     't2m': {
        'param': '167',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join([final24]) 
    },
    
     'sst': {
        'param': '34',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join([final24]) 
    },
    
     'u10': {
        'param': '165',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join([final6]) 
    },
    
    'v10': {
        'param': '166',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join([final6]) 
    }
}

def getdatesformonth(month):
    a = (
       '2018-01-01',
    )
    for b in a:
        dates = b.split('/')
        if datetime.strptime(dates[0],'%Y-%m-%d').month == month:
            return dates
    return []   
    
   # Program start
for filename in (
    'VAR',
):
    for month in range(1,13):

        dates = getdatesformonth(month)

        for d in dates:
            refyear = int(d[:4])
            prefix = 'ftype'
            datadir = '%s/%s'%(dir,filename)
            if not os.path.exists(datadir)  :
                os.makedirs(datadir)
            hdate = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])
            target = '%s/%s_%s_%s_%s.grb'%(datadir,filename,forcastcycle,d,prefix)

        
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
