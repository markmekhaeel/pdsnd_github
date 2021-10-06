import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days=['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city,month,day=None,None,None    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while not(city in CITY_DATA.keys()):
        city=input('Enter the name of city you want collect data about(chicago, new york city, washington):\n')
        city=city.lower()
    print('city accepted: ',city)
    
    #get user input for month (all, january, february, ... , june)
    while not(month in months):
        month=input('what month you want filter data in(e.g: january,.. or all):\n')
        month=month.lower()
    print('month accepted: ', month)

    #get user input for day of week (all, monday, tuesday, ... sunday)
    while not(day in days):
        day=input('what day you want to filter in or all\n')
        day=day.lower()
    print('Day confirmed: ',day)

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
    #months = ['january', 'february', 'march', 'april', 'may', 'june']

    df=pd.read_csv(CITY_DATA[city])         #reads the file name as dataframe

    df['Start Time']=pd.to_datetime(df['Start Time'])       #convering the start time column to datetime

    df['month']=df['Start Time'].dt.month    #add month column has only month of the start time  

    if month != 'all':                                      #filtering by specific month
        month=months.index(month)
        df =df[df['month']==month]


    df['day']=df['Start Time'].dt.weekday_name        #add day columns splitted from the start date
    
    if day != 'all':                                        #filtering the data by specific day
        df =df[df['day']== day.title()]

    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    pop_month=df['month'].mode()[0]
    print('the most common month is: ',months[pop_month].title())
    #display the most common day of week
    pop_day=df['day'].mode()[0]
    print('the most common day is: ',pop_day)
    #display the most common start hour
    pop_hour=df['Start Time'].dt.hour.mode()[0]
    print('the most common hour is: ',pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print('the most common start station is: ',df['Start Station'].mode()[0])

    #display most commonly used end station
    print('the most common end station is: ',df['End Station'].mode()[0])

    #display most frequent combination of start station and end station trip
    print('the most popular trip is: ',(df['Start Station'] + ' && ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    print('the total travel time is :\nBy seconds= {}S\nBy minutes= {} Minutes\nBy hours= {} Hours\nBy days= {} Days'.format(df['Trip Duration'].sum(),df['Trip Duration'].sum()/60,df['Trip Duration'].sum()/(60*60),df['Trip Duration'].sum()/(60*60*24)))

    #display mean travel time
    print('the total travel time is :',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print('number of total subscribers is :{}\nNumber of total customers is :{}'.format(df['User Type'].value_counts()[0],df['User Type'].value_counts()[1]))

    #Check for gender column is in our data frame
    if 'Gender' in df.columns:
        print('Male: {}\nFemale: {}'.format(df['Gender'].value_counts()[0],df['Gender'].value_counts()[1]))

    #Display earliest, most recent, and most common year of birth
        print('Earliest birth year is: {}\nMost recent birth year is:{}\nMost common birth year is: {}'.format(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day =get_filters()    #get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
