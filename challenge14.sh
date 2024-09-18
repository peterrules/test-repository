#!/bin/bash
# Create a script that ask the user for a number between 1 and 10.  Have the script tell the user if there
# number is greater than 5, less than 5, or equal to 5.  Please use an if/else or elif statement to make this happen.  
# Also put the if/else statemnt inside a function.
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)
#Here are some helpful commands to make this happen.

number=5

read -p "enter a number between 1 and 10: " input
function calculations() {

    if [[ "$input" -le "$number" && "$input" -gt 0 && "$input" -ne "$number" ]]; then
    echo "$input is less than $number!"
    elif [[ "$input" -gt "$number" && "$input" -le 10 && "$input" -ne "$number" ]]; then
    echo "$input is greater than $number!"

    elif [ "$input" = "$number" ]; then
    echo "$input is equal to $number!"

    else 
    echo "invalid! try again!"
    fi
}
calculations