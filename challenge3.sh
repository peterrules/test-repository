#!/bin/bash
# Condtinal Statment 
# This ops challenges is about conditinal stamtment of if else statments and how they work
# We are going to take a varibale with the number and have the computer tell us if its greater than 5 less than 5 or equals 5

number=5
if [ "$number" -gt 5 ]; then
    echo "$number is greater than 5."
elif [ "$number" -lt 5 ]; then
    echo "$number is less than 5."
else 
    echo "$number is exactly 5."
fi