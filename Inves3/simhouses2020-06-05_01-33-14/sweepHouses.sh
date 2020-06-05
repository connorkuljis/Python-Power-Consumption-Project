#!/bin/bash

echo
echo "####### HOUSE SIMULATION SWEEP #######"

sim_dir=simhouses`date "+%Y-%m-%d_%H-%M-%S"`

mkdir $sim_dir
cp housesimulation.py $sim_dir
cp sweepHouses.sh $sim_dir
# cd $sim_dir

echo $sim_dir

sName=$1
sPostcode=$2

# mansions
lowMM=$3    
hiMM=$4     
stepMM=$5   

# family
lowFF=$6    
hiFF=$7     
stepFF=$8   

# flats
lowFL=$9   
hiFL=${10}  
stepFL=${11}

# studios
lowST=${12} 
hiST=${13}  
stepST=${14}

echo
echo "Parameters are: "
echo "mansions: " $lowMM $hiMM $stepMM
echo "family homes: " $lowFF $hiFF $stepFF
echo "flats: " $lowFL $hiFL $stepFL
echo "studios: " $lowST $hiST $stepST
echo

echo "Running experiments"

for mm in `seq $lowMM $stepMM $hiMM`;
do
    for ff in `seq $lowFF $stepFF $hiFF`;
    do
	for fl in `seq $lowFL $stepFL $hiFL`;
	do
	    for st in `seq $lowST $stepST $hiST`;
	    do
		echo "Experiment: " $mm $ff $fl $st
		outfile="REPORT_MM"$mm"_FF"$ff"_FL"$fl"_ST"$st".txt"
		python3 housesimulation.py $1 $2 $mm $ff $fl $st > $outfile
	    done
	done
    done
done

