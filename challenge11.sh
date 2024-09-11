#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

read -p "Hello, how are you today?" input
case $input in

  good)
    echo "I'm happy you're having a good day"
    ;;

  bad)
    echo "Sorry you're having a bad day"
    ;;


  *)
    echo "Input invalid, please try again"
    ;;
esac

