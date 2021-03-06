import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

citys = ['chicago', 'new york', 'washington']

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Please choose a city you like to see data for chicago, new york or washington.').lower()
       if city in citys:
            break
       else:
           print("Please choose one of the 3 cities (chicago, new york city, washington):")    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month?(all, january, february, march, april, may, june).').lower()
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month in months:
            break 
        else:
           print("Please choose one of the options")    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('And which day? (all, sunday, monday, tuesday, wednesday, '\
                         'thursday, friday, saturday).').lower()
        days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]
        if day in days:
            break 
        else:
           print("Please choose one of the options")    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print(f"The most common month is {common_month}")

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print(f"The most common day is {common_day}")

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour is {common_start_hour}")
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f"The most common used start station is {common_start_station}") 

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f"The most common used end station is {common_end_station}") 

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df['Start Station']+" - "+ df['End Station'].mode()[0]
    print(f"The most common trip is {common_start_end_station}") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"Total Travel Time is {total_travel_time/3600} hours") 

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print(f"Average Travel Time is {average_travel_time/3600} hours") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_type = df["User Type"].value_counts()

    # TO DO: Display counts of gender
    if "Gender" in df :
        print (f"Count Of Gender {count_of_user_type}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df :
        earliest_year_of_birth = int(df["Birth Year"].min())
        print (f"Earliest Year of Birth {earliest_year_of_birth}")
        
        recent_year_of_birth = int(df["Birth Year"].max())
        print (f"Recent Year of Birth {recent_year_of_birth}")
        common_year_of_birth = int(df["Birth Year"].mode()[0])
        print (f"Common Year Of Birth {common_year_of_birth}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disply_data(df) :
    """ ask user if he need to disply raw dat or no """
    # TO DO: get user input to display data or not
    i = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
    if view_data not in ['yes','no']:
        print('please type yes or no')
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
        
    elif view_data == 'no':
        break
    else:
          while i+5 < df.shape[0]:
                print(df.iloc[i:i+5])
                i= i + 5
                view_data = input('\nWould you like to view 5 more rows?\n Enter yes or no.\n').lower()
                if view_data != 'yes':
                    print('Thank you')
                    break
                    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disply_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
