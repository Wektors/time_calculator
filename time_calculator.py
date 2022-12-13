def add_time(start, duration, day = None):

    split_start = start.replace(':', " ").replace('AM', '00').replace('PM', '12').split()
    
    minutes_start = int(split_start[0]) * 60 + int(split_start[1]) + int(split_start[2]) * 60

    split_duration = duration.split(':')

    minutes_duration = int(split_duration[0]) * 60 + int(split_duration[1])

    minutes_result = minutes_start + minutes_duration

    def day_to_num(weekday):

        if weekday == "Monday":
            num = 0

        if weekday == "Tuesday":
            num = 1

        if weekday == "Wednesday":
            num = 2

        if weekday == "Thursday":
            num = 3

        if weekday == "Friday":
            num = 4

        if weekday == "Saturday":
            num = 5

        if weekday == "Sunday":
            num = 6

        if weekday == None:
            num = None

        return num

    day_num = day_to_num(day)

    days_to_add = 0

    while minutes_result > 1440:
        days_to_add += 1;
        minutes_result -= 1440

    hours_result = 0
        
    if minutes_result < 720:
        am_pm = "AM"

    elif minutes_result < 1440:
        am_pm = "PM"

    else:
        am_pm = "AM"

    while minutes_result >= 60:
        hours_result += 1
        minutes_result -= 60

    if hours_result > 12:
        hours_result -= 12

    if hours_result == 0:
        hours_result = "00"
    
    elif hours_result < 10:
        hours_result = "0" + str(hours_result)

    if minutes_result == 0:
        minutes_result = "00"


    time_result = str(hours_result) + ":" + str(minutes_result) + " " + am_pm

    if day_num != None:
        time_result += ", " + str(day_num)

    return time_result

print(add_time("12:00 AM", "12:00", "Monday"))