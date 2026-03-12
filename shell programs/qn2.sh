#! /bin/bash

read -p "Enter a username : " username

while true; do
  if who | grep -q "^username\b"; then
    echo "User $username has logged in"
    break
  else
    echo "try after some time"
    sleep 30
  fi
done