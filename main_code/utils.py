import requests


def get_json():

    file = requests.get("https://www.jsonkeeper.com/b/FGAS")
    file = file.json()
    return file


def pull_out_id():

    list_of_id = []
    dates = []
    dict_of_dates = {}

    max_date = ['2019', '11', '00']
    file = get_json()

    for index in file:
        if len(index) != 0 and index['state'] == "EXECUTED":
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            if year_month_day[0] == max_date[0] and year_month_day[1] >= max_date[1]:
                full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
                dates.append(full_date)
                dict_of_dates[full_date] = index_id

    dates.sort(reverse=True)
    dates = dates[0:6]
    while len(list_of_id) < 5:
        for ides in dates:
            list_of_id.append(dict_of_dates[ides])
    return list_of_id
