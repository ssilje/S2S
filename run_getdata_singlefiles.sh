#!/bin/bash

# get argument                                                                                                                                                                                                                                                                                                                                         
datein=${1}
year=$(echo ${datein} | cut -d'-' -f1)
month=$(echo ${datein} | cut -d'-' -f2)
echo ${datein}

run_dir='/cluster/home/sso102/S2S/scripts/S2S'
savedir='/cluster/work/users/sso102/S2S/ECMWF/TOT_PR_singlefiles'


if [ ! -d ${run_dir}/jobs ]
then
    mkdir ${run_dir}/jobs
else
    rm -r ${run_dir}/jobs
    mkdir ${run_dir}/jobs
fi

if [ ! -d ${savedir} ]
then
    mkdir ${savedir}

fi

# Reforecasts with the model version CY46R1: https://confluence.ecmwf.int/display/S2S/ECMWF+Model+Description+CY46R1
# Data time of first forecast run:   11 June 2019
# Here the dates for reforecasts from 01.07.2019-30.06.2020 and 20 years back in time

DATE='2019-07-01 2019-07-04 2019-07-08 2019-07-11 2019-07-15 2019-07-18 2019-07-22 2019-07-25 2019-07-29 
        2019-08-01 2019-08-05 2019-08-08 2019-08-12 2019-08-15 2019-08-19 2019-08-22 2019-08-26 2019-08-29 
        2019-09-02 2019-09-05 2019-09-09 2019-09-12 2019-09-16 2019-09-19 2019-09-23 2019-09-26 2019-09-30 
        2019-10-03 2019-10-07 2019-10-10 2019-10-14 2019-10-17 2019-10-21 2019-10-24 2019-10-28 2019-10-31 
        2019-11-04 2019-11-07 2019-11-11 2019-11-14 2019-11-18 2019-11-21 2019-11-25 2019-11-28 
        2019-12-02 2019-12-05 2019-12-09 2019-12-12 2019-12-16 2019-12-19 2019-12-23 2019-12-26 2019-12-30 
        2020-01-02 2020-01-06 2020-01-09 2020-01-13 2020-01-16 2020-01-20 2020-01-23 2020-01-27 2020-01-30 
        2020-02-03 2020-02-06 2020-02-10 2020-02-13 2020-02-17 2020-02-20 2020-02-24 2020-02-27 
        2020-03-02 2020-03-05 2020-03-09 2020-03-12 2020-03-16 2020-03-19 2020-03-23 2020-03-26 2020-03-30 
        2020-04-02 2020-04-06 2020-04-09 2020-04-13 2020-04-16 2020-04-20 2020-04-23 2020-04-27 2020-04-30 
        2020-05-04 2020-05-07 2020-05-11 2020-05-14 2020-05-18 2020-05-21 2020-05-25 2020-05-28 
        2020-06-01 2020-06-04 2020-06-08 2020-06-11 2020-06-15 2020-06-18 2020-06-22 2020-06-25 2020-06-29'



for d in ${DATE}; do 
    y=$(echo ${d} | cut -d'-' -f1)
    
    
    m=$(echo ${d} | cut -d'-' -f2)
    day=$(echo ${d} | cut -d'-' -f3)
    if [ $y == $year ] && [ $m == $month ]
        then
        HC = 0
        while [ HC -le 20  ] # 20 years hindcast
        do
        yHC=`expr ${y} - $HC`
        echo $yHC
        echo $d
        cp $run_dir/getdata_hindcast_ECMWF_singlefiles.py $run_dir/jobs/getdata_hindcast_ECMWF${d}.py 
        sed -i "s/2018-01-01/$d/g" $run_dir/jobs/getdata_hindcast_ECMWF${d}.py 
        sed -i "s/yy = 0/yy = ${HC}/g" $run_dir/jobs/getdata_hindcast_ECMWF${d}.py 
        
        HC=`expr ${HC} + 1`
            if [ ! -f ${savedir}/tp_cf_${d}_hc_.grb ] tp_cf_2019-07-15_hc_2000-07-15.nc
                then
                echo "running python $run_dir/jobs/getdata_hindcast_ECMWF${d}.py"
  
                python $run_dir/jobs/getdata_hindcast_ECMWF${d}.py

                wait
                echo "done..."
                else 
                echo " File already downloded "
            fi  
      else 
      echo "Date does not match the available date"
     fi
done
