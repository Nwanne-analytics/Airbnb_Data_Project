#importing the needed modules
import airbnb_tui
import matplotlib.pyplot as plt
import pandas as pd
 
# function to plot the airbnb 
def proportion_bedrooms(df_airbnb):
    # get the appropriate column and data
    bedroom_group = df_airbnb.groupby("bedrooms").size().sort_values(ascending=True)
    bedroom_list = bedroom_group.index.tolist()
    num_bedroom_list = bedroom_group.tolist()
    
    # create the figure
    fig = plt.figure(figsize=(8,14))
    
    # plot the pie chart,label and title
    plt.pie(num_bedroom_list, labels=bedroom_list, autopct='%1.1f%%')
    plt.title("Proportion of the Number of Bedrooms of Listings")
    plt.legend(loc="best",bbox_to_anchor=(1,1),fontsize=8)
    
    # show the graph
    plt.show()
    

def num_listings_roomtype(df_airbnb):
    # get the appropriate column and data
    room_type_group = df_airbnb.groupby("room_type").size().sort_values(ascending=False)
    num_listing_room_type = room_type_group.tolist()
    room_type = room_type_group.index.tolist()
    
    # create the figure
    fig = plt.figure(figsize=(15,8))
    # plot bar
    plt.bar(room_type,num_listing_room_type)
    # label
    plt.xlabel("Room Type")
    plt.ylabel("Number of Listing")
    plt.yticks(range(0, 10000, 500)) # to make reading the graph easier due to smaller values
    # set title
    plt.title("Number of Listing for Each Room Type")
    #show the graph
    plt.show()

# Display the relationship between accommodates and price using scatter plot
def accommodates_and_price(df_airbnb):
    fig = plt.figure(figsize=(15,8)) #Create figure object and set up the size of figure

    accommodates = df_airbnb["accommodates"]
    price = df_airbnb["price"]

    # plot
    plt.scatter(accommodates, price)
    # label
    plt.xlabel('Maximun Capacity')
    plt.ylabel('Price')
    plt.title('Maximun Capacity vs Price')
    # show graph
    plt.show()
    
def prices_per_year(df_airbnb):
    # convert the host_since column to a datetime
    df_airbnb["host_since"] = pd.to_datetime(df_airbnb["host_since"])
    # filter year 2019
    year_2019 = df_airbnb.query("host_since >= '2019-01-01' and host_since <= '2019-12-31'")
    # filter year 2020
    year_2020 = df_airbnb.query("host_since >= '2020-01-01' and host_since <= '2020-12-31'")
    # filter year 2021
    year_2021 = df_airbnb.query("host_since >= '2021-01-01' and host_since <= '2021-12-31'")
    # filter year 2022
    year_2022 = df_airbnb.query("host_since >= '2022-01-01' and host_since <= '2022-12-31'")
    
    # group the year by month and sum the prices
    price_year_2019 = year_2019.groupby(year_2019.host_since.dt.month)["price"].sum()
    price_year_2020 = year_2020.groupby(year_2020.host_since.dt.month)["price"].sum()
    price_year_2021 = year_2021.groupby(year_2021.host_since.dt.month)["price"].sum()
    price_year_2022 = year_2022.groupby(year_2022.host_since.dt.month)["price"].sum()
    
    #Create figure, subplots and get the axes
    fig , (axis1,axis2,axis3,axis4) = plt.subplots(4,1, figsize = (12,15))
    

    #Add title for entire figure
    fig.suptitle("Airbnb prices from 2019 - 2022")

    # Airbnb price in 2019 to axis1
    # set x axis and y axis for axis1
    x = price_year_2019.index.tolist()
    y = price_year_2019.tolist()

    # plot line graph for axis1
    axis1.plot(x,y)
    # set titles and labels
    axis1.set(title="Price of Airbnb in 2019", xlabel='Month',ylabel='Price')

    # Airbnb price in 2020 to axis2
    # set x axis and y axis for axis2
    x = price_year_2020.index.tolist()
    y = price_year_2020.tolist()

    # plot line graph for axis2
    axis2.plot(x,y)
    # set titles and labels
    axis2.set(title="Price of Airbnb in 2020", xlabel='Month',ylabel='Price')

    # Airbnb price in 2021 to axis3
    # set x axis and y axis for axis3
    x = price_year_2021.index.tolist()
    y = price_year_2021.tolist()

    # plot line graph for axis3
    axis3.plot(x,y)
    # set titles and labels
    axis3.set(title="Price of Airbnb in 2021", xlabel='Month',ylabel='Price')

    # Airbnb price in 2020 to axis4
    # set x axis and y axis for axis4
    x = price_year_2022.index.tolist()
    y = price_year_2022.tolist()

    # plot line graph for axis4
    axis4.plot(x,y)
    # set titles and labels
    axis4.set(title="Price of Airbnb in 2022", xlabel='Month',ylabel='Price')

    # set space between the subplots
    plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
                   

    # show graph
    plt.show()

