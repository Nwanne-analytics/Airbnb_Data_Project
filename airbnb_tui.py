# Setting up the airbnb text user interface module
import random

# this will separate different lines where appropriate
line_separator = "-" * 120


# function to get the user's name and welcome the user to use the software
def name_of_user():
    print("Please enter your name.")
    name = input().title()
    print(f"\n Welcome {name}!\n You are ready to use Nwanneka's COM 728 Airbnb data software.\n")

# start function to display the appropriate start message at the beginning of the program
def start(msg=""):
#     print(line_separator)
    output = f"\n\033[1mProgram started: {msg}\033[0m"
    print(f"{line_separator}\n{output}\n")
    
# end function
def end():
    print(f"\n\033[1mOperation completed\033[0m.\n")

# error function 
def error(msg=""):
    print(f"Error! {msg}\nPlease try again!\n")
    
# function exit messages
def exit_msg():
    messages = [
    "Goodbye!",
    "Have a good day!",
    "See you next time!",
    "Exited!",
    "Bye!"      
    ]
    print(random.choice(messages))
    

# this function asks the user about choice of programme he wants to perform with respect to question a, b and c of the requirement
def users_choice_of_program():
    print(f"""{line_separator}\n
             Please follow the instructions below to perform any operation of choice.\n
             Enter \033[1mA\033[0m to perform tasks using the csv module.\n
             Enter \033[1mB\033[0m query or analyse using the pandas module.\n
             Enter \033[1mC\033[0m to visualize the Airbnb dataset using the matplotlib module.\n
             Enter \033[1mEXIT\033[0m to quit.""")
    print(f"{line_separator}\n")
    while True:
        try:
            users_choice = input().upper().strip()
            # check the user's entry
            if users_choice in ["A", "B", "C", "EXIT"]:
                break
            while users_choice not in ["A", "B", "C", "EXIT"]:
                print("Enter A, B, C or EXIT")
                break
        # handle any value error     
        except ValueError:
            print("The input was not an alphabet")         
    return users_choice

    
#users_choice_of_program() for qusetion a   
def menu1():
    while True:
        try:
            print(f"{line_separator}\n")
            print("""
Enter \033[1m1\033[0m to retrieve a name of listing, host_name, description, host_location, and the date the host was created for an individual host by host_id.\n
Enter \033[1m2\033[0m to retrieve host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location.\n
Enter \033[1m3\033[0m to retrieve room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type.\n
Enter \033[1m4\033[0m retrieve other ratings and whether the host is instant bookable by superhost, location and review score rating.\n")
Enter \033[1mExit\033[0m to exit.
            """)
            print(f"{line_separator}\n")
    
            # collect input from the user
            choice = input().strip().lower()
            # check for conditions
            if choice == '1':
                print(f"\033[1mRetrieving name of listing, host_name, description, host_location, and the date the host was created for an individual host by host_id...\n{line_separator}\033[0m\n")
                break

            if choice == '2':
                print(f"\033[1mRetrieving host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location...\n{line_separator}\033[0m\n")
                break

            if choice == '3':
                print(f"\033[1mRetrieving room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type...\n {line_separator}\033[0m\n")
                break

            if choice == '4':
                print(f"\033[1mRetrieving other ratings and whether the host is instant bookable based on superhost, location and review score rating ...\n{line_separator}\033[0m\n")
                break

            if choice == 'exit':
                break
            
            while choice not in ['1','2','3','4','exit']:
                print("Enter 1, 2, 3, 4 or Exit")
                break
        # except any value error
        except ValueError:
            print("The input was not a valid input.")

    return choice
        

        
# users_choice_of_program() for qusetion b 
def menu2():
    while True:
        try:
            print(f"{line_separator}\n")
            print("Enter \033[1m1\033[0m to to identify the top 10 most popular amenities or features that Airbnb hosts provide to customer.\n")
            print("Enter \033[1m2\033[0m to analyse the average price of stay in each location.\n")
            print("Enter \033[1m3\033[0m to analyse the average review scores rating for each location.\n")
            print("Enter \033[1m4\033[0m to analyse to the overall score rating and price based on location.\n")
            print("Enter \033[1mExit\033[0m to exit")
            print(f"{line_separator}\n")  
            
            # collect input from the user
            choice = input().strip().lower()
            # check for conditions  
            if choice == '1':
                print(f"\033[1mIdentifying the top 10 most popular amenities or features that Airbnb hosts provide to customer...\n{line_separator}\033[0m\n")
                break

            if choice == '2':
                print(f"\033[1mAnalysing the average price of stay in each location...\n{line_separator}\033[0m\n")
                break

            if choice == '3':
                print(f"\033[1mAnalysing the average review scores rating for each location...\n {line_separator}\033[0m\n")
                break

            if choice == '4':
                print(f"\033[1mRetrieving the overall score rating and price based on location...\n{line_separator}\033[0m\n")
                break

            if choice == 'exit':
                break
            
            while choice not in ['1','2','3','4','exit']:
                print("Enter 1, 2, 3, 4 or Exit")
                break
                #choice = int(input().strip())
        except ValueError:
            print("The input was not a valid input.")

    return choice


