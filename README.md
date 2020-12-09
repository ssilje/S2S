# S2S
Scripts to download S2S model forecasts from ECMWF's Web-API: 
https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets

1) Install the ECMWF key on your computer 
2) Install the ecmwf-api-client library (I used Anaconda)


getdata_hindcast_ECMWF.py

Downloading:
Lead time: 40 days (time step daily) 
Model: ECMWF control forecasts (model version CY46R1, https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1) 
Variable: Accumulated precipitation 
Resolution: 1 x 1 grid


run_getdata.sh

