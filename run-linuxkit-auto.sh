#!/bin/bash

# usage: ./run-linuxkit-auto.sh [container-name] [start-num-iterations] [end-num-iterations]
# usage example: ./run-linuxkit-auto.sh ubuntu 10 20

counter=1
output="gcda-data-$1"
data_output_path="/home/detectivelyw/Downloads/"
data_output="$data_output_path$output.tar.gz"
data_store_path="/home/detectivelyw/Documents/projects/tracks/linuxkit-auto-experiment/data/"
mem="4096"
cmd="sudo linuxkit run $1-gcov -mem $mem"

cd $KITSRC

echo "First arg: $1"
echo "Second arg: $2"
echo "Third arg: $3"
num_iterations=$(($3-$2+1))
num_current=$2
echo "We would like to run $1 container in LinuxKit for $num_iterations iterations"

while [ $counter -le $num_iterations ]
do
    echo "running iteration number [$counter/$num_iterations] ..."
    echo "$cmd"
    eval $cmd
    echo "iteration number [$counter/$num_iterations]: LinuxKit run has finished!"

    output_data_file_name="$output-$num_current.tar.gz"
    output_path="$data_store_path$output_data_file_name"

    if [ -f "$data_output" ]
    then
        echo "now copying output data from $data_output to $output_path ..."
        copy_cmd="mv $data_output $output_path"
        echo $copy_cmd
        eval $copy_cmd
        echo "data copying has finished successfully!"
    else
        echo "$data_output not found."
        echo "***Warning*** iteration $counter failed to produce the correct output data!"
    fi
    echo "iteration number [$counter/$num_iterations] has finished successfully!"
    ((counter++))
    ((num_current++))
done
