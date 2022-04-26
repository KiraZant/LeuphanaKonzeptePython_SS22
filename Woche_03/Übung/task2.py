import pandas as pd
weather = pd.read_csv("canada_weather.csv")


def replace_minus(value):
    """
    Replaces 'false' minus sign by a regular minus sign in a given string
    :param value: String of a number in false format (str)
    :return: correctly formatted string (str)
    """
    return value.replace("−", "-")


def split_city_state(df):
    pass


def clean_temps(df, cols):
    pass

