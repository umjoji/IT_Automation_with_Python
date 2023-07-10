#!/usr/bin/bash

# bash script to get the files with a particular pattern
# and saves them in a seperate file

search_pattern=$1
search_path=$2
destination_file=$3
> ./$destination_file
for file in $(grep $search_pattern $search_path | cut -d' ' -f3); do
    if test -e $file; then
        echo $file >> $destination_file
    else
        echo "File not found"
    fi
done