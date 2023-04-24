# importing modules
import os
import airbnb_tui
import pandas as pd

# line separator
sep = "."*120

# function to get file path from the user
def get_file_path():
    path = "Data/"
    print("Enter the name of the dataset you want to load (Airbnb_UK_2022.csv): ")
    file_path = input()
    # keep asking the user to input the correct file path until it is correct
    while file_path != "Airbnb_UK_2022.csv":
        airbnb_tui.error("File path not found.")
        file_path = input()
    # join the file path
    airbnb_file_path = os.path.join(path,file_path)
    return (airbnb_file_path)

         
# function to get data from the Airbnb dataset using the host id           
def get_by_host_id(airbnb_data):
    while True:
        try:
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
            
            # display the information to the user based on host id
            print(f"{sep}\nThe details of \033[1mHost {host_id}\033[0m are:\n")
            print(f"{sep}\n\033[1mThe name of listing is:\033[0m {name_of_listing}\n")
            print(f"{sep}\n\033[1mThe host name is:\033[0m {host_name}\n")
            print(f"{sep}\n\033[1mThe date created by host:\033[0m {host_since}\n")
            print(f"{sep}\n\033[1mThe host location is:\033[0m {host_location}\n")
            print(f"{sep}\n\033[1mThe description is:\033[0m {description}.\n{sep}")
            break
        # except when the ID is not found because when it doesn't match the compiler moves on untill line 47 where it assumes you are 
        # calling a variable you haven't assigned.
        except UnboundLocalError:
            airbnb_tui.error("There is no host with the ID you entered!")
            break            

def get_by_location(airbnb_data):
    while True:
            # get location from user
            print("Enter a location")
            location = input().capitalize().strip()
            print(f"You have selected \033[1m{location}\033[0m as your location.")
            print(f"\nThe host name, property type, price mainimum and maximum nights for listings in {location} are listed below:\n{sep}\n")
            print(f"| \033[1m{'host_id':<10}\033[0m | \033[1m{'host_name':<25}\033[0m | \033[1m{'property_type':<18}\033[0m | \033[1m{'price':<10}\033[0m | \033[1m{'maximum_nights':<14}\033[0m | \033[1m{'minimum_nights':<10}\033[0m |\n{sep}")

            # Display the appropriate columns and rows
            location_found = False
            for row in airbnb_data:
                if location == row[5]:
                    host_id = row[0]
                    host_name = row[3]
                    property_type = row[13]
                    price = row[20]
                    maximum_nights = row[22]
                    minimum_nights = row[21]        
                    print(f"| {host_id:<10} | {host_name:<25} | {property_type:<18} | {price:<10} | {maximum_nights:<14} | {minimum_nights:<15}|")
                    location_found = True
                    
            # inform the user when the location is not found
            if not location_found:
                    airbnb_tui.error(f"No listing for '{location}' found!")
            break
          

            
# function to get information by property type
def get_by_property_type(airbnb_data):
    while True:
        
        # get property type from the user
        print("Enter a property type:")
        property_type = input().lower().strip()

        print(f"You have selected \033[1m{property_type}\033[0m as the type of property you want to retrieve.\n")
        print(f"The room type, accomodates, bathrooms, bedroom and beds for listings of {property_type} are listed below:\n{sep}\n")
        print(f"| \033[1m{'room_type':<12}\033[0m | \033[1m{'accomodates':<11}\033[0m | \033[1m{'bathrooms':<16}\033[0m | \033[1m{'bedroom':<10}\033[0m | \033[1m{'beds':<10}\033[0m |\n{sep}")

        # Display the rows
        by_property_type = False
        for row in airbnb_data:
            if property_type == row[13]:
                # select the appropriate columns based on the given property type
                room_type = row[14]
                accomodates = row[15]
                bathrooms = row[16]
                bedrooms = row[17]  
                beds = row[18]
                print(f"| {room_type:<12} | {accomodates:<11} | {bathrooms:<16} | {bedrooms:<10} | {beds:<10} |")

                by_property_type = True

        # inform the user when the property type is not found
        if not by_property_type:
                airbnb_tui.error(f"No property type '{property_type}' found!\nYou might want to check your spelling or enter another property type.")
        break
         
            
