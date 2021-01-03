import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_months = ['january', 'february', 'march', 'april', 'may','june', 'all']
valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

#-------------------------------------------------------------START : get_filters---------------------------------------------------------------------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
#---------------------------------------------------------------------CITY-----------------------------------------------------------------------
    #  print instructons to user
    print('\nHello! Let\'s explore some US bikeshare data!\n\n'.center(120).upper())
    print('To view the available bikeshare data, kindly \nType: the letter (c) for Chicago. \n\
Type: the letter (n) for New York City.\nType: the letter (w) for Washington.\n ')
  
    # Get user input for city (chicago, new york city, washington)
    city = input("Enter your input (◒‿◒): ").lower()
    valid_cities = [ 'c','n','w']
   
# A while loop to handle invalid inputs
    while city not in valid_cities :
        print("\nUnvalid letter, please (ಠ_ಠ). \n")
        print('To view the available bikeshare data, kindly \nType: the letter (c) for Chicago. \n\
Type: the letter (n) for New York City.\nType: the letter (w) for Washington.\n ')
        # Ask to enter an input agin
        city = input("Enter your input (◒‿◒):  ").lower()
    
    # Mapping the cities 
    cities = {'c': 'chicago' , 
              'n': 'new york city', 
              'w':'washington'}
    city =  cities[city]
#--------------------------------------------------------------------MONTH---------------------------------------------------------------------
    # print instructons to user
    print("To filter %s\'s data by month, please enter the month name or enter \'all\' for not filtering \n\
Vaild inputs is  [ January - February - March - April - May - June - All ]\n " %  city )
    #  Get user input for month (all, january, february, ... , june)
    month = input('Enter your input (◒‿◒): ').lower()

    # A while loop to handle invalid inputs
    while month not in valid_months :
        print('\nEnter a valid month, please (ಠ_ಠ).\n')
        print('''To filter %s\'s data by month, please enter the month name or enter \'all\' for not filtering \n\
Vaild inputs is  [ January - February - March - April - May - June - All ]\n ''' % city)
        # Ask to enter an input agin
        month = input('Enter your input (◒‿◒):  ').lower()
#----------------------------------------------------------------------DAY---------------------------------------------------------------------
    # print instructons to user
    print('''To filter %s\'s data by day, please enter the day name or enter \'all\' for not filtering \n\
Vaild inputs is  [ Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday,  All ]\n ''' % city )
    #  Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter your input (◒‿◒): ').lower()

    # A while loop to handle invalid inputs
    while day not in  valid_days :
        print('\nEnter a valid month, please (ಠ_ಠ).\n')
        print('''To filter %s\'s data by month, please enter the month name or enter \'all\' for not filtering \n\
Vaild inputs is  [ Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday,  All ]\n '''  % city)
        # Ask to enter an input agin
        
        day = input('Enter your input (◒‿◒):   ').lower()
    print('-'*60)
    return city, month, day
#--------------------------------------------------------------END  :  get_filters-----------------------------------------------------------------
#--------------------------------------------------------------START:  load_data-------------------------------------------------------------------
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime( df['Start Time'] )
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = valid_months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]
        
    return df
#--------------------------------------------------------------END  :  load_data---------------------------------------------------------------------
#--------------------------------------------------------------START:  time_stats--------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\ncalculating the most frequent times of travel...\n'.title())
    start_time = time.time()
    
    #-------------------Display the most common month------------------------------
    if month == 'all' :
     #used valid_month list to return the name of the month not he number
        print("The most common month is ( ✿ ‿ ✿ ): [ %s ]" % valid_months[df['Month'].mode().values[0] - 1])
    else :
        print("The most common month is ( ✿ ‿ ✿ ): [ %s ]" % month)
        
   #------------------ Display the most common day of week-----------------------------
    if day == 'all' :
        print("The most common day is   ( ✿ ‿ ✿ ): [ %s ]" % df['Day'].mode().values[0])
    else :
        print("The most common day is   ( ✿ ‿ ✿ ): [ %s ]" % day)
        
    #-------------------Display the most common start hour------------------------------
    print("The most common hour is  ( ✿ ‿ ✿ ): [ %d ]" % df['Start Time'].dt.hour.mode().values[0])
    
    #-------------------Print run time of this function------------------------------
    print("\nThis took (%s) seconds." % (time.time() - start_time))
    print('-'*60)
