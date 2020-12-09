# S2S
Scripts to download S2S model forecasts from ECMWF's Web-API: 

https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets

1) Install the ECMWF key on your computer 
2) Install the ecmwf-api-client library (use Anaconda)

### getdata_hindcast_ECMWF.py

Downloading:

Lead time: 40 days (time step daily) 

Model: ECMWF control forecasts (model version CY46R1, https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1) 

Variable: Accumulated precipitation (228228)

Resolution: 1 x 1 grid


### run_getdata.sh

Downloading options for the reforecasts currently set from 01.07.2019-30.06.2020 and 20 years back in time
run the script as: ./run_getdata.sh <year-month> , e.g. 
  #### ./run_getdata.sh 2019-08 
  
  is downloading all the reforecasts (with 40 days lead time) in August from 1999-2019 and storing them in one grib file.