# plot the top 10 amenities to the user 
def plot_top10_amenities(df_airbnb):
    # select the amenities column and cast to list
    amenities = df_airbnb['amenities'].to_list()
    amenities = [eval(amenity) for amenity in amenities] #the previous function returns the list as a string, hence eval
    
    # created a big list and appended all the items in the amenities into it.
    amenities_list = []
    for amenity in amenities:
        amenities_list.extend(amenity)
    count = pd.Series(amenities_list).value_counts().head(10)
    
    amenities = ["Smoke alarm", "Kitchen", "Essentials", "Wifi", "Iron", "Hangers", "Hot water", "Long stays", "Dishes & silverware", "Hair dryer"]
    count = [count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7], count[8], count[9]]
    
    # creates figure for the plot
    fig = plt.figure(figsize=(18,8))
    
    # create a horizontal bar chart
    plt.barh(amenities, count, color="blue")
    # label the x and y and label the graph
    plt.xlabel("Amenities")
    plt.ylabel("Count")
    plt.title("Top Ten Amenities Provided by Hosts")
    # show the graph
    plt.show() 
 

"""
I am interested in knowing whether the customers spend more nights in listings with high review scores and what affects the price of listings.
"""
# own selection for question c
def own_selection_c():
    df_airbnb = pd.read_csv("Data/Airbnb_UK_2022.csv")
    # convert the host_since column to a datetime
    df_airbnb["host_since"] = pd.to_datetime(df_airbnb["host_since"])
    
