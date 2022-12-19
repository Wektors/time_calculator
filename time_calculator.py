def add_time(start, duration, day = ""):

    split_start = start.replace(':', " ").replace('AM', '00').replace('PM', '12').split()
    
    minutes_start = int(split_start[0]) * 60 + int(split_start[1]) + int(split_start[2]) * 60

    split_duration = duration.split(':')

    minutes_duration = int(split_duration[0]) * 60 + int(split_duration[1])

    minutes_result = minutes_start + minutes_duration

    if day != "":
        day_num = 0

    def day_to_num(day):
        weekdays = {"monday" : 0, "tuesday" : 1, "wednesday" : 2, "thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6}
        num = weekdays.get(day.lower())
        return num

    def num_to_day(num):

        weekdays = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday"}
        while num > 6:
            num = num - 7
        day = weekdays.get(num)
        return day
    
    day_num = day_to_num(day)

    days_to_add = 0

    while minutes_result > 1440:
        days_to_add += 1;
        minutes_result -= 1440

    hours_result = 0
        
    if minutes_result < 720:
        am_pm = "AM"

    if minutes_result > 720:
        am_pm = "PM"

    else:
        am_pm = "AM"

    while minutes_result >= 60:
        hours_result += 1
        minutes_result -= 60

    if hours_result > 12:
        hours_result -= 12

    if hours_result == 0:
        hours_result = "12"

    if minutes_result == 0:
        minutes_result = "00"

    elif minutes_result < 10:
        minutes_result = "0" + str(minutes_result)


    time_result = str(hours_result) + ":" + str(minutes_result) + " " + am_pm

    if day != "":
        day_num = day_num + days_to_add
        time_result += ", " + str(num_to_day(day_num))

    if days_to_add == 1:
        time_result += " (next day)"

    if days_to_add > 1:
        time_result += " (" + str(days_to_add) + " days later)"

    return time_result
    
print(add_time("8:16 PM", "466:02", "tuesday"))