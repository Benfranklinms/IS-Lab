#! /bin/bash

read -p "Enter file name : " file

if [ -f "$file" ]; then
  chmod a-x "$file"
  echo "Permission removed"
else
  echo "File not found"
fi