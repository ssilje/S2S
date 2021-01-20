# S2S
Scripts to download S2S model forecasts from ECMWF's Web-API: 

https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets

1) Install the ECMWF key on your computer 
2) Install the ecmwf-api-client library 


----------------------------------------------------------------------------------------------------------------------------------
### getdata_CY46R1_ECMWF.py

Downloading:

Lead time: 46 days (time step daily) 

Model: ECMWF control forecasts (model version CY46R1, https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1) 

Variable: 
- Accumulated precipitation(228228)
- t2m (167)  
- sst (34)

Resolution: 1 x 1 grid


### run_getdata_CY46R1_ECMWF.sh

Downloading options for the reforecasts and forecast currently set from 01.07.2019-30.06.2020 and 20 years back in time
Need to set in the script: 
### var='tp' # sst, t2m, tp
### ftype='pf' #cf, pf
### product='forecast' # forecast, hindcast

run the script as: ./run_getdata_CY46R1_ECMWF.sh


------------------------------------------------------------------------------------------------------------
#### The data downloaded can be used by CONFER and CLIMATE FUTURES

To access the data form  NIRD: /nird/projects/NS9853K/DATA/S2S 

To access from FRAM: /nird/projects/nird/NS9853K/DATA/S2S 

Creation date: 12.01.2021
contact: Silje Lund Sørland, ssor@norceresearch.no

### Information:

S2S: sub-seasonal to seasonal prediction project. Web: https://confluence.ecmwf.int/display/S2S
It is a WWRP/THORPEX-WCRP joint research project established to improve forecast skill and understanding on the sub-seasonal to seasonal time scale

The S2S data are downloaded from ECMWF's MARS archive: https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets
 
The data is downloaded on a 1x1 degree grid. Note that the different models have different resolutions (and the model have different resolution for different lead-times).

The data is donwloaded as hindcast and forecast, with the associated ensemble members. 

The data structure: 

#### S2S/hindcast/_modeling-center_/_type-files_/_variable-name_/

where (add the information when new models, variables are included)
- _modeling-center_: ECMWF
- _type-files_: sfc, pl
- _variable-name_: tp (accumulated), t2m

Information about the different model is given here: https://confluence.ecmwf.int/display/S2S/Models

Information about the specific models that is downloaded: 

#### ECMWF: 
- Model version CY46R1, https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1)
- Data time of first forecast run:   11 June 2019
- First forecast downloaed: 2019-07-01 and one year (2020-06-29)
- Hindcast: 20 years
- Ensemble members: 
  - forecast 50 + 1
  - hindcast 10 + 1
  
  
