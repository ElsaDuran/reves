import ast
import collections

def to_dict(dataframe, column):
    dataframe[column] = dataframe[column].apply(lambda x: np.nan if pd.isnull(x) else ast.literal_eval(x))
    return dataframe


def to_list(column, key):
    new_column = column.fillna('[]').apply(ast.literal_eval).apply(lambda x: [i[key] for i in x]
    if isinstance(x, list) else [])

    return new_column


def word_count(dataframe, ref_variable):
    values_list = []

    for elements_list in dataframe[ref_variable]:
        for value in elements_list:
            values_list.append(value)

    return collections.Counter(values_list)

def is_order(input_list):
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))


def word_count2(dataframe, ref_variable):
    values_list = []

    for elements_list in dataframe[ref_variable]:
        for value in elements_list[:4]:
            values_list.append(value)

    return collections.Counter(values_list)


def word_mean(dataframe, column, variable):
    counter = word_count(dataframe, column)

    word_mean_dict = {}

    for i, x in enumerate(dataframe[column]):
        for name in x:
            if name not in word_mean_dict:
                word_mean_dict[name] = dataframe.get_value(i, variable) / counter[name]
            else:
                word_mean_dict[name] = word_mean_dict[name] + (dataframe.get_value(i, variable) / counter[name])

    return word_mean_dict

def is_ordered(input_list):
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))


def word_count2(dataframe, ref_variable):
    values_list = []

    for elements_list in dataframe[ref_variable]:
        for value in elements_list[:4]:
            values_list.append(value)

    return collections.Counter(values_list)


def media(lista):
    return np.mean(list(map(lambda x: diccionario[x] if x in diccionario else np.mean(list(diccionario.values())), lista)))
