#!/usr/bin/env python
# coding: utf-8

# importing modules
import os
import airbnb_tui

sep = "."*124

# function to get file path from the user
def get_file_path():
    path = "Data/"
    print("Enter the name of the dataset you want to load (with no file extension): ")
    file_path = input()
    # keep asking the user to input the correct file path until it is correct
    while file_path != "Airbnb_UK_2022.csv":
        airbnb_tui.error("File path not found.")
        file_path = input()
    airbnb_file_path = os.path.join(path,file_path)
    return (airbnb_file_path)


#tui.start("loading the airbnb dataset")
            
           
def get_by_host_id(airbnb_data):
    # ask for user input
    host_id = input("Enter the host id: ").strip()
            
    # Loop through each row in the CSV file
    for row in airbnb_data:
        # Check if the value in the 'host_id' column is equal to the user inputted host_id'
        if host_id == row[0]:
            # selected the appropriate columns based on the given host_id
            name_of_listing = row[1]
            host_name = row[3]
            description = row[2]
            host_location = row[5]
            host_since = row[4]
                    
            # display the information to the user based on host id
    print(f"{sep}\nThe details of Host {host_id} are:\n")
    print(f"{sep}\nThe name of listing is: {name_of_listing}\n")
    print(f"{sep}\nThe host name is : {host_name}\n")
    print(f"{sep}\nThe date created by host: {host_since}\n")
    print(f"{sep}\nThe host location is: {host_location}\n")
    print(f"{sep}\nThe description is: {description}.\n{sep}")


def get_by_location(airbnb_data):
    # get location from user
    print("Enter a location")
    location = input().capitalize()
    print(f"You have selected {location} as your location.")
    print(f"The host name, property type, price mainimum and maximum nights for listings in {location} are listed below\n{sep}\n")
    print(f"| {'host_id':<10} | {'host_name':<20} | {'property_type':<10} | {'price':<10} | {'maximum_nights':<14} | {'minimum_nights':<10}|")
     
    # Display the rows
    for row in airbnb_data:
        if location == row[5]:
            host_id = row[0]
            host_name = row[3]
            property_type = row[13]
            price = row[20]
            maximum_nights = row[22]
            minimum_nights = row[21]
            print(sep)
            print(f"| {host_id:<10} | {host_name:<20} | {property_type:<13} | {price:<10} | {maximum_nights:<14} | {minimum_nights:<14}|")
            
def get_by_property_type(airbnb_data):
    # get property type from the user
    print("Enter a property type.")
    property_type = input().lower().strip()
            
    print(f"You have selected {property_type} as the type of property you want to retrieve.\n")
    print(f"The room type, property type, accomodates, bathrooms, bedroom and beds for listings of {property_type} are listed below\n{sep}\n")
    print(f"| {'property_type':<11} | {'room_type':<13} | {'accomodates':<11} | {'bathrooms':<16} | {'bedroom':<10} | {'beds':<10}|")
     
    # Display the rows
    for row in airbnb_data:
        # select the appropriate columns based on the given host_id
        if property_type == row[13]:
            property_type = row[13]
            room_type = row[14]
            accomodates = row[15]
            bathrooms = row[16]
            bedrooms = row[17]
            beds = row[18]
            print(sep)
            print(f"| {property_type:<14} | {room_type:<12} | {accomodates:<11} | {bathrooms:<16} | {bedrooms:<10} | {beds:<10} |")    

    