# users_choice_of_program() for qusetion c 
def menu3():   
    while True:
        try:
            print(f"{line_separator}\n")
            print("""
Enter \033[1m1\033[0m to display the proportion of number of bedrooms of Airbnb listing using pie chart.\n
Enter \033[1m2\033[0m to display the number of listings for each room type using bar chart.\n
Enter \033[1m3\033[0m to display the relationship between accommodates and price using scatter plot.\n
Enter \033[1m4\033[0m to display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot).\n
Enter \033[1m5\033[0m to display a visualisation of your choice to present the information from the Airbnb services or properties that can indicate customer behaviour or pattern.\n
Enter \033[1mExit\033[0m to exit
            """)            
            print(f"{line_separator}\n")    
        
            # collect input from the user
            choice = input().strip().lower()
            # check for conditions
            if choice == '1':
                print(f"\033[1mDisplaying the proportion of number of bedrooms of Airbnb listing using pie chart...\n{line_separator}\033[0m\n")
                break
            if choice == '2':
                print(f"\033[1mDisplaying the number of listings for each room type using bar chart...\n{line_separator}\033[0m\n")
                break
            if choice == '3':
                print(f"\033[1mDisplaying the relationship between accommodates and price using scatter plot...\n {line_separator}\033[0m\n")
                break
            if choice == '4':
                print(f"\033[1mDisplaying Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot)...\n{line_separator}\033[0m\n")
                break
            if choice == '5':
                print(f"\033[1mDisplaying a visualisation of your choice to present the information from the Airbnb services or properties that can indicate customer behaviour or pattern...\n{line_separator}\033[0m\n")
                break
            if choice == 'exit':
                break   
            # check the user's entry, if not in the option continue to tell the user to make input
            while choice not in ['1','2','3','4','5','exit']:
                print("Enter 1, 2, 3, 4, 5 or Exit")
                break      
        except ValueError:
            print("The input was not a valid input.")

    return choice  
    
# menu in situation where the user wants to see more on proportion of bedroom
def menu4():  
    while True:        
        print("""
        Do you want to have a sense of the proportion of the number of bedrooms before ploting?\n
        Enter \033[1mYes\033[0m to see the proportion of the number of bedrooms before ploting.
        Enter \033[1mNo\033[0m to see the plot only.\n
        """)

        # collect the user's input
        user_input = input().capitalize().strip()
        try:
            # check for conditions
            if user_input == "Yes":
                print("\033[1mRetrieveing information about the proportion of the number of bedrooms before ploting...\n\033[0m")

            elif user_input == "No":
                print("\033[1mShowing plot of the proportion of the number of bedrooms of listings...\033[0m")
            # check the user's input
            while user_input not in ['Yes', 'No']:
                print("Enter 'Yes' or 'No'")  
                user_input = input().capitalize().strip()
        except ValueError:
            print("The input was not a valid input.")
        return user_input 
    
    
# menu if the user wants to see the plot of top 10 most popular amentities
def menu5():
    while True:
        print("""
        Do you want to see a bar graph of the top 10 popular amenities?\n
        Enter \033[1mYes\033[0m to see the horizontal bar graph of the top 10 popular amenities.
        Enter \033[1mNo\033[0m to see the listing only.
        """)

        # collect the user's input
        user_input = input().capitalize().strip()
        try: 
            # check for conditions
            if user_input == "Yes":
                print("\033[1mRetrieveing the bar graph of the top 10 popular amenities...\033[0m")

            elif user_input == "No":
                print("\033[1mShowing the top 10 popular amenities...\033[0m")
            # check the user's input
            while user_input not in ['Yes', 'No']:
                print("Enter 'Yes' or 'No'")
                user_input = input().capitalize().strip()
        except ValueError:
            print("The input was not a valid input.")
        return user_input