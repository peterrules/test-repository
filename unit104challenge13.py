# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import math

math

years = 90 - age
months = years * 12
weeks = years * 52
days = years * 365
final_age = 90



print(f"You have {months} month(s), {weeks} weeks, and {days} day(s) until you turn {final_age}.")