from urllib.request import urlretrieve
import pandas as pd


def inflation_calculator(price, date_from, date_to, borough, csv_url):
    """
    Determines the price of a house given inflation between two dates in a given London borough according
    to the UK House Price Index.

    :param price: Initial price of the house of interest.
    :param date_from: 'from' date for initial price.
    :param date_to: 'to' date for final price.
    :param borough: London borough of interest.
    :param csv_url: Url of .csv file.
    :return: Price at the ‘to’ date given the change in the London borough between the 'from' and 'to' dates.
    """

    url = str(csv_url)
    urlretrieve(url, 'Data.csv')

    def calculate_inflation_rate(date_from_sub, date_to_sub):
        """
        This function calculates the rate of inflation between two dates.
        :param date_from_sub: 'from' date for initial index.
        :param date_to_sub: 'to' date for final index.
        :return: An integer representing the inflation rate between the two inputted dates.
        """

        df = pd.read_csv('Data.csv')

        if df['RegionName'].empty:
            error_value = 0
            return error_value

        data_from_index = df.loc[(df['Date'] == str(date_from_sub)) & (df['RegionName'] == borough), ['Index']]
        data_to_index = df.loc[(df['Date'] == str(date_to_sub)) & (df['RegionName'] == borough), ['Index']]

        if data_from_index.empty or data_to_index.empty:
            error_value = 0
            return error_value

        data_from_index_value = data_from_index.values[0]
        data_to_index_value = data_to_index.values[0]
        inflation_rate_sub = data_to_index_value[0] / data_from_index_value[0]
        return inflation_rate_sub

    inflation_rate = calculate_inflation_rate(date_from, date_to)
    inflated_price = price * inflation_rate
    return inflated_price


def list_of_boroughs():
    """
    This function returns a list of the boroughs in the .csv.
    :return: A list of all acceptable boroughs
    """

    df = pd.read_csv('Data.csv')
    borough_list = df.RegionName.unique()
    return borough_list


def mmyyyy_to_ddmmyyyy(mmyyyy):
    """
    Function to convert a date between MM/YYYY format and DD/MM/YYYY format,
    where the day is always the first of the month.

    :param mmyyyy: Date consisting of the month and year
    :return: Date consisting of the day, month and year
    """

    ddmmyyyy = '01/' + mmyyyy
    return ddmmyyyy
