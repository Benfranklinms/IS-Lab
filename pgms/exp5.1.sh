#!/bin/bash

count=1

for file in *; do
  if [ -f "$file" ]; then
    date=$(stat -f %Sm "$file")
    echo "$count. $file - $date"
    ((count++))
  fi
done
