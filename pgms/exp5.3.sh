#!/bin/bash

echo "enter filename"
read file

if [ -f "$file" ]; then
  chmod -x "$file"
  echo "permissions of $file has been removed"
else
  echo "file $file not found"
fi