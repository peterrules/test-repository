#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Step 1: Take a user input string. Presumably the string is a domain name such as Google.com.
read -p "enter a domain name" domain
echo $domain
# Step 2: Run whois against a user input string.
function dowhois () {
    { 
        whois $domain
        
    } >> "test.txt"
 
}
dowhois
# Step 3: Run dig against the user input string.
function dodig () {
    { 
        dig $domain
        
    } >> "dig.txt"
 
}
dodig
# Step 4: Run host against the user input string. 
function dohost () {
    { 
        host $domain
        
    } >> "host.txt"
 
}
dohost
# Step 5: Run nslookup against the user input string.
function donslookup () {
    { 
        nslookup $domain
        
    } >> "nslookup.txt"
 
}
donslookup
# Step 6:Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.

