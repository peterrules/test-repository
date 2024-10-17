# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.




from urllib import response
import requests

#"get" is used to request data from a specified resource
#"post" is used to send data to a create or update a resource
#"put" is used for the same purpose as "post", except "put" always produces the same result
#"delete" is used to delete the specified resource
#"head" is the same as "get", but without the response body
#"patch" is used to modify the specified resource
#"options" is used to describe the communication options of the specified resource


url= (input("Enter the URL you would like to use ")) 

while True:
    options = input("Select your HTTP methods: Get, Post, Put, Delete , Head, Patch, Options\n") 
    if options == ("get"):
        break     
    elif options == ("post"):
        break          
    elif options == ("put"):
        break  
    elif options == ("delete"):
        break    
    elif options == ("head"):
        break 
    elif options == ("patch"):
        break  
    elif options == ("options"):
        break  
    else:
        print("Invalid, please try again")

print(f"You are about to use '{options}' on this url '{url}'")

yesandno = input("Confirm? (y/n): ")
while {True}:
    
    if yesandno == "y":
        print("Continuing...")
        break
    elif yesandno == "n":
        print("Cancelling")
        break
    else:
        print("invalid")


 
if options == ("get"): 
    response = requests.get(url)
elif options == ("post"): 
    response = requests.post(url)
elif options == ("put"):
    response = requests.put(url)
elif options == ("delete"): 
    response = requests.delete(url)
elif options == ("head"):
    response = requests.head(url)
elif options == ("patch"):
    response = requests.patch(url)
elif options == ("options"): 
    response = requests.options(url)  

print(response.status_code)   
if response.status_code == 200:
    print("success!")
elif response.status_code == 405:
    print("error! request denied!")
elif response.status_code == 404:
    print("error, not found")
else:
    print("error")

print(response.headers)
#print(response) 
#response = requests.get(url)
#print(response.headers)