import requests


def main_function():
    file = get_json()
    list_of_id = pull_out_id()
    for id_number in list_of_id:
        for i in file:
            if len(i) != 0 and i['id'] == id_number:
                time_data = i['date'].split('T')
                date_dash = time_data[0].split('-')
                required_date = f"{date_dash[2]}.{date_dash[1]}.{date_dash[0]}"
                disc = i['description']
                if 'from' in i:
                    from_ = i['from'].split(' ')
                    if len(from_) == 3:
                        from_num = from_[2]
                        abs_from = f"{from_[0]} {from_[1]} {from_num[:4]} {from_num[4:6]}** **** {from_num[-4:]} -> "
                    else:
                        from_num = from_[1]
                        abs_from = f"{from_[0]} {from_num[:4]} {from_num[4:6]}** **** {from_num[-4:]} -> "
                else:
                    abs_from = ''
                to = i['to'].split(' ')
                num_of_trans = to[1]
                summ = i["operationAmount"]["amount"]
                cur = i["operationAmount"]["currency"]["name"]
                print(f"{required_date} {disc}\n{abs_from}"
                      f"{to[0]} **{num_of_trans[-4:]}\n{summ} {cur}\n")


def get_json():
    file = requests.get("https://www.jsonkeeper.com/b/FGAS")
    file = file.json()
    return file


def pull_out_id():
    list_of_id = []
    dates = []
    dict_of_dates = {}

    file = get_json()

    for index in file:
        if len(index) != 0 and index['state'] == "EXECUTED":
            date_month_num = index['date'].split('T')
            year_month_day = date_month_num[0].split('-')
            index_id = index['id']
            full_date = year_month_day[0] + year_month_day[1] + year_month_day[2]
            dates.append(full_date)
            dict_of_dates[full_date] = index_id

    dates.sort(reverse=True)
    dates = dates[0:5]
    while len(list_of_id) < 5:
        for ides in dates:
            list_of_id.append(dict_of_dates[ides])
    return list_of_id
