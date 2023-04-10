#importing the needed modules
import airbnb_tui
#import airbnb_process


# function to plot the airbnb 
def proportion_bedrooms(df_airbnb):
    bedroom_group = df_airbnb.groupby("bedrooms").size().sort_values(ascending=True)
    bedroom_list = bedroom_group.index.tolist()
    num_bedroom_list = bedroom_group.tolist()
    fig = plt.figure(figsize=(7,9))

    plt.pie(num_bedroom_list,labels=bedroom_list,autopct='%1.1f%%')
    plt.title("Proportion of the Number of Bedrooms of Listings")

    plt.legend(loc="best",bbox_to_anchor=(1,1))

    plt.show()

def num_listings_roomtype(df_airbnb):
    room_type_group = df_airbnb.groupby("room_type").size().sort_values(ascending=False)
    num_listing_room_type = room_type_group.tolist()
    room_type = room_type_group.index.tolist()
    fig = plt.figure(figsize=(15,8))

    plt.bar(room_type,num_listing_room_type)
    # label
    plt.xlabel("Room Type")
    plt.ylabel("Number of Listing")
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

    
"""
I am interested in knowing whether the customers spend more nights in listings with high review scores and what affects the price of listings.
"""
def relationship(df_airbnb):
    
 