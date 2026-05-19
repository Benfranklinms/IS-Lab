#!/bin/bash

read -p "Enter filename: " file

if [ ! -f hash.txt ]; then
    shasum -a 256 "$file" > hash.txt
    echo "Hash stored"
else
    shasum -a 256 -c hash.txt
fi