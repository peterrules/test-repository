#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables

function math(){
    num1=3 
    num2=5
    num3=$((num1 + num2))
    echo $num3
}
math
math
math
math
