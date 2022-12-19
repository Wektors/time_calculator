# time calculator

## Intro
 testing environment here is provided by freeCodeCamp, main.py is mine

if you wanna test it change the print statement at the end of main.py file and run the program
``` python
print(add_time("initial_time", "time_to_add," "day_of_the_week"))
```
## program's purpose: 

Contains a function named add_time that takes in two required parameters and one optional parameter:

* a start time in the 12-hour clock format (ending in AM or PM)
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

If the result is the next day, it should show (next day) after the time. If the result is more than one day later, shows (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result.

## Example input and output:

``` python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```