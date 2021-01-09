#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
import os,sys
from datetime import datetime
server = ECMWFDataServer()
datadir = '/cluster/work/users/sso102/S2S/hindcast/ECMWF/sfc/tp'

basedict = {
    'class': 's2',
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
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join(['%i'%i for i in range(0,1104,24)]) # 40 days forecast
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
    'tp',
    #'sst',
):
    for month in range(1,13):

        dates = getdatesformonth(month)

        for d in dates:
            refyear = int(d[:4])
            prefix = 'cf'
            hdate = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])
            #target = '%s/%s_%s_%s_%s_%s.grb'%(datadir,filename,prefix,d,'hc', hdate)
            target = '%s/%s_%s_%s_%s.grb'%(datadir,filename,'CY46R1',d,prefix)

            #tp_CY46R1_${d}_cf.grb
            if not os.path.isfile(target):
                dic = basedict.copy()
                for k,v in meta[filename].items():
                    dic[k] = v
                dic['date'] = d
                dic['type'] = prefix
                dic['hdate'] = hdate
                dic['target'] = target
                print(dic)
                if server is not None:
                    server.retrieve(dic)
