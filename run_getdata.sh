#!/bin/bash

DATE=
run_dir='/cluster/home/sso102/S2S/scripts/S2S'


sed -i "s/2018-01-01/$DATE/g" $run_dir/$param$min/getdata_hindcast_ECMWF.py 