#--------------------------------------------------------------END  :  time_stats---------------------------------------------------------------------
#--------------------------------------------------------------START:  station_stats------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Display most commonly used start station
    print("The most common start station is ( ◠‿◠ ): [ %s ]" % df['Start Station'].mode().values[0])
    # Display most commonly used end station
    print("The most common end station is   ( ◠‿◠ ): [ %s ]" % df['End Station'].mode().values[0])
    # Display most frequent combination of start station and end station trip
    df['Trip'] ="\nFrom [ " + df['Start Station'] + " ] To [" + df['End Station'] + "]"
    print("The most common combination of start station and end station trip is ( ◠‿◠ ): %s" % df['Trip'].mode().values[0])
    
    # Print run time of this function-
    print("\nThis took ( %s ) seconds." % (time.time() - start_time))
    print('-'*60)
#--------------------------------------------------------------END  :  station_stats------------------------------------------------------------------
#--------------------------------------------------------------START:  trip_duration_stats------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # Display total travel time
    Total_time = df['Trip Duration'].sum()
    # Representation of time duration HH:MM:SS
    Mins , Secs = divmod(Total_time , 60)
    Hrs , Mins =  divmod(Mins , 60)
    Days , Hrs =  divmod(Hrs , 60)
    Months,Days = divmod(Days , 30)
    Years , Months = divmod(Months , 12)
    print("The total travels time [ Years:Month:Days:Hours:Minutes:Seconds] is [%d:%d:%d:%d:%d:%d]✌\n" % (Years , Months ,  Days,  Hrs , Mins , Secs)  )

    # Display mean travel time
    Avg_time = df['Trip Duration'].mean()
    # Representation of time duration HH:MM:SS
    Min , Sec = divmod(Avg_time , 60)
    Hr , Min =  divmod(Min , 60)
    
    print("The avarage travels time [Hours:Minutes:Seconds] is [%d:%d:%d]✌\n" % (Hr , Min , Sec)  )

    print("\nThis took ( %s ) seconds." % (time.time() - start_time))
    print('-'*60)
#--------------------------------------------------------------END  :  trip_duration_stats--------------------------------------------------
#--------------------------------------------------------------START:  user_stats-----------------------------------------------------------
def user_stats(df , city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The number of user types is (ᅌᴗᅌ)\n{}\n" .format(  df['User Type'].value_counts()  ) )
    
    
    # Display counts of gender
    if city != 'washington' : 
        print('-'*30)
        print("The number of gender is (ᅌᴗᅌ)\n{}\n" .format( df['Gender'].value_counts())  )
     
    # Display earliest, most recent, and most common year of birth
    if city != 'washington': 
        print('-'*30)
        print("The earliest year of birth is    (ᅌᴗᅌ): {}\n" .format(df['Birth Year'].min()) )
        print("The most recent year of birth is (ᅌᴗᅌ): {}\n" .format(df['Birth Year'].max()) )
        print("The common year of birth  is     (ᅌᴗᅌ): {}\n" .format( df['Birth Year'].mode().values[0]) )

    print("\nThis took ( %s ) seconds." % (time.time() - start_time))
    print('-'*60)
#--------------------------------------------------------------END   :  user_stats-----------------------------------------------------------
#--------------------------------------------------------------START :  display_raw_data-----------------------------------------------------
def display_raw_data(df):
    i = 0 
    raw = input("\nWould you like to print 5 rows data? Input 'yes' or 'no':  ( ✿ ‿ ✿ ).\n").lower() 

    while True:            
        if raw == 'no':
            break
        print(df.iloc[i:i+5])
        raw =  input("\nWould you like to print 5 rows data? Enter 'yes' or 'no'  ( ✿ ‿ ✿ ).\n").lower() 
        i += 5
        
        print('-'*60)
#--------------------------------------------------------------END :  display_raw_data--------------------------------------------
#--------------------------------------------------------------Calling the functions----------------------------------------------
while True:
    
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df,city)
    display_raw_data(df)
    
    restart = input("\nWould you like to restart? Enter 'yes' or 'no'  ( ✿ ‿ ✿ ).\n").lower()
    while restart not in ['yes','no'] :
        print('UNVALID INPUT (ಠ_ಠ).\n')
        restart = input("\nWould you like to restart? Enter 'yes' or 'no'  ( ✿ ‿ ✿ ).\n").lower()
    if restart.lower() != 'yes':
        break
