#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
import os,sys
from datetime import datetime
server = ECMWFDataServer()
product = 'PRODUCT' # forecast
#datadir = '/cluster/work/users/sso102/S2S/hindcast/ECMWF/sfc/tp'
#dir = '/cluster/work/users/sso102/S2S/hindcast/ECMWF/sfc'

product = 'hindcast' # forecast
dirbase = '/cluster/work/users/sso102/S2S/'
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
        'step': '/'.join(['%i'%i for i in range(0,1104,24)]) 
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
 #   'tp',
 #   't2m',
 #   'sst',
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

            #tp_CY46R1_${d}_cf.grb
            if not os.path.isfile(target):
                dic = basedict.copy()
                for k,v in meta[filename].items():
                    dic[k] = v
                dic['date'] = d
                dic['type'] = prefix
                if ( product == 'hindcast' ):
                    dic['hdate'] = hdate
                    if prefix == 'pf':
                        dic['number'] = '1/2/3/4/5/6/7/8/9/10'
                if ( product == 'forecast' ):
                    if prefix == 'pf':
                        dic['number'] = '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50'
                dic['target'] = target
                
                print(dic)
                if server is not None:
                    server.retrieve(dic)
