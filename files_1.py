with open('dataset_3363_2.txt') as in_file, open('dataset.txt', 'w') as out_file:
    s1 = in_file.readline()
    # print(s1)

    # s1 = input('Type a string: ')
    num = ''
    n = 0
    temp_string = ''
    str_list = []

    for j in s1:
        if j.isdigit():
            num += j
            n += 1
        else:
            if num != '':
                if s1[n - 1].isdigit():
                    temp_string = s1[n - 2] * int(num)
                    str_list.append(temp_string)
                else:
                    temp_string = s1[n - 1] * int(num)
                    str_list.append(temp_string)
                n += 1
                num = ''
                temp_string = ''

    if num != '':
        if s1[n - 1].isdigit():
            temp_string = s1[n - 2] * int(num)
            str_list.append(temp_string)
        else:
            temp_string = s1[n - 1] * int(num)
            str_list.append(temp_string)

    # print(str_list)
    extended_str = ''.join(str_list)
    # print(extended_str)


    out_file.write(extended_str)
