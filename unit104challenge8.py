# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line: 
counting = 0
while {True}:
    time.sleep(1)
    counting = counting + 1
    print (f"{counting}, mississippi")
    if counting == 5:
        print ("ready or not, here i come!")
        break