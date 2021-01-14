# S2S
Scripts to download S2S model forecasts from ECMWF's Web-API: 

https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets

1) Install the ECMWF key on your computer 
2) Install the ecmwf-api-client library (use Anaconda)


----------------------------------------------------------------------------------------------------------------------------------
### getdata_CY46R1_ECMWF.py

Downloading:

Lead time: 46 days (time step daily) 

Model: ECMWF control forecasts (model version CY46R1, https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1) 

Variable: 
Accumulated precipitation:(228228)
t2m (167)  
sst (34)

Resolution: 1 x 1 grid


### run_getdata_CY46R1_ECMWF.sh

Downloading options for the reforecasts and forecast currently set from 01.07.2019-30.06.2020 and 20 years back in time
Need to set in the script: 
## var='tp' # sst, t2m, tp
## ftype='pf' #cf, pf
## product='forecast' # forecast, hindcast

run the script as: ./run_getdata_CY46R1_ECMWF.sh

  
  
