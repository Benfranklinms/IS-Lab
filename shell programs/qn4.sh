#! /bin/bash

read -p "Enter file name to moniter : " file

if [ ! -f "$file" ]; then
  echo "file not found"
  exit 1
fi

hashfile="$file.hash"

if [ ! -f "$file" ]; then
  sha256sum "$file" > "$hashfile"
  echo "hash created"
else
  sha256sum -c "$hashfile"
fi