#!/bin/bash

index=0
# for file in pos/* 
while [[ $index -le 4 ]]
do 
    "$(mkdir allSamples/info$((index)))"
    "$(opencv_createsamples -img start_pos/Just_Logo/pos$((index)).png -bg bg.txt -bgcolor 40 -info allSamples/info$((index))/info$((index)).lst -pngoutput allSamples/info$((index)) -maxxangle 1.1 -maxyangle 1.1 -maxzangle 0.5 -num 3030)"
    index=$((index+1))
done 