# function for own selection
"""
Is host a super host? If the user selects yes... get location from the user and return some information.
Allow the user to be able to play with the score rating he wants to see.
""" 
def by_location_superhost(airbnb_data):
    while True:       
        # get whether the user wants to select a superhost or not
        print("Enter 'True' to view hosts that are superhosts.")
        print("Enter 'False' to view hosts that are not superhosts.")
        is_superhost = input().upper().strip()

        # get location from user
        print("Enter a location")
        location = input().capitalize().strip()

        # get the review score the user wants to see
        print("Enter the review rating e.g 4.60")
        review_rating = (input().strip())

        # display to the user the selected values #\033[0m | \033[1m
        print("\nYour selections:")
        print(f"{sep}\nLocation: \033[1m{location}\033[0m")
        print(f"Superhost: \033[1m{is_superhost}\033[0m")
        print(f"Review score rating: \033[1m{review_rating}\033[0m\n{sep}\n")

        #create heading for the result
        print(f"| \033[1m{'host_id':<14}\033[0m | \033[1m{'host_name':<12}\033[0m | \033[1m{'review_scores_location':<20}\033[0m | \033[1m{'review_scores_value':<10}\033[0m | \033[1m{'instant_bookable':<10}\033[0m |\n{sep}")

        # Select the needed rows
        combination = False
        for row in airbnb_data:

            # check the conditions based on the user inputs
            if row[5] == location and row[27] == review_rating and row[9] == is_superhost:
                host_id = row[0]
                host_name = row[3]
                review_scores_rating = row[27]
                review_scores_location = row[32]
                review_scores_value = row[33]
                instant_bookable = row[23]
                print(f"| {host_id:<14} | {host_name:<12} | {review_scores_location:<22} | {review_scores_value:<19} | {instant_bookable:<14} |{sep}")
                combination = True
        # inform the user when the combination is not matched
        if not combination:
            airbnb_tui.error("\nNo selection matching your search!\nYou can check your spelling or different combinations.")
        break
        
        
# function to show the ten(10) most popular amenities
def top_10_amenities(airbnb_data):
    amenities = airbnb_data['amenities'].to_list()
    amenities = [eval(amenity) for amenity in amenities] #the previous function returns the list as a string, hence eval

    # created a big list and appended all the items in the amenities into it.
    amenities_list = []
    for amenity in amenities:
        amenities_list.extend(amenity)

    # turn the list into a pandas series and count all items    
    count = pd.Series(amenities_list).value_counts().head(10)
    
    # display nicely to the user
    print("These are the top 10 amenities provided by the hosts.\n")
    print(f"Top 1: Smoke alarm was provided by {count[0]} hosts.\n")
    print(f"Top 2: Kitchen was provided by {count[1]} hosts.\n")
    print(f"Top 3: Essentials was provided by {count[2]} hosts.\n")
    print(f"Top 4: Wifi was provided by {count[3]} hosts.\n")
    print(f"Top 5: Iron was provided by {count[4]} hosts.\n")
    print(f"Top 6: Hangers was provided by {count[5]} hosts.\n")
    print(f"Top 7: Hot water was provided by {count[6]} hosts.\n")
    print(f"Top 8: Long term stays allowed was provided by {count[7]} hosts.\n")
    print(f"Top 9: Dishes and silverware was provided by {count[8]} hosts.\n")
    print(f"Top 10: Hair dryer was provided by {count[9]} hosts.")


# function to get average price of stay in each location    
def average_price(df_airbnb):
    print(f"The average price of stay in each location with the minimun and maximum nights are listed below.\n{sep}\n")
    avg_price = df_airbnb.groupby("host_location")[["price","maximum_nights","minimum_nights"]].mean()
    print(avg_price.to_markdown())


# function to get the average review score rating for each location
def average_review_score(df_airbnb):
    print(f"The average review score rating for each location are listed below.\n{sep}\n")
    avg_review_score = df_airbnb.groupby("host_location")["review_scores_rating"].mean()
    print(avg_review_score.to_markdown())
  
    
# own selection for question b
"""
Function to take location from the user and return the room types available in that location. The function will also calculate
and display the overall rating for each room type available and the average price for each room type.
"""
def best_rating_price(df_airbnb):
    # copy the airbnb dataset not to change the original dataset
    df_airbnb_copy = df_airbnb.copy()
    # calculate the overall rating based on all the ratings in the dataset
    df_airbnb_copy["overall_rating"] = (df_airbnb_copy["review_scores_rating"]+df_airbnb_copy["review_scores_accuracy"]+df_airbnb_copy["review_scores_cleanliness"]+df_airbnb_copy["review_scores_checkin"]+df_airbnb_copy["review_scores_communication"]+df_airbnb_copy["review_scores_location"]+df_airbnb_copy["review_scores_value"])/7
    
    # group by the location and room type and select the price and overall rating
    best_rating_price = df_airbnb_copy.groupby(["host_location", "room_type"])[["overall_rating", "price"]].mean().reset_index()
    
    #sort the values
    best_rating_price.sort_values(["overall_rating", "price"], ascending=True, inplace=False)
    
    # get the location the user is interested in, ensure the first letter is capitalized and remove any white spaces
    location = input("Enter the location: ").capitalize().strip()
    print(f"\nYou have selected {location} as your location.")
    best = best_rating_price.loc[best_rating_price["host_location"] == location, :]
    
    if best.empty:
        print(f'{location} not found!')
    # let the user see the display highlighting the overall rating and the price
    best = best.style.background_gradient(cmap="Purples", low=0.40)
    return best


# let the user have a sense of the proportion of the number of bedrooms
def merge(df_airbnb):
    bedroom_group = df_airbnb.groupby("bedrooms").size().sort_values(ascending=True)
    bedroom_list = bedroom_group.index.tolist()
    num_bedroom_list = bedroom_group.tolist()
    bedroom_group_tup = [(bedroom_list[i], num_bedroom_list[i]) for i in range(0, len(bedroom_list))]
    # unpack and print
    for i,j in bedroom_group_tup:
        print(f'The listings with {i} bedrooms are {j} in number. \n')   
