import re
def arithmetic_arranger(problems, bool=False):
    num_1 = list()
    num_2 = list()
    total = list()
    num_of_dashes = list()
    operator = list()
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''

    x = 0
    for _ in problems:  # Error

        if len(problems) > 5:  # Error
            return "Error: Too many problems."
            quit()

        c = re.findall("[+-]", problems[x])
        if len(c) != 1:
            return "Error: Operator must be '+' or '-'."
            quit()

        t = re.split('[+-]', problems[x])
        t_0 = t[0].strip()
        t_1 = t[1].strip()
        check = re.findall('[^0123456789]', t_0 + t_1)
        if len(check) != 0:
            return 'Error: Numbers must only contain digits.'
            quit()

        t = re.split('[+-]', problems[x])
        t_0 = t[0].strip()
        t_1 = t[1].strip()
        if len(t_1) > 4 or len(t_0) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            quit()

        num_1.append(int(t_0))
        num_2.append(int(t_1))
        x += 1

    x = 0
    for _ in problems:  # Calculation
        operator.append(re.findall('[+-]', problems[x]))
        if len(re.findall('[+]', problems[x])) > 0:
            total.append(num_1[x] + num_2[x])
        else:
            total.append(num_1[x] - num_2[x])
        x += 1

    x = 0
    for _ in problems:
        if len(str(total[x])) > max(len((str(num_1[x])).strip()), len(str(num_2[x]).strip())):
            num_of_dashes.append(len(str(total[x])) + 1)

        elif len((str(num_1[x])).strip()) > len(str(num_2[x]).strip()):
            num_of_dashes.append(len(str(num_1[x]).strip()) + 2)

        else:
            num_of_dashes.append(len(str(num_2[x]).strip()) + 2)

        x += 1

    x = 0
    for _ in problems:
        if x == len(problems) - 1 :
            space = 0
        else:
            space = 4
        line_1 = line_1 + ' ' * (num_of_dashes[x] - len(str(num_1[x]))) + str(num_1[x]) + " " * space
        line_2 = line_2 + operator[x][0] + ' ' * (num_of_dashes[x] - len(str(num_2[x])) - 2) + " " + str( num_2[x]) + " " * space
        line_3 = line_3 + "-" * num_of_dashes[x] + " " * space
        line_4 = line_4 + ' ' * (num_of_dashes[x] - len(str(total[x]))) + str(total[x]) + " " * space
        x += 1

    if bool:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4

    else:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3
        
    return arranged_problems
