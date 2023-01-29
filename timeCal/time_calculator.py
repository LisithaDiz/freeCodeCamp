def add_time(start, duration, day=''):
    get_time = start.split(' ')
    time = get_time[0]
    m = True
    if get_time[1] == 'AM':
        m = False

    intial_num = [int(i) for i in time.split(':')]
    adding_Num = [int(j) for j in duration.split(':')]

    if m:
        intial_num[0] = intial_num[0] + 12

    hoursPlus = (adding_Num[0] % 24)

    if adding_Num[1] + intial_num[1] < 60:
        ans_last = (adding_Num[1]) + (intial_num[1])
        ans_first = (hoursPlus + (intial_num[0])) % 12
        x = (hoursPlus + (intial_num[0])) % 24
    else:
        ans_last = (adding_Num[1]) + (intial_num[1]) - 60
        ans_first = (1 + hoursPlus + (intial_num[0])) % 12
        x = (1 + hoursPlus + (intial_num[0])) % 24

    if ans_first == 0:
        ans_first = 12

    if x >= 12:
        meri = " PM"
    else:
        meri = " AM"

    if ans_last < 10:
        ans_last = '0' + str(ans_last)

    if adding_Num[1] + intial_num[1] < 60:
        full_time_1 = adding_Num[0] + intial_num[0]
        full_time_2 = adding_Num[1] + intial_num[1]
    else:
        full_time_1 = adding_Num[0] + intial_num[0] + 1
        full_time_2 = adding_Num[1] + intial_num[1] - 60

    t = float(f'{full_time_1}.{full_time_2}')
    o = int(t / 24)
    if o == 1:
        line = ' (next day)'
    elif o > 1:
        line = f' ({o} days later)'
    else:
        line = ''

    if day == '':
        final_time = str(ans_first) + ':' + str(ans_last) + meri + line
    else:
        day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = day.capitalize()
        i = day_list.index(day)
        the_day = ', '+day_list[(i + o) % 7]
        final_time = str(ans_first) + ':' + str(ans_last) + meri + the_day + line
    return final_time
