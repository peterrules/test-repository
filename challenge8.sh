#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

#Enter an infinite loop

while true
do 
    read -p "enter an input" input

if [ "$input" -eq 1 ]; then
    echo "hello world"
elif [ "$input" -eq 2 ]; then
   ping "google.com"

elif [ "$input" -eq 3 ]; then
   ifconfig
else 
    echo "invalid entry"
fi
done