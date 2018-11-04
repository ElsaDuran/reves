import ast
import collections
import numpy as np
import pandas as pd
import re
import unidecode


def to_dict(dataframe, column):
    """
    This function transforms a column of a dataframe which has a dictionary that are in string format into a dictionary.  
    :params dataframe, column: dataframe and column to do the transformation
    :return dataframe: the new dataframe with the column transformed
    :libraries needed: ast, pandas
    """
    dataframe[column] = dataframe[column].apply(lambda x: np.nan if pd.isnull(x) else ast.literal_eval(x))
    return dataframe


def to_list(column, key):
    """
    This function transforms a column of a dataframe that are a list of dictionaries into a list of values according to the specified key.  
    :param column: column of the dataframe to be transformed
    :param key: key of the dictionary in which is taken the value
    :return new_column: the new column transformed
    :libraries needed: ast
    """
    new_column = column.fillna('[]').apply(ast.literal_eval).apply(lambda x: [i[key] for i in x]
    if isinstance(x, list) else [])

    return new_column


def word_count(dataframe, ref_variable, n = None):
    """
    This function obtains a collection in dictionary format with the word count holded in the column of a dataframe.  
    :param dataframe: dataframe in which are the column to obtain the word count.
    :param ref_variable: string with the name of the column of the dataframe. It is mandatory to have the values of the column in list format.
    :param n: int, upper limit of items in the list to calculate the count. By default is None, so it is calculated the word count for all items in the list.
    :return collection
    :libraries needed: collections
    """
    values_list = []

    for elements_list in dataframe[ref_variable]:
        for value in elements_list[:n]:
            values_list.append(value)

    return collections.Counter(values_list)


def is_ordered(input_list):
    """
    This function checks if a list of numbers are in order.
    :param input_list: list with the numbers.
    :return boolean (True if the list is in order, False if it is not)
    """
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))


def word_mean(dataframe, column, variable):
    """
    This function creates a dictionary in which the keys are the values contained in a column of a dataframe and the values are
    the mean of the variable defined for that key. In order to calculate the mean it is necessary calculate the count for each value
    contained in the column. For this reason this function calls the function word_count.

    :param dataframe: dataframe in which are the column and the variable needed to make the dictionary
    :param column: column in the dataframe in which the values are the keys of the dictionary. The values of the column must be in list format.
    :param variable: string with the name of the column of the dataframe on which we want to calculate the mean.
    :return dictionary. Keys: unique values obtained from column. Value: mean of the variable.
    """
    counter = word_count(dataframe, column)

    word_mean_dict = {}

    for i, x in enumerate(dataframe[column]):
        for name in x:
            if name not in word_mean_dict:
                word_mean_dict[name] = dataframe.get_value(i, variable) / counter[name]
            else:
                word_mean_dict[name] = word_mean_dict[name] + (dataframe.get_value(i, variable) / counter[name])

    return word_mean_dict


def get_mean(values_list, variable_mean_dict):
    """
    This function calculates the average of the values obtained from a list whose names are keys of a dictionary from which the numeric value is obtained. 
    In the event that a value of the list is not in the dictionary, the average value of the dictionary will be taken as value.

    :param values_list: list with strings.
    :param variable_mean_dict: dictionary with keys and value in order to obtain the value of several keys and calculate their mean.
    :return float number
    """

    return np.mean(list(map(lambda x: variable_mean_dict[x] if x in variable_mean_dict else np.mean(list(variable_mean_dict.values())), values_list)))


def get_male_count(input_list):   
    """
    This function counts how many men are in a list. 
    It is needed that the values of the list are numbers: 1 if it is a woman, 2 if it is a man.
    """
    male = 0
    for gender in input_list:
        if gender == 2:
            male += 1
    return male



def get_female_count(input_list):   
    """
    This function counts how many women are in a list. 
    It is needed that the values of the list are numbers: 1 if it is a woman, 2 if it is a man.
    """
    female = 0
    for gender in input_list:
        if gender == 1:
            female += 1
    return female




def clean(line):
    """
    This function cleans a string removing all special characters, remove accents and double spaces between words
    """
    return " ".join(unidecode.unidecode(re.sub("[^\w ]", "", line).lower().strip()).split())