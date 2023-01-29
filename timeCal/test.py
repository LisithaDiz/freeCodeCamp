import re
# This is testing page, Ignore this
s = '6:45'
d = (re.split('\W', s))
print(d)

test_list = ['1', '4', '3', '6', '7']

# using list comprehension to
# perform conversion
test_list = [int(i) for i in test_list]

# Printing modified list
print(test_list)
print('evec'.capitalize())
if '':
    print(2)
else:
    print(45)

day = 'Sunday'
day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Friday']
day = day.capitalize()
i = day_list.index(day)
print('')