def add_time(start, duration, *day):

    split_start = start.replace(':', " ").replace('AM', '00').replace('PM', '12').split()
    
    minutes_start = int(split_start[0]) * 60 + int(split_start[1]) + int(split_start[2]) * 60

    split_duration = duration.split(':')

    minutes_duration = int(split_duration[0]) * 60 + int(split_duration[1])

    minutes_result = minutes_start + minutes_duration

    days_result = 0

    while minutes_result > 1440:
        days_result += 1;
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

    return time_result

print(add_time("12:00 AM", "12:00",))