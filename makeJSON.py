import datetime
import json
import random
from collections import OrderedDict


def random_date(start, end):
    # start_date = datetime.date(2020, 1, 1)
    # print(start_date)
    # end_date = datetime.date(2022, 12, 31)

    start_date = datetime.datetime.strptime(str(start), "%y%m%d")
    end_date = datetime.datetime.strptime(str(end), "%y%m%d")

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date


start_value = 0
dict = {}
for i in range(100):
    rand_date = random_date(190101, 221231)
    start_value = 0

    # print(f"{rand_date}: {start_value}")
    dict[rand_date] = start_value

ordered_data = OrderedDict(sorted(dict.items(), key=lambda t: t[0]))

json_dict = {}

for date in ordered_data.keys():
    start_value = start_value + random.randint(1, 20)
    string_date = date.strftime("%Y-%m-%d")
    json_dict[string_date] = start_value
#
# for date, value in ordered_data.items():
#     print(f"{date}: {value}")

json_obj = json.dumps(json_dict)
print(json_obj)
