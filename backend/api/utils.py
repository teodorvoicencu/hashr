def dataframe_to_json(dataframe, fields):
    data = []
    for key, value in dataframe.to_dict().items():
        data.append({fields[0]: key, fields[1]: value})

    return data