#     df_airbnb = df_airbnb.copy()
#     df_airbnb["host_acceptance_rate"].str.rstrip("%").astype(float)

    # define a lambda function to remove percent sign and convert to float
    remove_percent = lambda x: float(x[:-1]) if x.endswith("%") else x

    # apply the lambda function to the 'col1' column
    df_airbnb['host_acceptance_rate'] = df_airbnb['host_acceptance_rate'].apply(remove_percent)
    
    # filter year 2019
    year_2019 = df_airbnb.query("host_since >= '2019-01-01' and host_since <= '2019-12-31'")
    # filter year 2020
    year_2020 = df_airbnb.query("host_since >= '2020-01-01' and host_since <= '2020-12-31'")
    # filter year 2021
    year_2021 = df_airbnb.query("host_since >= '2021-01-01' and host_since <= '2021-12-31'")
    # filter year 2022
    year_2022 = df_airbnb.query("host_since >= '2022-01-01' and host_since <= '2022-12-31'")

    # group the year by month and get the mean of the review_scores_rating
    review_year_2019 = year_2019.groupby(year_2019.host_since.dt.month)["review_scores_rating"].mean()
    review_year_2020 = year_2020.groupby(year_2020.host_since.dt.month)["review_scores_rating"].mean()
    review_year_2021 = year_2021.groupby(year_2021.host_since.dt.month)["review_scores_rating"].mean()
    review_year_2022 = year_2022.groupby(year_2022.host_since.dt.month)["review_scores_rating"].mean() 
    
    #group the year by year and host_is_superhost and find the mean of the acceptance rate
    acceptance_rate_2019 = year_2019.groupby([year_2019.host_since.dt.year,year_2019.host_is_superhost])["host_acceptance_rate"].mean().tolist()
    acceptance_rate_2020 = year_2020.groupby([year_2020.host_since.dt.year,year_2020.host_is_superhost])["host_acceptance_rate"].mean().tolist()
    acceptance_rate_2021 = year_2021.groupby([year_2021.host_since.dt.year,year_2021.host_is_superhost])["host_acceptance_rate"].mean().tolist()
    acceptance_rate_2022 = year_2022.groupby([year_2022.host_since.dt.year,year_2022.host_is_superhost])["host_acceptance_rate"].mean().tolist()

    # adjust subplots
    plt.subplots_adjust(wspace=0.3,hspace=0.5)
    # create subplots
    fig = plt.figure(figsize=(25,20))
    plt.figure(facecolor='yellow')
    #Add title for entire figure
    fig.suptitle("Customer behaviours")
    
    #create the axis
    ax1 = fig.add_subplot(4,1,1)
    ax2 = fig.add_subplot(4,3,4)
    ax3 = fig.add_subplot(4,3,5)
    ax4 = fig.add_subplot(4,3,6)
    ax5 = fig.add_subplot(4,2,5)
    ax6 = fig.add_subplot(4,2,6)
    ax7 = fig.add_subplot(4,1,4)

    # data for ax1
    x = review_year_2019.index.tolist()
    y1 = review_year_2019.tolist()
    y2 = review_year_2020.tolist()
    y3 = review_year_2021.tolist()
    y4 = review_year_2022.tolist()
    y = [y1,y2,y3,y4]
    # plot line graph for axis1
    for i in range(len(y)):
        years = [2019, 2020, 2021, 2022]
        ax1.plot(x,y[i],'o-',label=years[i])

    # set titles and labels
    ax1.set(title="Best Months to Use Airbnb Based on Review Score Rating from 2019 to 2022",xlabel='Months',ylabel='Review Score Rating')
    ax1.legend()
    
    # axis 2
    # airbnb_dataset[["review_scores_accuracy", "minimum_nights"]]
    x = df_airbnb["review_scores_accuracy"]
    y = df_airbnb["minimum_nights"]
    ax2.scatter(x,y)
    # set titles and labels
    ax2.set(title="Relationship b/w Review Scores Accuracy and Minimum Nights", xlabel='Review Scores Accuracy',ylabel='Minimum Nights')

    # axis 3
    # airbnb_dataset[["review_scores_cleanliness", "minimum_nights"]]
    x = df_airbnb["review_scores_cleanliness"]
    y = df_airbnb["minimum_nights"]
    ax3.scatter(x,y)
    ax3.set(title="Relationship b/w Review Scores Cleanliness and Minimum Nights", xlabel='Review Scores Cleanliness',ylabel='Minimum Nights')

    # axis 4
    # airbnb_dataset[["review_scores_checkin", "minimum_nights"]]
    x = df_airbnb["review_scores_checkin"]
    y = df_airbnb["minimum_nights"]
    ax4.scatter(x,y)
    ax4.set(title="Relationship b/w Review Scores Checkin and Minimum Nights", xlabel='Review Scores Checkin',ylabel='Minimum Nights')

    # axis 5
    # airbnb_dataset[["review_scores_communication", "minimum_nights"]]
    x = df_airbnb["review_scores_communication"]
    y = df_airbnb["minimum_nights"]
    ax5.scatter(x,y)
    ax5.set(title="Relationship b/w Review Scores Communication and Minimum Nights", xlabel='Review Scores Communication',ylabel='Minimum Nights')

    # axis 6
    # airbnb_dataset[["review_scores_location", "minimum_nights"]]
    x = df_airbnb["review_scores_location"]
    y = df_airbnb["minimum_nights"]
    ax6.scatter(x,y)
    ax6.set(title="Relationship b/w Review Scores Location and Minimum Nights", xlabel='Review Scores Location',ylabel='Minimum Nights')

    #axis 7
    # comparison between super hosts and non super hosts regarding the acceptance rate
    
    is_not_super = [80.33,82.60,87.52,91.06] 
    is_super = [92.17,93.36,91.05,91.06]
    
    X_axis = [1, 2, 3, 4]
    width = 0.25

    ax7.bar(X_axis, is_super, color='b', width=width, edgecolor='black', label='is_super')
    ax7.bar([x + width for x in X_axis], is_not_super, color='r', width=width, edgecolor='black', label='is_not_super')

    ax7.set(title="Acceptance rate in each year", xlabel="Year",ylabel ="Acceptance rate" )
    ax7.set_xticks([x + width/2 for x in X_axis], [2019,2020,2021,2022])
    ax7.legend(loc='upper center')
    
    # show the graph
    plt.show()
    
#     fig.savefig('Own_selection2.png')   
 