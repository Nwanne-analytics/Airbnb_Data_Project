# Setting up the airbnb text user interface module
import random
# this will separate different lines where appropriate
line_separator = "-" * 120


# function to get the user's name and welcome the user to use the software
def name_of_user():
    print("Please enter your name.")
    name = input().capitalize()
    print(f"\n Welcome {name}!\n You are ready to use Nwanneka's COM 728 software.\n")

# start function to display the appropriate start message at the beginning of the program
def start(msg=""):
    print(line_separator)
    output = f"Program started: {msg}"
    print(f"{line_separator}\n{output}\n")
    
# end functuion
def end():
    print(f"\nOperation completed.\n{line_separator}\n")

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
             Enter A to perform tasks using the csv module.\n
             Enter B query or analyse using the pandas module.\n
             Enter C to visualize the Airbnb dataset using the matplotlib module.\n
             Enter EXIT to quit.""")
    print(f"{line_separator}\n")
    while True:
        try:
            users_choice = input().upper().strip()
            
            if users_choice in ["A", "B", "C", "EXIT"]:
                break
            while users_choice not in ["A", "B", "C", "EXIT"]:
                print("Enter A, B, C or EXIT")
                break
               
        except ValueError:
            print("The input was not an alphabet")
    return users_choice

    
#users_choice_of_program() for qusetion a   
def menu1():
    while True:
        try:
            print(f"{line_separator}\n")
            print("Enter 1 to retrieve a name of listing, host_name, description, host_location, and the date the host was created for an individual host by host_id.\n")
            print("Enter 2 to retrieve host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location.\n")
            print("Enter 3 to retrieve room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type.\n")
            print("Enter 4 retrieve specific columns of your choice related to an individual host by location.\n")
            print("Enter Exit to exit")
            print(f"{line_separator}\n")
    
        
            choice = input().strip().lower()
            
            if choice == '1':
                print(f"Retrieving name of listing, host_name, description, host_location, and the date the host was created for an individual host by host_id.\n{line_separator}\n")
                break

            if choice == '2':
                print(f"Retrieving host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location.\n{line_separator}\n")
                break

            if choice == '3':
                print(f"Retrieving room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type.\n {line_separator}\n")
                break

            if choice == '4':
                print(f"Retrieving specific columns and other ratings based on superhost, location and review score rating .\n{line_separator}\n")
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
        

        
# users_choice_of_program() for qusetion b 
def menu2():
    while True:
        try:
            print(f"{line_separator}\n")
            print("Enter 1 to to identify the top 10 most popular amenities or features that Airbnb hosts provide to customer.\n")
            print("Enter 2 to analyse the average price of stay in each location.\n")
            print("Enter 3 to analyse the average review scores rating for each location.\n")
            print("Enter 4 to analyse to the overall score rating and price based on location.\n")
            print("Enter Exit to exit")
            print(f"{line_separator}\n")    
        
            choice = input().strip().lower()
            
            if choice == '1':
                print(f"Identifying the top 10 most popular amenities or features that Airbnb hosts provide to customer.\n{line_separator}\n")
                break

            if choice == '2':
                print(f"Analysing the average price of stay in each location.\n{line_separator}\n")
                break

            if choice == '3':
                print(f"Analysing the average review scores rating for each location.\n {line_separator}\n")
                break

            if choice == '4':
                print(f"Retrieving the overall score rating and price based on location.\n{line_separator}\n")
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
Enter 1 to display the proportion of number of bedrooms of Airbnb listing using pie chart.\n
Enter 2 to display the number of listings for each room type using bar chart.\n
Enter 3 to display the relationship between accommodates and price using scatter plot.\n
Enter 4 to display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot).\n
Enter 5 to display a visualisation of your choice to present the information from the Airbnb services or properties that can indicate customer behaviour or pattern.\n
Enter Exit to exit
            """)            
            print(f"{line_separator}\n")    
        
            choice = input().strip().lower()
            
            if choice == '1':
                print(f"Displaying the proportion of number of bedrooms of Airbnb listing using pie chart.\n{line_separator}\n")
                break
            if choice == '2':
                print(f"Displaying the number of listings for each room type using bar chart.\n{line_separator}\n")
                break
            if choice == '3':
                print(f"Displaying the relationship between accommodates and price using scatter plot.\n {line_separator}\n")
                break
            if choice == '4':
                print(f"Displaying Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot).\n{line_separator}\n")
                break
            if choice == '5':
                print(f"Displaying a visualisation of your choice to present the information from the Airbnb services or properties that can indicate customer behaviour or pattern.\n{line_separator}\n")
                break
            if choice == 'exit':
                break
            
            while choice not in ['1','2','3','4','5','exit']:
                print("Enter 1, 2, 3, 4, 5 or Exit")
                break
                #choice = int(input().strip())
        except ValueError:
            print("The input was not a valid input.")

    return choice  
    
    
#     print(f"{line_separator}\n")
#     print("Enter 1 to display the proportion of number of bedrooms of Airbnb listing using pie chart.\n")
#     print("Enter 2 to display the number of listings for each room type using bar chart.\n")
#     print("Enter 3 to display the relationship between accommodates and price using scatter plot.\n")
#     print("Enter 4 to display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot).\n")
#     print("Enter 5 to display a visualisation of your choice to present the information from the Airbnb services or properties that can indicate customer behaviour or pattern.\n")
#     print("Enter 0 to exit")
#     print(f"{line_separator}\n")
#     while True:
#         try:
#             choice = int(input().strip())
#             if choice in [0,1,2,3,4,5]:
#                 break
#             while choice not in [0,1,2,3,4,5]:
#                 print("Enter 1, 2, 3, 4, 5 or 0")
#                 choice = int(input().strip())
#         except ValueError:
#             print("The input was not a valid integer.")

# def displays_c():
#     display = menu3()
#     if display == 1:
#         print(f"Displaying the proportion of number of bedrooms of Airbnb listing using pie chart.\n{line_separator}\n")
#     elif display == 2:
#         print(f"Displaying the number of listings for each room type using bar chart.\n{line_separator}\n")
#     elif display == 3:
#         print(f"Displaying the relationship between accommodates and price using scatter plot.\n {line_separator}\n")
#     elif display == 4:
#         print(f"Displaying Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot).\n{line_separator}\n")
#     elif display == 5:
#         print(f"Displaying a visualisation of your choice to present the information from the Airbnb services or properties that can indicate customer behaviour or pattern.\n{line_separator}\n") 
#     elif display == 0:
#         print(f"Goodbye!{line_separator}\n")

def menu4():
    print("Do you want to have a sense of the proportion of the number of bedrooms before ploting?")
    print("Enter Yes to see the proportion of the number of bedrooms before ploting.")
    print("Enter No to exit")
    users_input = input()
    return users_input 