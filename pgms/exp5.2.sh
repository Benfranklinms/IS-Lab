#!/bin/bash

echo "enter username"
read username

while true; do
  if who | grep -q "^$username\b"; then
    echo "user $username logged in"
    break
  else
    echo "try after some time"
    sleep 30
  fi
done