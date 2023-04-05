#!/usr/bin/env python
# coding: utf-8

# Setting up the airbnb text user interface module

# this will separate different lines where appropriate
line_separator = "-" * 124


# function to get the user's name and welcome the user to use the software
def name_of_user():
    print("Please enter your name.")
    name = input()
    print(f"\n Welcome {name}!\n You are ready to use Nwanneka's COM728 software.\n")

# start function to display the appropriate start message at the beginning of the program
def start(msg=""):
    print(line_separator)
    output = f"program started: {msg}"
    print(f"{line_separator}\n{output}\n")
    

# end function to display the appropraiate message at the end of the operation
def end():
    print(f"\nOperation completed.\n{line_separator}\n")
    

# error function 
def error(msg=""):
    print(f"Error! {msg}\nPlease try again!\n")
    

# this function asks the user about choice of programme he wants to perform with respect to question a, b and c
def users_choice_of_program():
    print(f"{line_separator}\n")
    print("Enter A to perform tasks using the csv module.\n")
    print("Enter B query or analyse using the pandas module.\n")
    print("Enter C to visualize the Airbnb dataset using the matplotlib module.\n")
    print("Enter EXIT to quit")
    print(f"{line_separator}\n")
    users_choice = input().strip()
    users_choice = users_choice.upper()
    while users_choice not in ["A", "B", "C", "EXIT"]:
        print("Enter A, B, C or EXIT")
        users_choice = input().upper().strip()        
    return users_choice

    
#users_choice_of_program()    
def menu1():    
    print(f"{line_separator}\n")
    print("Enter 1 to retrieve a name of listing, host_name, description, host_location, and the date the host was created for an individual host by host_id.\n")
    print("Enter 2 to retrieve host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location.\n")
    print("Enter 3 to retrieve room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type.\n")
    print("Enter 4 retrieve specific columns of your choice related to an individual host by location.\n")
    print("Enter 0 to exit")
    print(f"{line_separator}\n")
    choice = int(input().strip())
    while choice not in [0,1,2,3,4]:
        print("Enter 1, 2, 3, 4 or 0")
        choice = int(input().strip())        
    return choice
    
def displays():
    display = menu1()
    if display == 1:
        print(f"Retrieving name of listing, host_name, description, host_location, and the date the host was created for an individual host by host_id.\n{line_separator}\n")
    elif display == 2:
        print(f"Retrieving host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location.\n{line_separator}\n")
    elif display == 3:
        print(f"Retrieving room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type.\n {line_separator}\n")
    elif display == 4:
        print(f"Retrieving specific columns of your choice related to an individual host by location.\n{line_separator}\n")
    else:
        print(f"Goodbye!{line_separator}\n")







