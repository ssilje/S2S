from ecmwfapi import ECMWFDataServer
import os,sys
from datetime import datetime

datadir = '/Volumes/LaCie/Data/s2s/gha'
server = None
#server = ECMWFDataServer()

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
        'area': '25/21/-28/52',
        'grid': '1/1',
        'levtype': 'sfc',
        'step': '/'.join(['%i'%i for i in range(0,721,24)])
    },
    'sst': {
        'param': '34',
        'area': '-30/-180/30/180',
        'grid': '1.5/1.5',
        'levtype': 'sfc',
        'step': '0-24/24-48/48-72/72-96/96-120/120-144/144-168/168-192/192-216/216-240/240-264/264-288/288-312/312-336/336-360/360-384/384-408/408-432/432-456/456-480/480-504/504-528/528-552/552-576/576-600/600-624/624-648/648-672/672-696/696-720'
    }
}

def getdatesformonth(month):
    a = (
        #'2019-07-01/2019-07-04/2019-07-08/2019-07-11/2019-07-15/2019-07-18/2019-07-22/2019-07-25/2019-07-29',
        #'2019-08-01/2019-08-05/2019-08-08/2019-08-12/2019-08-15/2019-08-19/2019-08-22/2019-08-26/2019-08-29',
        '2019-09-02/2019-09-05/2019-09-09/2019-09-12/2019-09-16/2019-09-19/2019-09-23/2019-09-26/2019-09-30',
        '2019-10-03/2019-10-07/2019-10-10/2019-10-14/2019-10-17/2019-10-21/2019-10-24/2019-10-28/2019-10-31',
        '2019-11-04/2019-11-07/2019-11-11/2019-11-14/2019-11-18/2019-11-21/2019-11-25/2019-11-28',
        '2019-12-02/2019-12-05/2019-12-09/2019-12-12/2019-12-16/2019-12-19/2019-12-23/2019-12-26/2019-12-30',
        '2020-01-02/2020-01-06/2020-01-09/2020-01-13/2020-01-16/2020-01-20/2020-01-23/2020-01-27/2020-01-30',
        '2020-02-03/2020-02-06/2020-02-10/2020-02-13/2020-02-17/2020-02-20/2020-02-24/2020-02-27',
        '2020-03-02/2020-03-05/2020-03-09/2020-03-12/2020-03-16/2020-03-19/2020-03-23/2020-03-26/2020-03-30',
        '2020-04-02/2020-04-06/2020-04-09/2020-04-13/2020-04-16/2020-04-20/2020-04-23/2020-04-27/2020-04-30',
        '2020-05-04/2020-05-07/2020-05-11/2020-05-14/2020-05-18/2020-05-21/2020-05-25/2020-05-28',
        '2020-06-01/2020-06-04/2020-06-08/2020-06-11/2020-06-15/2020-06-18/2020-06-22/2020-06-25/2020-06-29',
        '2020-07-02/2020-07-06/2020-07-09/2020-07-13/2020-07-16/2020-07-20/2020-07-23/2020-07-27/2020-07-30',
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
    #'tp',
    'sst',
):

    #for month in [2,3,4,5,9,10,11,12]:
    #for month in [8]:
    for month in range(1,13):

        dates = getdatesformonth(month)

        for d in dates:

            print(d)
            refyear = int(d[:4])
            hdate = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])

            for prefix in (
                'cf',
                'pf',
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

