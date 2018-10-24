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