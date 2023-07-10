#!/usr/bin/bash

old_filename=$1
old_file_extension=$2
new_file_extension=$3
for file in $old_filename; do
    name=$(basename "$file" $old_file_extension)
    mv "$file" "$name$new_file_extension"
done
