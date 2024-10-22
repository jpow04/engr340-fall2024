import sys
import pandas as pd

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data = []

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date, county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases == '':
            cases = 0
        if deaths == '':
            deaths = 0

        # convert elements into ints
        try:
            entry = (date, county, state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)

    return data


def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    # Establish pandas data frame
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # create dataset focusing on only Harrisonburg City and Rockingham County VA
    data_rockingham = df.loc[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]
    data_harrisonburg = df.loc[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]

    # Establish corresponding pandas data frame
    df_rockingham = pd.DataFrame(data_rockingham, columns=['date', 'county', 'state', 'cases', 'deaths'])
    df_harrisonburg = pd.DataFrame(data_harrisonburg, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # Reset data frame index
    df_rockingham = df_rockingham.reset_index(drop=True)
    df_harrisonburg = df_harrisonburg.reset_index(drop=True)

    # Confirm data frame is sorted by date
    df_rockingham = df_rockingham.sort_values(by='date', ascending=True)
    df_harrisonburg = df_harrisonburg.sort_values(by='date', ascending=True)

    # Print data frames to manually check
    '''pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df_rockingham)
    print(df_harrisonburg)'''

    # Select first entry in dataset as a variable
    first_case_rockingham = df_rockingham.at[0, 'date']
    first_case_harrisonburg = df_harrisonburg.at[0, 'date']

    # Print variables
    print("the first positive COVID case in Rockingham County, Virginia was documented:", first_case_rockingham)
    print("the first positive COVID case in Harrisonburg City, Virginia was documented:", first_case_harrisonburg)

    return


def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # Establish pandas data frame
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # create dataset focusing on only Harrisonburg City and Rockingham County VA
    data_rockingham = df.loc[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]
    data_harrisonburg = df.loc[(df['county'] == 'Harrisonburg city') & (df['state'] == 'Virginia')]

    # Establish corresponding pandas data frame
    df_rockingham = pd.DataFrame(data_rockingham, columns=['date', 'county', 'state', 'cases', 'deaths'])
    df_harrisonburg = pd.DataFrame(data_harrisonburg, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # Reset data frame index
    df_rockingham = df_rockingham.reset_index(drop=True)
    df_harrisonburg = df_harrisonburg.reset_index(drop=True)

    # Confirm data frame is sorted by date
    df_rockingham = df_rockingham.sort_values(by='date', ascending=True)
    df_harrisonburg = df_harrisonburg.sort_values(by='date', ascending=True)

    # Utilize .diff to calculate difference of cases column and add it to dataframe
    df_rockingham['new cases'] = df_rockingham['cases'].diff()
    max_cases_index_rockingham = df_rockingham['new cases'].idxmax()  # Find index of the maximum amount of new cases
    greatest_number_cases_rockingham = df_rockingham.loc[max_cases_index_rockingham, 'new cases']  # Select new cases
    greatest_number_cases_date_rockingham = df_rockingham.loc[max_cases_index_rockingham, 'date']  # Select Date

    # Utilize .diff to calculate difference of cases column and add it to dataframe
    df_harrisonburg['new cases'] = df_harrisonburg['cases'].diff()
    max_cases_index_harrisonburg = df_harrisonburg['new cases'].idxmax()  # Find index of the maximum amount of new cases
    greatest_number_cases_harrisonburg = df_harrisonburg.loc[max_cases_index_harrisonburg, 'new cases']  # Select new cases
    greatest_number_cases_date_harrisonburg = df_harrisonburg.loc[max_cases_index_harrisonburg, 'date']  # Select Date

    # Print data frames to manually check
    '''pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df_rockingham)
    print(df_harrisonburg)'''

    print("The greatest number of new cases reported in Rockingham County was", greatest_number_cases_rockingham, "on", greatest_number_cases_date_rockingham)
    print("The greatest number of new cases reported in Harrisonburg City was", greatest_number_cases_harrisonburg, "on", greatest_number_cases_date_harrisonburg)

    return


def third_question(data):
    """
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    """
    # Establish pandas data frame
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # create dataset focusing on only Rockingham County VA
    data_rockingham = df.loc[(df['county'] == 'Rockingham') & (df['state'] == 'Virginia')]

    # Establish corresponding pandas data frame
    df_rockingham = pd.DataFrame(data_rockingham, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # Reset data frame index
    df_rockingham = df_rockingham.reset_index(drop=True)

    # Confirm data frame is sorted by date
    df_rockingham = df_rockingham.sort_values(by='date', ascending=True)

    # Utilize .diff to calculate difference of cases column and add it to dataframe
    df_rockingham['new cases'] = df_rockingham['cases'].diff()
    # Utilize .rolling and .mean to take the mean of the new cases over a 7 day window
    df_rockingham['7 day cases average'] = df_rockingham['new cases'].rolling(7).mean()
    # Find the id of the max average cases for the 7 day window
    max_7_day_average_rockingham = df_rockingham['7 day cases average'].idxmax()
    # Select start and end date of max 7 day average, and value of 7 day average
    greatest_average_rockingham_end = df_rockingham.loc[max_7_day_average_rockingham, 'date']  # Select max end
    greatest_average_rockingham_start = df_rockingham.loc[max_7_day_average_rockingham-7, 'date']  # Select max start
    greatest_average_rockingham = df_rockingham['7 day cases average'].max()

    # Print data frames to manually check
    '''pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df_rockingham)
    print(max_7_day_average_rockingham)
    print(greatest_average_rockingham_end)
    print(greatest_average_rockingham_start)'''

    print("The worst seven-day period in Rockingham County for new COVID cases was from",
          greatest_average_rockingham_start, "to", greatest_average_rockingham_end, "with an average of",
          greatest_average_rockingham, "cases")

    return


if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    '''for (date, county, state, cases, deaths) in data:
        print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')'''

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    print("Answers to Question 1")
    first_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    print("Answers to Question 2")
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    print("Answers to Question 3")
    third_question(data)
