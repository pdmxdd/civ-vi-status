import datetime

def central_time(datetime_string):
    datetime_string_split = datetime_string.split("/")
    print(datetime_string_split)
    central_year = int(datetime_string_split[0])
    central_month = int(datetime_string_split[1])
    central_day = int(datetime_string_split[2])
    central_hour = int(datetime_string_split[3][0:2]) - 5
    if central_hour < 0:
        central_hour += 24
        central_day = int(datetime_string_split[2]) - 1
        if central_day == 0:
            if datetime_string_split[1] in ["01", "03", "05", "07", "08", "10", "12"]:
                central_day = 31
            elif datetime_string_split[1] in ["04", "06", "09", "11"]:
                central_day = 30
            else:
                # TODO: if leapyear(): central_day = 29 if leapyear(): else central_day = 28
                central_day = 28
            central_month = int(datetime_string_split[1]) - 1
            if central_month == 0:
                central_month = 12
                central_year = int(datetime_string_split[0]) - 1

    if central_day < 10:
        central_day = "0{}".format(central_day)
    if central_month < 10:
        central_month = "0{}".format(central_month)
    if central_hour < 10:
        central_hour = "0{}".format(central_hour)

    print("{}/{}/{}/{}{}".format(central_year, central_month, central_day, central_hour, datetime_string_split[3][2:]))

    return "{}/{}/{}/{}{}".format(central_year, central_month, central_day, central_hour, datetime_string_split[3][2:])


if __name__ == "__main__":
    print(datetime.datetime.utcnow().strftime("%Y/%m/%d/%H:%M:%S"))
    central_time(datetime.datetime.utcnow().strftime("%Y/%m/%d/%H:%M:%S"))
