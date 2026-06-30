#!/usr/bin/env bash

shopt -s nullglob

for dir in Level\ *; do
    if [ -d "$dir" ]; then
        num="${dir#Level }"

        if [[ "$num" =~ ^[0-9]+$ ]]; then
            new_num=$(printf "%03d" "$((10#$num))")
            new_dir="Level $new_num"

            if [ "$dir" != "$new_dir" ]; then
                if [ -e "$new_dir" ]; then
                    echo "Skipped: $new_dir already exists"
                else
                    mv "$dir" "$new_dir"
                    echo "Renamed: $dir -> $new_dir"
                fi
            fi
        fi
    fi
done